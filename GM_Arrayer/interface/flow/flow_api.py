# 方案流程相关接口
from GM_Arrayer.utils.requests_plus import *
from GM_Arrayer.utils.data_operation import DataOperation


class FlowApi:
    def __init__(self):
        self.url = 'http://10.3.0.100:8081/api/v1'

    def list_set(self, payload):
        """
        设置方案列表下发
        @param payload: 方案列表
        @return:
        """
        url = self.url + '/flow/list/set'
        return RequestsPlus('post', url, json=payload).res_obj()

    def list_start(self):
        """
        开始list运行
        @return:
        """
        url = self.url + '/flow/list/start'
        return RequestsPlus('get', url).res_obj()

    def list_pause(self):
        """
        暂停list运行
        @return:
        """
        url = self.url + '/flow/list/pause'
        return RequestsPlus('get', url).res_obj()

    def list_resume(self):
        """
        继续list运行
        @return:
        """
        url = self.url + '/flow/list/resume'
        return RequestsPlus('get', url).res_obj()

    def list_stop(self):
        """
        停止list运行
        @return:
        """
        url = self.url + '/flow/list/stop'
        return RequestsPlus('get', url).res_obj()

    def run_group_skip(self, group_id):
        """
        跳过方案组
        @param group_id: 跳过方案组的ID
        @return:
        """
        url = self.url + '/flow/runGroup/skip'
        payload = {
            'runGroupId': group_id
        }
        return RequestsPlus('get', url, params=payload).res_obj()

    def run_pause(self):
        """
        暂停run运行
        @return:
        """
        url = self.url + '/flow/run/pause'
        return RequestsPlus('get', url).res_obj()

    def run_resume(self):
        """
        继续run运行
        @return:
        """
        url = self.url + '/flow/run/resume'
        return RequestsPlus('get', url).res_obj()

    def run_stop(self):
        """
        停止run运行
        @return:
        """
        url = self.url + '/flow/run/stop'
        return RequestsPlus('get', url).res_obj()

if __name__ == '__main__':
    flow = FlowApi()
    # 调试
    do = DataOperation('set_list.json')
    data = do.get_json_data()[0]
    # pprint(flow.list_set(payload=data))
    # pprint(flow.list_start())
    pprint(flow.list_stop())

