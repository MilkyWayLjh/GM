# PLC调试接口：DJ喷液 吸液 清洗 充排水 调试相关接口
from GM_Arrayer.utils.requests_plus import *
from GM_Arrayer.utils.data_operation import DataOperation


class DJApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8080/api/v1'

    def dj4_long_spray(self, spray_time1=2000, spray_time2=2000, spray_time3=2000, spray_time4=2000):
        """
        DJ4长喷
        @param spray_time1:喷液时间1 <integer>
        @param spray_time2:喷液时间2 <integer>
        @param spray_time3:喷液时间3 <integer>
        @param spray_time4:喷液时间4 <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actDJ4LongSpray'
        payload = {
            "sprayTime1": spray_time1,
            "sprayTime2": spray_time2,
            "sprayTime3": spray_time3,
            "sprayTime4": spray_time4
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_large_volume_spray(self, payload):
        """
        DJ4大体积喷液
        @param payload:请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDJLargeVolumeSpray'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_micro_spray(self, payload):
        """
        DJ微体系喷液(竖喷)
        @param payload:请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDJMicroSystem'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_spray(self, payload):
        """
        DJ4预喷点喷  前置接口：1、DJ微体系喷液
        @param payload:请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actLargeSystemSpray'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj_pool_filling(self, time=5000):
        """
        DJ清洗池充水
        @param time: 充水时间ms <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actDJCleaningPool'
        payload = {
            "time": time
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj_pool_drainage(self, time=8000):
        """
        DJ清洗池排水
        @param time: 排水时间ms <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actDJWashBasinDrainage'
        payload = {
            "time": time
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_cleaning(self, payload):
        """
        DJ4清洗
        @param payload:请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDJ4Cleaning'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_suction_inplace(self, payload):
        """
        DJ4原地吸液
        @param payload:请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDJSuctionInPlace'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_suction_quadruple_pump(self, payload):
        """
        DJ4四联柱塞泵吸液
        @param payload:请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDJ4QuadruplePlungerPumpSuction'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_deep_cleaning(self, payload):
        """
        DJ4深度清洗  前置接口：1、DJ充水。2、DJ排水。3、DJ4清洗。4、DJ原地吸液。5、DJ4四联柱塞泵吸液
        @param payload:请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actDJDeepCleaning'
        return RequestsPlus('post', url, json=payload).res_obj()

    def dj4_inner_wall_cleaning(self, delay_after_valve1=1000, delay_after_valve2=1000,
                                delay_open_valve=3000, delay_stop_pump_valve=1000):
        """
        DJ4内壁清洗
        @param delay_after_valve1:停阀后延时1 <integer>
        @param delay_after_valve2:停阀后延时2 <integer>
        @param delay_open_valve:开阀后延时 <integer>
        @param delay_stop_pump_valve:延时停泵阀 <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actDJInnerWallCleaning'
        payload = {
            "delayAfterValve1": delay_after_valve1,
            "delayAfterValve2": delay_after_valve2,
            "delayOpenValve": delay_open_valve,
            "delayStopPumpValve": delay_stop_pump_valve
        }
        return RequestsPlus('post', url, json=payload).res_obj()


if __name__ == '__main__':
    dj = DJApi()
    # 调试
    # DJ4长喷
    # dj.dj4_long_spray()

    # DJ4大体积喷液
    do = DataOperation('dj4_large_volume_spray.json')
    data1 = do.get_json_data()[7]
    # dj.dj4_large_volume_spray(payload=data1)

    # DJ4微体系喷液(竖喷)
    do = DataOperation('dj4_micro_spray.json')
    data2 = do.get_json_data()[5]
    # dj.dj4_micro_spray(payload=data2)
    # DJ4预喷点喷
    do = DataOperation('dj4_micro_spray.json')
    data3 = do.get_json_data()[9]
    # dj.dj4_spray(payload=data3)

    # DJ清洗池充水/排水
    # dj.dj_pool_filling()
    # dj.dj_pool_drainage()

    # DJ4清洗
    do = DataOperation('dj4_cleaning.json')
    data4 = do.get_json_data()[1]
    # dj.dj4_cleaning(payload=data4)

    # DJ4原地吸液
    do = DataOperation('dj4_suction.json')
    data5 = do.get_json_data()[1]
    # dj.dj4_suction_inplace(payload=data5)

    # DJ4四联柱塞泵吸液
    do = DataOperation('dj4_suction.json')
    data6 = do.get_json_data()[3]
    # dj.dj4_suction_quadruple_pump(payload=data6)

    # DJ4深度清洗
    do = DataOperation('dj4_cleaning.json')
    data7 = do.get_json_data()[3]
    # dj.dj4_deep_cleaning(payload=data7)

    # DJ4内壁清洗
    # dj.dj4_inner_wall_cleaning()

