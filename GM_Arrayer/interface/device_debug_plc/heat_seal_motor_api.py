# PLC调试接口：热封电机动作，U轴动作，温度控制 调试相关接口
from GM_Arrayer.utils.requests_plus import *


class HeatSealMotorApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def rolling_film_motor_start(self):
        """
        卷膜电机启动
        @return:
        """
        url = self.url + '/device/debug/plc/actRollingFilmMotorStarts'
        return RequestsPlus('get', url).res_obj()

    def rolling_film_motor_stop(self):
        """
        卷膜电机停止
        @return:
        """
        url = self.url + '/device/debug/plc/actCoilMotorStops'
        return RequestsPlus('get', url).res_obj()

    def u_axis_move(self, position=200, speed=60):
        """
        U轴运动
        @param position: 位置<number>
        @param speed: 速度<number>
        @return:
        """
        url = self.url + '/device/debug/plc/actUAxisMove'
        payload = {
            "position": position,
            "speed": speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def u_axis_read_position(self):
        """
        U轴当前位置
        @return:
        """
        url = self.url + '/device/debug/plc/readUActualPosition'
        return RequestsPlus('get', url).res_obj()

    def u_axis_home(self):
        """
        U轴回原
        @return:
        """
        url = self.url + '/device/debug/plc/actUAxisHome'
        return RequestsPlus('get', url).res_obj()

    def heat_temperature_control(self, sensor1k=1, sensor1b=0, sensor2k=1, sensor2b=0,
                                 target_temperature=50, temperature_difference=10):
        """
        热封温度控制
        @param sensor1k: 1号传感器K值 <number>
        @param sensor1b: 1号传感器B值 <number>
        @param sensor2k: 2号传感器K值 <number>
        @param sensor2b: 2号传感器B值 <number>
        @param target_temperature: 目标温度 <number>
        @param temperature_difference: 温差值 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actHeatTemperatureControl'
        payload = {
            "sensor1B": sensor1b,
            "sensor1K": sensor1k,
            "sensor2B": sensor2b,
            "sensor2K": sensor2k,
            "targetTemperature": target_temperature,
            "temperatureDifference": temperature_difference
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def read_heat_seal_temperature1(self):
        """
        读取热封1号温度传感器
        @return:
        """
        url = self.url + '/device/debug/plc/readHeatSealTemperature1'
        return RequestsPlus('get', url).res_obj()

    def read_heat_seal_temperature2(self):
        """
        读取热封2号温度传感器
        @return:
        """
        url = self.url + '/device/debug/plc/readHeatSealTemperature2'
        return RequestsPlus('get', url).res_obj()

if __name__ == '__main__':
    hs = HeatSealMotorApi()
    pprint(hs.u_axis_read_position())
    pprint(hs.read_heat_seal_temperature1())
