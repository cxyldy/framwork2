import json
import time

from utils.encrypt_method import get_rsa_sign
from utils.read_config import timestamp


class RequestEnrypt:

    def request_encrypt_method(self, body, headers):
        if (body):
            # 读取配置文件模块可自动生成当前时间戳，替换文件body中的时间戳
            body = eval(body)
            body['timestamp'] = f"{timestamp}"
            signvalue = get_rsa_sign(body)
            encrypt_headers = eval(headers)
            encrypt_headers["sign"] = signvalue
            return body,encrypt_headers
