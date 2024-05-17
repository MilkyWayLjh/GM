# PLC调试接口：热封流程中的单个动作 调试相关接口
from GM_Arrayer.utils.requests_plus import *


class HeatSealFlowApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8080/api/v1'

    def diaphragm_platen_out(self):
        """
        压膜板推出
        @return:
        """
        url = self.url + '/device/debug/plc/actDiaphragmPlatenOut'
        return RequestsPlus('get', url).res_obj()

    def diaphragm_platen_return(self):
        """
        压膜板收回
        @return:
        """
        url = self.url + '/device/debug/plc/actDiaphragmPlatenReturn'
        return RequestsPlus('get', url).res_obj()

    def heat_seal_z_axis_move(self, position=45, speed=60):
        """
        热封Z轴运动
        @param position: 位置 <number>
        @param speed: 速度 <number>
        @return:
        """
        url = self.url + '/device/debug/plc/actHeatSealZAxisMove'
        payload = {
            "position": position,
            "speed": speed
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def heat_seal_z_read_pos(self):
        """
        热封Z轴当前位置
        @return:
        """
        url = self.url + '/device/debug/plc/readHeadSealZPos'
        return RequestsPlus('get', url).res_obj()

    def heat_seal_z_home(self):
        """
        热封Z轴回原
        @return:
        """
        url = self.url + '/device/debug/plc/actHeatSealZAxisHome'
        return RequestsPlus('get', url).res_obj()

    def tran_section_out(self):
        """
        热封横切出刀
        @return:
        """
        url = self.url + '/device/debug/plc/actTranSectionOut'
        return RequestsPlus('get', url).res_obj()

    def tran_section_return(self):
        """
        热封横切收刀
        @return:
        """
        url = self.url + '/device/debug/plc/actTranSectionReturn'
        return RequestsPlus('get', url).res_obj()

    def vertical_cutting_out(self):
        """
        热封竖切出刀
        @return:
        """
        url = self.url + '/device/debug/plc/actVerticalCuttingOut'
        return RequestsPlus('get', url).res_obj()

    def vertical_cutting_return(self):
        """
        热封竖切收刀
        @return:
        """
        url = self.url + '/device/debug/plc/actVerticalCuttingReturn'
        return RequestsPlus('get', url).res_obj()

    def heat_seal_pre_cut_film(self, first_count=3, second_count=16, third_count=5):
        """
        热封卷膜预切
        @param first_count: 第一段计数 <integer>
        @param second_count: 第二段计数 <integer>
        @param third_count: 第三段计数 <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actHeatSealCutFilm'
        payload = {
            "firstCount": first_count,
            "secondCount": second_count,
            "thirdCount": third_count
        }
        return RequestsPlus('post', url, json=payload).res_obj()

    def heat_seal_flow(self, position=45, speed=60, time=1200):
        """
        热封动作流程
        @param position: 位置 <number>
        @param speed: 速度 <number>
        @param time: 时间ms <integer>
        @return:
        """
        url = self.url + '/device/debug/plc/actHeatSeal'
        payload = {
            "position": position,
            "speed": speed,
            "time": time
        }
        return RequestsPlus('post', url, json=payload).res_obj()

if __name__ == '__main__':
    hs = HeatSealFlowApi()
    # 调试
    pprint(hs.heat_seal_z_read_pos())

