import pytest
import allure
from GM_Arrayer.utils.get_keyword import GetKeyword
from time import sleep
from pprint import pprint


# @allure.feature('DP移液模块测试')
@allure.story('DP吸液')
@allure.title('DP吸液动作检查-吸1号位')
@allure.step('DP吸液1号样本板位置')
@allure.severity(allure.severity_level.CRITICAL)
def test_01_dp_suction(dp, dp_suction):
    result = dp.dp_suction(payload=dp_suction)
    # pprint(result)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
    pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')   # 断言响应体中信息为success


# DP加液
class TestDPFilling:
    @allure.story('DP加液-mode1')
    @allure.title('DP加液-mode1-动作检查')
    @allure.step('DP加液-吸一喷一')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02_dp_filling1(self, dp, dp_filling1):
        result = dp.dp_filling(dp_filling1)
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
        pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')  # 断言响应体中信息为success

    @allure.story('DP加液-mode2')
    @allure.title('DP加液-mode2-动作检查')
    @allure.step('DP加液-吸一喷二')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03_dp_filling2(self, dp, dp_filling2):
        result = dp.dp_filling(dp_filling2)
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
        pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')  # 断言响应体中信息为success

    @allure.story('DP加液-mode4')
    @allure.title('DP加液-mode4-动作检查')
    @allure.step('DP加液-吸一喷四')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_dp_filling4(self, dp, dp_filling4):
        result = dp.dp_filling(dp_filling4)
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
        pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')  # 断言响应体中信息为success


@allure.story('DP清洗')
@allure.title('DP清洗动作检查')
@allure.step('DP清洗流程')
@allure.severity(allure.severity_level.NORMAL)
def test_04_dp_cleaning(dp, dp_cleaning):
    result = dp.dp_cleaning(dp_cleaning)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
    pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')  # 断言响应体中信息为success


@allure.story('DP清洗池充水')
@allure.title('DP清洗池充水动作检查')
@allure.step('DP清洗池充水流程')
@allure.severity(allure.severity_level.NORMAL)
def test_05_dp_pool_filling(dp):
    result = dp.dp_pool_filling(6000)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
    pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')  # 断言响应体中信息为success


@allure.story('超声波开启')
@allure.title('超声波开启检查')
@allure.step('开启超声波')
@allure.severity(allure.severity_level.MINOR)
def test_06_dp_ultrasonic_open(dp):
    result = dp.dp_ultrasonic_open()
    sleep(3)  # 超声开启持续3s
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
    pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')  # 断言响应体中信息为success


@allure.story('超声波关闭')
@allure.title('超声波关闭检查')
@allure.step('关闭超声波')
@allure.severity(allure.severity_level.MINOR)
def test_07_dp_ultrasonic_stop(dp):
    result = dp.dp_ultrasonic_stop()
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
    pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')  # 断言响应体中信息为success


@allure.story('DP清洗池排水')
@allure.title('DP清洗池排水动作检查')
@allure.step('DP清洗池排水流程')
@allure.severity(allure.severity_level.NORMAL)
def test_08_dp_pool_drainage(dp):
    result = dp.dp_pool_drainage(10000)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)  # 断言响应状态码为200
    pytest.assume(GetKeyword.get_keyword(result, 'msg') == 'success')  # 断言响应体中信息为success

