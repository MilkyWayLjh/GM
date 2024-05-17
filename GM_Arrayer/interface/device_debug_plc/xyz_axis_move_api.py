# PLC调试接口：XYZ轴移动 调试相关接口
from GM_Arrayer.utils.requests_plus import *


class AxisMoveApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8080/api/v1'

    def x_axis_move(self, position=295, speed=60):
        """
        X轴运动
        @param position: 位置 <number>
        @param speed: 速度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actXAxisMove'
        payload = {
            "position": position,
            "speed": speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def x_axis_read_position(self):
        # X轴当前位置
        url = self.url + '/device/debug/plc/readXActualPosition'
        return RequestsPlus('get', url).res_obj()

    def x_axis_home(self):
        # X轴回原
        url = self.url + '/device/debug/plc/actXAxisHome'
        return RequestsPlus('get', url).res_obj()

    def y_axis_move(self, position=81, speed=60):
        """
        Y轴运动
        @param position: 位置 <number>
        @param speed: 速度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actYAxisMove'
        payload = {
            "position": position,
            "speed": speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def y_axis_read_position(self):
        # Y轴当前位置
        url = self.url + '/device/debug/plc/readYActualPosition'
        return RequestsPlus('get', url).res_obj()

    def y_axis_home(self):
        # Y轴回原
        url = self.url + '/device/debug/plc/actYAxisHome'
        return RequestsPlus('get', url).res_obj()

    def z_axis_move(self, position=35, speed=60):
        """
        Z轴运动
        @param position: 位置 <number>
        @param speed: 速度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actZAxisMove'
        payload = {
            "position": position,
            "speed": speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def z_axis_read_position(self):
        # Z轴当前位置
        url = self.url + '/device/debug/plc/readZActualPosition'
        return RequestsPlus('get', url).res_obj()

    def z_axis_home(self):
        # Z轴回原
        url = self.url + '/device/debug/plc/actZAxisHome'
        return RequestsPlus('get', url).res_obj()

    def z_two_speed_exercises(self, z_change_position=15, z_first_speed=20, z_position=35, z_second_speed=60):
        """
        Z轴两段速运动
        @param z_change_position: Z轴变速位 <number>
        @param z_first_speed: Z轴第一段速 <number>
        @param z_position: Z轴目标位 <number>
        @param z_second_speed: Z轴第二段速 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actZTwoSpeedExercises'
        payload = {
            "zchangePosition": z_change_position,
            "zfirstSpeed": z_first_speed,
            "zposition": z_position,
            "zsecondSpeed": z_second_speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def xyz_linked_move(self, x_position=66, x_speed=60, y_position=325.5, y_speed=60,
                        z_position=0, z_safety_position=35, z_speed=60):
        """
        XYZ联动
        @param x_position: X位置 <number>
        @param x_speed: X速度 <number>
        @param y_position: Y位置 <number>
        @param y_speed: Y速度 <number>
        @param z_position: Z位置 <number>
        @param z_safety_position: Z安全位置 <number>
        @param z_speed: z速度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actXYZLinkedMove'
        payload = {
            "xposition": x_position,
            "xspeed": x_speed,
            "yposition": y_position,
            "yspeed": y_speed,
            "zposition": z_position,
            "zsafetyPosition": z_safety_position,
            "zspeed": z_speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()


if __name__ == '__main__':
    am = AxisMoveApi()
    # 调试
    pprint(am.x_axis_read_position())
    pprint(am.y_axis_read_position())
    pprint(am.z_axis_read_position())

    am.xyz_linked_move()

