import pytest
import allure
from GM_Arrayer.utils.get_keyword import GetKeyword


class TestDiaphragmPlaten:
    @allure.story('压膜板推出功能')
    @allure.title('压膜板推出检查')
    @allure.step('压膜板推出动作反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_diaphragm_platen_out(self, heat_seal_flow):
        result = heat_seal_flow.diaphragm_platen_out()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

    @allure.story('压膜板收回功能')
    @allure.title('压膜板收回检查')
    @allure.step('压膜板收回动作反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_02_diaphragm_platen_return(self, heat_seal_flow):
        result = heat_seal_flow.diaphragm_platen_return()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


class TestHeatSealZAxis:
    @allure.story('热封Z轴运动功能')
    @allure.title('热封Z轴运动检查')
    @allure.step('热封Z轴运动动作反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_03_heat_seal_z_axis_move(self, heat_seal_flow):
        result = heat_seal_flow.heat_seal_z_axis_move()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

    @allure.story('读取热封Z轴位置功能')
    @allure.title('读取热封Z轴位置检查')
    @allure.step('读取热封Z轴位置反馈')
    @allure.severity(allure.severity_level.MINOR)
    def test_04_heat_seal_z_read_pos(self, heat_seal_flow):
        result = heat_seal_flow.heat_seal_z_read_pos()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')
        pytest.assume(GetKeyword.get_keyword(result, 'data') == 45)

    @allure.story('热封Z轴回原功能')
    @allure.title('热封Z轴回原检查')
    @allure.step('热封Z轴回原动作反馈')
    @allure.severity(allure.severity_level.MINOR)
    def test_05_heat_seal_z_home(self, heat_seal_flow):
        result1 = heat_seal_flow.heat_seal_z_home()
        result2 = heat_seal_flow.heat_seal_z_read_pos()
        pytest.assume(GetKeyword.get_keyword(result1, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result1, 'des') == 'success')
        pytest.assume(GetKeyword.get_keyword(result2, 'data') == 0)


class TestTranSection:
    @allure.story('热封横切出刀功能')
    @allure.title('热封横切出刀检查')
    @allure.step('热封横切出刀动作反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_06_tran_section_out(self, heat_seal_flow):
        result = heat_seal_flow.tran_section_out()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

    @allure.story('热封横切收刀功能')
    @allure.title('热封横切收刀检查')
    @allure.step('热封横切收刀动作反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_07_tran_section_return(self, heat_seal_flow):
        result = heat_seal_flow.tran_section_return()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


class TestVerticalCutting:
    @allure.story('热封竖切出刀功能')
    @allure.title('热封竖切出刀检查')
    @allure.step('热封竖切出刀动作反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_08_vertical_cutting_out(self, heat_seal_flow):
        result = heat_seal_flow.vertical_cutting_out()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

    @allure.story('热封竖切收刀功能')
    @allure.title('热封竖切收刀检查')
    @allure.step('热封竖切收刀动作反馈')
    @allure.severity(allure.severity_level.NORMAL)
    def test_09_vertical_cutting_return(self, heat_seal_flow):
        result = heat_seal_flow.vertical_cutting_return()
        pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
        pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


@allure.story('热封卷膜预切功能')
@allure.title('热封卷膜预切检查')
@allure.step('热封卷膜预切动作反馈')
@allure.severity(allure.severity_level.CRITICAL)
def test_10_heat_seal_pre_cut_film(heat_seal_flow):
    result = heat_seal_flow.heat_seal_pre_cut_film()
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

@allure.story('热封动作流程')
@allure.title('热封动作流程检查')
@allure.step('热封动作流程反馈')
@allure.severity(allure.severity_level.CRITICAL)
def test_11_heat_seal_flow(heat_seal_flow):
    result = heat_seal_flow.heat_seal_flow()
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

