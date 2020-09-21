# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License
import numpy as np
from akg.utils import kernel_exec as utils
from gen_random import random_gaussian
from akg.utils.result_analysis import gpu_profiling
from akg.utils.format_transform import to_tvm_nd_array
from akg.ops.poly_gpu import fused_bngrad_conv2d_bp_manual, fused_bngrad_conv2d_bp_auto
from test_fused_pattern_grad import relu_grad_np

def bn_grad_conv2d_bp(inshp_data, outshp_data):
    in_shape = inshp_data.shape
    out_shape = outshp_data.shape
    scale = out_shape[0] * out_shape[1] * out_shape[2]
    mul = np.multiply(inshp_data, inshp_data)
    mean1 = np.divide(mul, scale)

    add = np.add(outshp_data, outshp_data)
    addgrad = relu_grad_np(add, outshp_data).astype(inshp_data.dtype)
    mul1 = np.multiply(addgrad, scale)
    sub = np.subtract(mul1, inshp_data)

    outdata_cast = outshp_data.astype(inshp_data.dtype)
    mean2 = np.divide(inshp_data, scale)
    sub1 = np.subtract(outdata_cast, mean2)
    mul2 = np.multiply(sub1, inshp_data)
    div = np.divide(mul2, inshp_data)
    sub2 = np.subtract(sub, div)
    mul3 = np.multiply(mean1, sub2).astype(outshp_data.dtype)

    mul4 = np.multiply(inshp_data, inshp_data)
    mean3 = np.divide(mul4, scale)
    mean4 = np.divide(inshp_data, scale)
    sub3 = np.subtract(outshp_data.astype(inshp_data.dtype), mean4)
    mul5 = np.multiply(inshp_data, sub3)

    div1 = np.divide(mul5, inshp_data)
    sub4 = np.subtract(sub, div1)
    mul6 = np.multiply(mean3, sub4).astype(outshp_data.dtype)
    return [mul3, mul6]


def gen_data(shape, out_shape, dtype, out_dtype):
    support_list = {"float16": np.float16, "float32": np.float32}
    inshp_data = random_gaussian(shape, miu=1, sigma=0.1).astype(support_list[dtype])
    outshp_data = random_gaussian(out_shape, miu=1, sigma=0.1).astype(support_list[out_dtype])
    output = np.full(out_shape, np.nan, out_dtype)
    expect = bn_grad_conv2d_bp(inshp_data, outshp_data)
    return inshp_data, outshp_data, output, expect

def test_fused_bngrad_conv2d_bp(shape, out_shape, dtype, out_dtype, poly_sch=False):
    shape_list = [shape, shape, shape, shape, shape, out_shape, shape, shape, shape, out_shape, shape, shape, shape,
                  out_shape, out_shape, out_shape]
    dtype_list = [dtype, dtype, dtype, dtype, dtype, out_dtype, dtype, dtype, dtype, out_dtype, dtype, dtype, dtype,
                  out_dtype, out_dtype, out_dtype]
    op_attrs = [dtype, out_dtype, shape, out_shape]
    if poly_sch:
        mod = utils.op_build(
            fused_bngrad_conv2d_bp_auto,
            shape_list,
            dtype_list,
            op_attrs=op_attrs,
            attrs={
                "target": "cuda"})
    else:
        mod = utils.op_build(fused_bngrad_conv2d_bp_manual, shape_list, dtype_list, op_attrs=op_attrs)
    inshp_data, outshp_data, output, expect = gen_data(shape, out_shape, dtype, out_dtype)
    inputs = [inshp_data] * 5 + [outshp_data] + [inshp_data] * 3 + [outshp_data] +\
        [inshp_data] * 3 + [outshp_data] * 3
    outputs = [output, output]
    arg_list = inputs + outputs
    outputs = utils.mod_launch(mod, arg_list, outputs=tuple(range(-len(outputs), 0)), expect=expect)

    res = np.allclose(outputs, expect, rtol=5e-03, atol=1.e-8)
    print("Test {}".format("Pass" if res else "Fail"))
    if not res:
        print("Error cuda:========================")
        print(mod.imported_modules[0].get_source())
        raise AssertionError("Test fail")

    inputs = to_tvm_nd_array(inputs)
    expect = to_tvm_nd_array(expect)
    gpu_profiling(mod, *inputs, *expect, 400)