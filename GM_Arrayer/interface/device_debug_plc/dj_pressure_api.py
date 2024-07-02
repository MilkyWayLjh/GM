# PLC调试接口：DJ4压力储液罐充排水 DJ4气压调节 调试相关接口
from GM_Arrayer.utils.requests_plus import *


class DJPressureApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def dj_pressure_tank_drainage(self, time=15000):
        """
        DJ4压力储液罐排水
        @param time:排水时间ms <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actPressureTankDrainage'
        payload = {
            "time": time
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj_pressure_tank_fill(self):
        """
        DJ4压力罐充水
        @return:
        """
        url = self.url + '/device/debug/plc/actPressureTankRefill'
        return RequestsPlus('get', url).res_obj()

    def dj_pressure_regulating(self, value=13):
        """
        DJ4气压调节
        @param value:气压值 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actDJ4PressureRegulating'
        payload = {
            "value": value
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj_read_pressure_value(self):
        """
        DJ4当前气压值
        @return:
        """
        url = self.url + '/device/debug/plc/readDJ4BarometricValue'
        return RequestsPlus('get', url).res_obj()

if __name__ == '__main__':
    dj_p = DJPressureApi()
    # 调试
    dj_p.dj_pressure_tank_drainage()
    dj_p.dj_pressure_tank_fill()
    dj_p.dj_pressure_regulating()
    pprint(dj_p.dj_read_pressure_value())

