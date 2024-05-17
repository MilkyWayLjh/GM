import pytest
from GM_Arrayer.utils.data_operation import DataOperation
from GM_Arrayer.interface.device_debug_plc.dp_api import DPApi
from GM_Arrayer.interface.device_debug_plc.xyz_axis_move_api import AxisMoveApi


# 封装获取数据操作方法
def get_data(filename):
    do = DataOperation(filename)
    data = do.get_json_data()
    return data


# dp相关模块
@pytest.fixture()
def dp():
    dp = DPApi()
    yield dp


# dp吸液参数化
@pytest.fixture(params=[get_data('dp_parameter.json')[1]])
def dp_suction(request):
    return request.param


# dp加液参数-mode1
@pytest.fixture(params=[get_data('dp_parameter.json')[3]])
def dp_filling1(request):
    return request.param


# dp加液参数-mode2
@pytest.fixture(params=[get_data('dp_parameter.json')[5]])
def dp_filling2(request):
    return request.param


# dp加液参数-mode4
@pytest.fixture(params=[get_data('dp_parameter.json')[7]])
def dp_filling4(request):
    return request.param


# dp清洗参数
@pytest.fixture(params=[get_data('dp_parameter.json')[9]])
def dp_cleaning(request):
    return request.param


# xyz轴移动相关模块
@pytest.fixture()
def xyz_axis():
    xyz_axis = AxisMoveApi()
    yield xyz_axis


