import pytest
import allure
from GM_Arrayer.utils.get_keyword import GetKeyword


@allure.story('机械臂抓取耗材-反应板')
@allure.title('机械臂抓取耗材检查-反应板')
@allure.step('机械臂抓取耗材动作反馈-反应板')
@allure.severity(allure.severity_level.CRITICAL)
def test_01_arm_grab(arm_move):
    result = arm_move.arm_grab(1, 2)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

@allure.story('机械臂放置耗材-反应板')
@allure.title('机械臂放置耗材检查-反应板')
@allure.step('机械臂放置耗材动作反馈-反应板')
@allure.severity(allure.severity_level.CRITICAL)
def test_02_arm_put(arm_move):
    result = arm_move.arm_put(85, 2)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


@allure.story('机械臂抓回耗材-反应板')
@allure.title('机械臂抓回耗材检查-反应板')
@allure.step('机械臂抓回耗材动作反馈-反应板')
@allure.severity(allure.severity_level.CRITICAL)
def test_03_arm_grab(arm_move):
    result = arm_move.arm_grab(85, 2)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


@allure.story('机械臂放回耗材-反应板')
@allure.title('机械臂放回耗材检查-反应板')
@allure.step('机械臂放回耗材动作反馈-反应板')
@allure.severity(allure.severity_level.CRITICAL)
def test_04_arm_put(arm_move):
    result = arm_move.arm_put(1, 2)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


@allure.story('机械臂抓取耗材-样本板')
@allure.title('机械臂抓取耗材检查-样本板')
@allure.step('机械臂抓取耗材动作反馈-样本板')
@allure.severity(allure.severity_level.NORMAL)
def test_05_arm_grab(arm_move):
    result = arm_move.arm_grab(6, 1)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


@allure.story('机械臂放置耗材-样本板')
@allure.title('机械臂放置耗材检查-样本板')
@allure.step('机械臂放置耗材动作反馈-样本板')
@allure.severity(allure.severity_level.NORMAL)
def test_06_arm_put(arm_move):
    result = arm_move.arm_put(81, 1)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


@allure.story('机械臂抓回耗材-样本板')
@allure.title('机械臂抓回耗材检查-样本板')
@allure.step('机械臂抓回耗材动作反馈-样本板')
@allure.severity(allure.severity_level.NORMAL)
def test_07_arm_grab(arm_move):
    result = arm_move.arm_grab(81, 1)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')


@allure.story('机械臂放回耗材-样本板')
@allure.title('机械臂放回耗材检查-样本板')
@allure.step('机械臂放回耗材动作反馈-样本板')
@allure.severity(allure.severity_level.NORMAL)
def test_08_arm_put(arm_move):
    result = arm_move.arm_put(6, 1)
    pytest.assume(GetKeyword.get_keyword(result, 'status_code') == 200)
    pytest.assume(GetKeyword.get_keyword(result, 'des') == 'success')

