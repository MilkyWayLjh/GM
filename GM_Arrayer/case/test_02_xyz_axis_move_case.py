import pytest
import allure
from GM_Arrayer.utils.get_keyword import GetKeyword


class TestXAxis:
    @allure.story('X轴移动功能')
    @allure.title('X轴运动检查')
    @allure.step('X轴动作反馈')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01_x_axis_move(self, xyz_axis):
        result = xyz_axis.x_axis_move()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

    @allure.story('读取X轴位置功能')
    @allure.title('读取X轴当前位置')
    @allure.step('X轴读取反馈')
    @allure.severity(allure.severity_level.MINOR)
    def test_02_x_axis_read_position(self, xyz_axis):
        result = xyz_axis.x_axis_read_position()
        print(result)
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'data') == 295)

    @allure.story('X轴回原功能')
    @allure.title('X轴回原')
    @allure.step('X轴回原反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_x_axis_home(self, xyz_axis):
        result1 = xyz_axis.x_axis_home()
        result2 = xyz_axis.x_axis_read_position()
        print(result2)
        pytest.assume(GetKeyword.get_keyword(result1, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result1, 'des') == 'success')
        pytest.assume(GetKeyword.get_keyword(result2, 'data') == 0)


class TestYAxis:
    @allure.story('Y轴移动功能')
    @allure.title('Y轴运动检查')
    @allure.step('Y轴动作反馈')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_04_y_axis_move(self, xyz_axis):
        result = xyz_axis.y_axis_move()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

    @allure.story('读取Y轴位置功能')
    @allure.title('读取Y轴当前位置')
    @allure.step('Y轴读取反馈')
    @allure.severity(allure.severity_level.MINOR)
    def test_05_y_axis_read_position(self, xyz_axis):
        result = xyz_axis.y_axis_read_position()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'data') == 81)

    @allure.story('Y轴回原功能')
    @allure.title('Y轴回原')
    @allure.step('Y轴回原反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_y_axis_home(self, xyz_axis):
        result1 = xyz_axis.y_axis_home()
        result2 = xyz_axis.y_axis_read_position()
        pytest.assume(GetKeyword.get_keyword(result1, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result1, 'des') == 'success')
        pytest.assume(GetKeyword.get_keyword(result2, 'data') == 0)


class TestZAxis:
    @allure.story('Z轴移动功能')
    @allure.title('Z轴运动检查')
    @allure.step('Z轴动作反馈')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_07_z_axis_move(self, xyz_axis):
        result = xyz_axis.z_axis_move()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

    @allure.story('读取Z轴位置功能')
    @allure.title('读取Z轴当前位置')
    @allure.step('Z轴读取反馈')
    @allure.severity(allure.severity_level.MINOR)
    def test_08_z_axis_read_position(self, xyz_axis):
        result = xyz_axis.z_axis_read_position()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'data') == 35)

    @allure.story('Z轴回原功能')
    @allure.title('Z轴回原')
    @allure.step('Z轴回原反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_z_axis_home(self, xyz_axis):
        result1 = xyz_axis.z_axis_home()
        result2 = xyz_axis.z_axis_read_position()
        pytest.assume(GetKeyword.get_keyword(result1, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result1, 'des') == 'success')
        pytest.assume(GetKeyword.get_keyword(result2, 'data') == 0)

    @allure.story('Z轴两段速运动功能')
    @allure.title('Z轴两段速运动')
    @allure.step('Z轴两段速运动反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_10_z_two_speed_exercises(self, xyz_axis):
        result = xyz_axis.z_two_speed_exercises()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


@allure.story('XYZ联动功能')
@allure.title('XYZ联动')
@allure.step('XYZ联动反馈')
@allure.severity(allure.severity_level.CRITICAL)
def test_11_xyz_linked_move(xyz_axis):
    result = xyz_axis.xyz_linked_move()
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

