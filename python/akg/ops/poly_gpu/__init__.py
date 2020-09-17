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
# limitations under the License.

"""__init__"""
from .equal import equal_manual, equal_auto
from .greater_equal import greater_equal_manual, greater_equal_auto
from .less_equal import less_equal_manual, less_equal_auto
from .cast import cast_manual, cast_auto
from .tile import tile_manual, tile_auto
from .one_hot import one_hot_manual, one_hot_auto
from .sqrt import sqrt_manual, sqrt_auto
from .sub import sub_manual, sub_auto
from .add import add_manual, add_auto
from .addn import addn_manual, addn_auto
from .rsqrt import rsqrt_manual, rsqrt_auto
from .expand_dims import expand_dims_manual, expand_dims_auto
from .batch_matmul import batch_matmul_manual, batch_matmul_auto
from .mul import mul_manual, mul_auto
from .exp import exp_manual, exp_auto
from .divide import divide_manual, divide_auto
from .maximum import maximum_manual, maximum_auto
from .minimum import minimum_manual, minimum_auto
from .reshape import reshape_manual, reshape_auto
from .trans_data import trans_data_manual, trans_data_auto
from .log import log_manual, log_auto
from .pow import pow_manual, pow_auto
from .reduce_sum import reduce_sum_manual, reduce_sum_auto
from .abs import abs_manual, abs_auto
from .neg import neg_manual, neg_auto
from .round import round_manual, round_auto
from .select import select_manual, select_auto
from .reciprocal import reciprocal_manual, reciprocal_auto
from .reduce_min import reduce_min_manual, reduce_min_auto
from .reduce_max import reduce_max_manual, reduce_max_auto
from .fused_conv2d_bn import fused_conv2d_bn_manual, fused_conv2d_bn_auto
from .fused_bn_update import fused_bn_update_manual, fused_bn_update_auto
from .fused_bngrad_conv2d_bp import fused_bngrad_conv2d_bp_manual, fused_bngrad_conv2d_bp_auto
from .fused_bn_relu import fused_bn_relu_manual, fused_bn_relu_auto
from .fused_relugrad import fused_relugrad_manual, fused_relugrad_auto
from .fused_bn_double_relu import fused_bn_double_relu_manual, fused_bn_double_relu_auto
from .fused_bn_relu_avgpool import fused_bn_relu_avgpool_manual, fused_bn_relu_avgpool_auto
from .fused_bngrad_conv2dbp_0 import fused_bngrad_conv2dbp_0_manual, fused_bngrad_conv2dbp_0_auto
from .fused_bn_grad import fused_bn_grad_manual, fused_bn_grad_auto
from .fused_bn_update_grad import fused_bn_update_grad_manual, fused_bn_update_grad_auto
from .fused_conv2d_bp_bn_grad import fused_conv2d_bp_bn_grad_manual, fused_conv2d_bp_bn_grad_auto
from .fused_l2loss import fused_l2loss_manual, fused_l2loss_auto
from .fused_cast_pad import fused_cast_pad_manual, fused_cast_pad_auto
from .fused_bngrad_conv2dback import fused_bngrad_conv2dback_manual, fused_bngrad_conv2dback_auto
from .fused_conv2dback_l2loss import fused_conv2dback_l2loss_manual, fused_conv2dback_l2loss_auto
from .fused_conv2dback_bngrad import fused_conv2dback_bngrad_manual, fused_conv2dback_bngrad_auto
from .pad import pad_manual, pad_auto
from .resize import resize_manual, resize_auto
from .resize_nearest_neighbor_grad import resize_nearest_neighbor_grad_manual, resize_nearest_neighbor_grad_auto
