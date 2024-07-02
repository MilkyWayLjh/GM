# 机械臂调试：机械臂初始化和Z轴抬升
from GM_Arrayer.utils.requests_plus import *


class DebugArm:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def lift_z_axis(self):
        """
        在机械臂运行到过低位置时,进行Z轴抬升（默认每次抬升20）
        @return:
        """
        url = self.url + '/device/debug/arm/liftZAxis'
        return RequestsPlus('get', url).res_obj()

    def arm_init(self):
        """
        对机械臂进行初始化
        @return:
        """
        url = self.url + '/device/debug/arm/init'
        return RequestsPlus('get', url).res_obj()

if __name__ == '__main__':
    da = DebugArm()
    # 调试
    pprint(da.arm_init())
