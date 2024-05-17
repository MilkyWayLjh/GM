# PLC调试接口：状态操作 调试相关接口
from GM_Arrayer.utils.requests_plus import *
from GM_Arrayer.utils.data_operation import DataOperation


class StatusOperationApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8080/api/v1'

    def refrigeration_control1(self, temperature=4):
        """
        制冷1 控制
        @param temperature: 设定温度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actRefrigerationControl1'
        payload = {
            "temperature": temperature
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def read_refrigeration_temp1(self):
        # 读取制冷模块1当前温度
        url = self.url + '/device/debug/plc/readCryogenicTemperature1'
        return RequestsPlus('get', url).res_obj()

    def refrigeration_control2(self, temperature=4):
        """
        制冷2 控制
        @param temperature: 设定温度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actRefrigerationControl2'
        payload = {
            "temperature": temperature
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def read_refrigeration_temp2(self):
        # 读取制冷模块2当前温度
        url = self.url + '/device/debug/plc/readCryogenicTemperature2'
        return RequestsPlus('get', url).res_obj()

    def bleed_pressure(self, lower_limit=150, upper_limit=180):
        """
        气源压力控制
        @param lower_limit: 气源下限 <number>
        @param upper_limit: 气源上限 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actBleedPressure'
        payload = {
            "lowerLimit": lower_limit,
            "upperLimit": upper_limit
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def read_waste_water_sensor(self):
        # 废水传感器
        url = self.url + '/device/debug/plc/readWasteWaterSensor'
        return RequestsPlus('get', url).res_obj()

    def read_pure_water_sensor(self):
        # 纯水传感器
        url = self.url + '/device/debug/plc/readPureWaterSensor'
        return RequestsPlus('get', url).res_obj()

    def auto_fill_water(self, lower_lower_water_refill=4000, lower_water_refill=5000, time_out=10000,
                        upper_refill_limit=15000):
        """
        自动补排水
        @param lower_lower_water_refill: 补水下下限 <integer>
        @param lower_water_refill: 补水下限 <integer>
        @param time_out: 超时时间 <integer>
        @param upper_refill_limit: 补水上限 <integer>
        @return: 
        """
        url = self.url + '/device/debug/plc/actAutomaticWaterRefill'
        payload = {
            "lowerLowerWaterRefill": lower_lower_water_refill,
            "lowerWaterRefill": lower_water_refill,
            "timeOut": time_out,
            "upperRefillLimit": upper_refill_limit
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def liquid_route_empty(self, payload):
        """
        液路排空    前置接口：1、DP充水。2、DP排水。3、DJ充水。4、DJ排水。5、DJ4清洗。6、DJ原地吸液。7、DJ4四联柱塞泵吸液。8、DJ内壁清洗。
                            9、压力罐排水。10、压力罐充水。
        @param payload: 请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actTheLiquidRouteEmpty'
        return RequestsPlus('post', url, json=payload).res_obj()

    def liquid_path_perfusion(self, payload):
        """
        液路灌注    前置接口：1、DP充水。2、DP排水。3、DJ充水。4、DJ排水。5、DJ4清洗。6、DJ原地吸液。7、DJ4四联柱塞泵吸液。8、DJ内壁清洗。
                            9、压力罐排水。10、压力罐充水。11、压力罐排水到下液位之下
        @param payload: 请求体json传参
        @return:
        """
        url = self.url + '/device/debug/plc/actLiquidPathPerfusion'
        return RequestsPlus('post', url, json=payload).res_obj()

if __name__ == '__main__':
    so = StatusOperationApi()
    # 调试
    pprint(so.read_waste_water_sensor())
    pprint(so.read_pure_water_sensor())

