# PLC调试接口：DJ z轴运动和柱塞泵调试相关接口
from GM_Arrayer.utils.requests_plus import *


class DJMotionApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def dj4_z_axis_move(self, dj4_z_position=60, dj4_z_speed=60):
        """
        DJ4 Z轴运动
        @param dj4_z_position: 位置 <number>
        @param dj4_z_speed: 速度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actDJ4ZAxisMove'
        payload = {
            "dj4ZPosition": dj4_z_position,
            "dj4ZSpeed": dj4_z_speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_read_position(self):
        """
        读取DJ4 Z轴当前位置
        @return:
        """
        url = self.url + '/device/debug/plc/readDJ4ZPistonPumpPosition'
        return RequestsPlus('get', url).res_obj()

    def dj4_z_axis_home(self):
        """
        DJ4 Z轴回原
        @return:
        """
        url = self.url + '/device/debug/plc/actDJ4ZAxisHome'
        return RequestsPlus('get', url).res_obj()

    def dj4_piston_pump_move(self, position=5, speed=1):
        """
        DJ4 柱塞泵运行
        @param position: 位置<number>
        @param speed: 速度<number>
        @return:
        """
        url = self.url + '/device/debug/plc/actDJ4PistonPumpMove'
        payload = {
            "position": position,
            "speed": speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_read_piston_pump_position(self):
        """
        DJ4柱塞泵当前位置
        @return:
        """
        url = self.url + '/device/debug/plc/readDJ4PistonPumpPosition'
        return RequestsPlus('get', url).res_obj()

    def dj4_piston_pump_home(self):
        """
        DJ4柱塞泵回原
        @return:
        """
        url = self.url + '/device/debug/plc/actDJ4PistonPumpHome'
        return RequestsPlus('get', url).res_obj()

if __name__ == '__main__':
    dj = DJMotionApi()
    # 调试
    dj.dj4_z_axis_move()
    pprint(dj.dj4_read_position())
    dj.dj4_z_axis_home()
    dj.dj4_piston_pump_move()
    pprint(dj.dj4_read_piston_pump_position())
    dj.dj4_piston_pump_home()

