# 机械臂调试：机械臂抓取和放置耗材
from GM_Arrayer.utils.requests_plus import *


class DebugArmMove:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def arm_grab(self, pos_num, consume_type):
        """
        机械臂抓取耗材
        @param pos_num: 抓的位置编号
        @param consume_type: 耗材类型（样本板是1，反应板是2）
        @return:
        """
        url = self.url + '/device/debug/arm/grab'
        payload = {
            'posNum': pos_num,
            'consumeType': consume_type
        }
        return RequestsPlus('post', url, params=payload).res_obj()

    def arm_put(self, pos_num, consume_type):
        """
        机械臂放置耗材
        @param pos_num: 放的位置编号
        @param consume_type: 耗材类型（样本板是1，反应板是2）
        @return:
        """
        url = self.url + '/device/debug/arm/put'
        payload = {
            'posNum': pos_num,
            'consumeType': consume_type
        }
        return RequestsPlus('post', url, params=payload).res_obj()


if __name__ == '__main__':
    dam = DebugArmMove()
    # 调试
    pprint(dam.arm_grab(1, 2))
    pprint(dam.arm_put(85, 2))

    pprint(dam.arm_grab(85, 2))
    pprint(dam.arm_put(1, 2))

