

import json

import requests

from utils.log_util import logger
from utils.read_config import url


class CoreMethod:
    def __init__(self):
        self.api_root_url = url

    def get(self, url, **kwargs):
        # return requests.get(self.api_root_url + url, **kwargs)
        return self.request(url, "get", **kwargs)

    def post(self, url, **kwargs):
        # return requests.post(self.api_root_url + url, **kwargs)
        return self.request(url, "post", **kwargs)


    def request(self, url, method, **kwargs):
        self.request_log(url, method, **kwargs)
        if method == "get":
            return requests.get(self.api_root_url + url, **kwargs)
        if method == "post":
            return requests.post(self.api_root_url + url, **kwargs)

    def request_log(self, url, method, **kwargs):
        data = dict(**kwargs).get('data')
        json_data = dict(**kwargs).get('json')
        params = dict(**kwargs).get('params')
        headers = dict(**kwargs).get('headers')

        logger.info(f"接口请求地址>>>{self.api_root_url + url}")
        logger.info(f"接口请求方法{method}")
        if data is not None:
            logger.info(f"接口请求data参数\n{json.dumps(data,ensure_ascii=False,indent=2)}")
            #  json.dumps 默认使用编码是ASCII，不包含中文，出现了乱码，加ensure_ascii=False，不会使用默认的ASCII编码，这样会正常显示中文
        if json is not None:
            logger.info(f"接口请求参数\n{json.dumps(json_data,ensure_ascii=False,indent=2)}")
        if params is not None:
            logger.info(f"接口请求参数\n{json.dumps(params,ensure_ascii=False,indent=2)}")
        if headers is not None:
            logger.info(f"接口请求头\n{json.dumps(headers,ensure_ascii=False,indent=2)}")
