import json

import requests

from common import core_apiquery
from common.core_apiquery import CoreMethod
from utils.log_util import logger


class MediumQueryMethod():
    def request(self, requestUrl, method, method_type, requestData, headers, **kwargs):
        logger.info("执行统一请求方法开始。。。。。。。。。。。。。")
        # 判断requestMethod是否是post
        if method.lower() == "post":
            # paramsType是form表单提交
            if method_type == "form":
                # requestData=eval(requestData)
                # headers = eval(headers)
                # response=requests.post(url=requestUrl, data=requestData, headers=headers)
                response = core_apiquery.CoreMethod().post(url=requestUrl, data=requestData, headers=headers
                                                           )
                return response
            # json提交
            elif method_type == 'json':
                requestData = requestData
                # requestData =json.loads(requestData)  #将字符串转为字典时，存在null值会报错，使用json.loads()函数：将json格式数据转换为字典，存在null时，转为None
                # requestData = json.dumps(requestData)
                # headers = eval(headers)
                # headers = json.dumps(headers)
                response = core_apiquery.CoreMethod().post(url=requestUrl, json=requestData, headers=headers)
                return response

        # 判断requestMethod是否是get
        elif method == "get":
            if method_type == "url":

                request_url = "%s%s" % (requestUrl, "" if requestData is None else requestData)
                headers = eval(headers) if headers != '' else headers
                response = core_apiquery.CoreMethod().get(url=request_url, headers=headers)

                print(response)
                return response
            elif method_type == "params":
                response = core_apiquery.CoreMethod().get(url=requestUrl, params=requestData, headers=headers)
                return response
