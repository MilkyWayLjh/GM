# 封装requests请求方法，对requests请求方法的二次封装
import requests
from pprint import pprint


class RequestsPlus:
    def __init__(self, method, url, params=None, data=None, json=None, headers=None):
        # 封装请求
        if method.lower() in ["get", "post"]:
            self.res = requests.request(method.lower(), url, params=params, data=data, json=json, headers=headers)
        else:
            self.res = None

    # 返回请求响应对象的上下文操作
    def res_obj(self):
        result = {}
        if self.res is not None:
            try:
                result["res_body"] = self.res.json()  # json格式返回值
            except:
                self.res.encoding = 'utf-8'
                result["res_body"] = self.res.text  # 查看文本格式的响应数据
            result["status_code"] = self.res.status_code  # 状态码
            result["res_time"] = self.res.elapsed.microseconds // 1000  # 响应时间
            result["req_url"] = self.res.request.url  # 请求地址
            result["req_body"] = self.res.request.body  # 请求体
            result["req_headers"] = self.res.request.headers  # 请求头
            result["res_headers"] = self.res.headers  # 响应头
        return result


if __name__ == '__main__':
    # 获取X轴当前位置
    sm = RequestsPlus('get', 'http://10.3.0.100:8080/api/v1/device/debug/plc/readXActualPosition')
    pprint(sm.res_obj())

