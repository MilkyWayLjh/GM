# PLC调试接口：PLC初始化和版本号 调试相关接口
from GM_Arrayer.utils.requests_plus import *


class PLCInitApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def plc_init(self):
        # PLC初始化连接
        url = self.url + '/device/debug/plc/init'
        return RequestsPlus('get', url).res_obj()

    def plc_read_version_number1(self):
        # 版本号首位
        url = self.url + '/device/debug/plc/readVersionsNumber1'
        return RequestsPlus('get', url).res_obj()

    def plc_read_version_number2(self):
        # 版本号第二位
        url = self.url + '/device/debug/plc/readVersionsNumber2'
        return RequestsPlus('get', url).res_obj()

    def plc_read_version_number3(self):
        # 版本号第三位
        url = self.url + '/device/debug/plc/readVersionsNumber3'
        return RequestsPlus('get', url).res_obj()

    def plc_read_version_number4(self):
        # 版本号第四位
        url = self.url + '/device/debug/plc/readVersionsNumber4'
        return RequestsPlus('get', url).res_obj()

if __name__ == '__main__':
    pass

