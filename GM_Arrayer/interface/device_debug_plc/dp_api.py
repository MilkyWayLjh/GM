# PLC调试接口：DP头调试相关接口
from GM_Arrayer.utils.requests_plus import *
from GM_Arrayer.utils.data_operation import DataOperation
from time import sleep


class DPApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def dp_suction(self, payload):
        """
        DP吸液
        @param payload: 请求体中json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDPSuction'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dp_filling(self, payload):
        """
        DP加液
        @param payload: 请求体中json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDPFilling'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dp_cleaning(self, payload):
        """
        DP清洗
        @param payload: 请求体中json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDPCleaning'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dp_pool_filling(self, time):
        """
        DP清洗池充水
        @param time: 充水时间 <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actDPCleaningPool'
        payload = {
            "time": time
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dp_ultrasonic_open(self):
        """
        超声波开启
        @return:
        """
        url = self.url + '/device/debug/plc/actUltrasonicOpen'
        return RequestsPlus('get', url).res_obj()

    def dp_ultrasonic_stop(self):
        """
        超声波关闭
        @return:
        """
        url = self.url + '/device/debug/plc/actUltrasonicStop'
        return RequestsPlus('get', url).res_obj()

    def dp_pool_drainage(self, time):
        """
        DP清洗池排水
        @param time: 排水时间 <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actDPWashBasinDrainage'
        payload = {
            "time": time
        }
        return RequestsPlus('post', url, json=payload).res_obj()

if __name__ == '__main__':
    dp = DPApi()
    # 读取DP参数
    do = DataOperation('dp_parameter.json')
    # 调试DP
    # DP吸液
    data1 = do.get_json_data()[1]
    pprint(dp.dp_suction(payload=data1))

    # DP加液
    data2 = do.get_json_data()[7]
    pprint(dp.dp_filling(payload=data2))

    # DP清洗
    data3 = do.get_json_data()[9]
    pprint(dp.dp_cleaning(payload=data3))

    # DP清洗池充水
    pprint(dp.dp_pool_filling(6000))

    # 超声波开启
    pprint(dp.dp_ultrasonic_open())
    sleep(3)
    # 超声波关闭
    pprint(dp.dp_ultrasonic_stop())

    # DP清洗池排水
    pprint(dp.dp_pool_drainage(10000))

