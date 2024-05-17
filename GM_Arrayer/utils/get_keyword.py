# 获取接口返回值中某个字段的值
import jsonpath


class GetKeyword:
    @staticmethod
    def get_keyword(source_data, keyword):
        """
        通过关键字获取对应的值，如果有多个值，默认取第一个，如果没有返回None
        :param source_data: 源数据
        :param keyword: 关键字key
        :return: 关键字对应的第一个值/None
        """
        try:
            return jsonpath.jsonpath(source_data, f"$..{keyword}")[0]
        except Exception as e:
            # print(f"{e}, {source_data}中，关键字{keyword}不存在")
            print(f"{e}：返回的数据源中，关键字{keyword}不存在")
            return None

    @staticmethod
    def get_keywords(source_data, keyword):
        """
        通过关键字获取对应所有值，如果不存在返回None(False)
        :param source_data: 源数据
        :param keyword: 关键字
        :return: list/None(False)
        """
        try:
            return jsonpath.jsonpath(source_data, f"$..{keyword}")
        except Exception as e:
            # print(f"{e}, {source_data}中，关键字{keyword}不存在")
            print(f"{e}：返回的数据源中，关键字{keyword}不存在")
            return None

if __name__ == '__main__':
    test_data = {
        'status_code': 200,
        'headers': {
            'Vary': 'Origin, Access-Control-RequestMethod, Access-Control-Request-Headers',
            'X-Content-Type-Options': 'nosniff',
            'X-XSSProtection': '1; mode=block',
            'Cache-Control': 'no-cache, no-store, maxage=0, must-revalidate',
            'Pragma': 'no-cache',
            'Expires': '0',
            'X-Frame-Options': 'DENY',
            'Content-Type': 'application/json',
            'Transfer-Encoding': 'chunked',
            'Date': 'Fri, 10 Jun 2022 03:31:58 GMT',
            'Keep-Alive': 'timeout=60',
            'Connection': 'keep-alive'
        },
        'body': {
            'code': 200,
            'message': '操作成功',
            'data': {
                'tokenHead': 'Bearer ',
                'code': 201,
                'token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImNyZWF0ZWQiOjE2NTQ4MzE5MTgxNzgsImV4cCI6MTY1NTQzNjcxOH0.J5a0VrwfYJuV3ec5biygHF06U9lH0RtPyFMs8VFbuEGWVVFvyRKM8nI39Sv8Pc9A9XHkoJ5TYVxSuagVLj3rQ '
            }
        },
        'response_time': 138
    }
    print(GetKeyword.get_keyword(test_data, "code"))
    print(GetKeyword.get_keywords(test_data, "code"))
    print(GetKeyword.get_keyword(test_data, "body"))
    print(GetKeyword.get_keywords(test_data, "body"))

    print(GetKeyword.get_keyword(test_data, "cod"))
    print(GetKeyword.get_keywords(test_data, "cod"))

