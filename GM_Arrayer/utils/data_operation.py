import pandas
import os
import json
from pprint import pprint


class DataOperation:
    """
    读取.csv,xls,xlsx文件
    优化读取json文件
    """
    def __init__(self, file_name):
        # 获取路径
        common_path = os.path.dirname(__file__)
        project_path = os.path.dirname(common_path)
        # 拼接路径
        full_path: str = os.path.join(project_path, 'data', file_name)     # : str 声明为字符串类型
        self.path = full_path

        # 判断文件的类型是否是.csv格式
        if full_path.endswith('.csv'):
            self.data = pandas.read_csv(full_path)
        # 判断文件的类型是否是.xls格式
        elif full_path.endswith('.xls'):
            self.data = pandas.read_excel(full_path)
        # 判断文件的类型是否是.xlsx格式
        elif full_path.endswith('.xlsx'):
            self.data = pandas.read_excel(full_path)
        # 判断文件的类型是否是.json格式
        elif full_path.endswith('.json'):
            self.data = pandas.read_json(full_path)
        else:
            print('其它类型的文本暂时不读取')

    def get_data_to_list(self):
        """将文本的内容转为一个列表"""
        return self.data.values.tolist()

    def get_data_to_dict(self):
        """将文本数据转为字典"""
        return [self.data.loc[i].to_dict() for i in self.data.index.values]

    def get_json_data(self):
        """
        打开并读取json文件，将文件内容转换成python对象
        :return: json对象
        """
        # 打开json文件
        with open(self.path, 'r', encoding='utf-8') as f:
            # 读取json文件，取出数据
            json_data = json.load(f)
        return json_data


if __name__ == '__main__':
    do = DataOperation("dp_parameter.json")
    pprint(do.data)
    pprint(do.path)
    pprint(do.get_json_data())
    data = do.get_json_data()[1]
    pprint(data)
