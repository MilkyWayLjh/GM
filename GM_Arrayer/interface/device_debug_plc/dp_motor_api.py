# PLC调试接口：DP轴活塞调试相关接口
from GM_Arrayer.utils.requests_plus import *


class DPMotorApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def dp_axis_move(self, position=5, speed=2):
        """
        DP轴运动(DP活塞运动)
        @param position: 运动位置 <number>
        @param speed: 速度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actDPAxisMove'
        payload = {
            "position": position,
            "speed": speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dp_read_position(self):
        """
        读取DP活塞当前位置
        @return: DP活塞当前位置
        """
        url = self.url + '/device/debug/plc/readDPPistonPumpPosition'
        return RequestsPlus('get', url).res_obj()

    def dp_axis_home(self):
        """
        DP活塞回原
        @return:
        """
        url = self.url + '/device/debug/plc/actDPAxisHome'
        return RequestsPlus('get', url).res_obj()

    def dp_reciprocating_motion(self, positional1=1, positional2=6, reciprocating_speed=2, time=5000):
        """
        DP活塞电机往复运动
        @param positional1: 位置1 <number>
        @param positional2: 位置2 <number>
        @param reciprocating_speed: 往复速度 <number>
        @param time: 往复时间 <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actReciprocatingPistonMotion'
        payload = {
            "positional1": positional1,
            "positional2": positional2,
            "reciprocatingSpeed": reciprocating_speed,
            "time": time
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dp_motor_release(self):
        """
        DP活塞松 解锁
        @return:
        """
        url = self.url + '/device/debug/plc/actDPMotorRelease'
        return RequestsPlus('get', url).res_obj()

    def dp_motor_tight(self):
        """
        DP活塞紧 锁定
        @return:
        """
        url = self.url + '/device/debug/plc/actDPMotorTight'
        return RequestsPlus('get', url).res_obj()


if __name__ == '__main__':
    dp = DPMotorApi()
    # pprint(dp.dp_axis_move(5, 3))
    # pprint(dp.dp_axis_move())
    # pprint(dp.dp_read_position())
    # pprint(dp.dp_axis_home())
    # pprint(dp.dp_reciprocating_motion(1, 6, 3, 3000))
    # pprint(dp.dp_reciprocating_motion())
    # pprint(dp.dp_motor_release())
    # pprint(dp.dp_motor_tight())
