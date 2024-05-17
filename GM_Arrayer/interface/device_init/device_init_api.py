# 设备初始化接口
from GM_Arrayer.utils.requests_plus import *


class DeviceInitApi:
    def __init__(self):
        self.url = "http://10.3.0.100:8080/api/v1"

    def device_init(self):
        # 设备初始化
        url = self.url + "/device/prod/init"
        return RequestsPlus('get', url).res_obj()

    def device_version(self):
        # 设备版本号
        url = self.url + "/device/prod/version"
        return RequestsPlus('get', url).res_obj()

if __name__ == '__main__':
    di = DeviceInitApi()
    # 调试
    # pprint(di.device_init())
    pprint(di.device_version())

