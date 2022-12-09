import json

import allure
import pytest
import requests

from common import medium_api
from common.medium_api import MediumQueryMethod
from utils.encrypt_method import get_rsa_sign
# from utils.read_config import reconfig
from utils.read_config import url, excel_path, fanhui_parm_list, key, timestamp
from utils.read_excel import get_casedata
from utils.log_util import logger
from utils.write_resopnse import Write_response

@pytest.mark.parametrize("case", get_casedata())
@allure.feature("顶动感")
class TestCase():
    @allure.story("测试模块划分")  # 标注Features功能模块下的分支功能
    @allure.severity('severity')  # 标注测试用例的重要级别
    # @allure.step("测试步骤一")

    def skip_case(self,case):
        if case[10] == 'N':
            pytest.skip()
    def test_common(self, case):
        # 判断excel文件中use_flag为N则跳过用例执行
        self.skip_case(case)
        allure.dynamic.title(case[0])
        title = case[0]
        url = case[1]
        body = eval(case[2])
        headers = eval(case[3])
        method=case[4]
        method_type=case[5]
        # 读取配置文件模块可自动生成当前时间戳，替换文件body中的时间戳
        body['timestamp']=f"{timestamp}"
        # body = body.replace('\r', '').replace('\n', '').replace('\t', '').replace('null','None') if body is not None else ""
        # 调用加密方法获取加密密钥
        get_sign = get_rsa_sign(body,key)
        # 将生成的签名放到请求头的sian字段中
        headers['sign']=f"{get_sign}"

        # openapi签名 将获取的加密密钥更新至body中的hmac中
        # body["hmac"] = get_hmac
        logger.info("开始逐个发起请求")
        # 调用中间request方法发起请求
        res = medium_api.MediumQueryMethod().request(url, method,method_type, body,headers)
        # 响应结果
        result = res.json()
        logger.info("请求结果：{}".format(result))
        # 将接口返回结果逐个添加到接口请求结果列表中
        fanhui_parm_list.append(result)# 把返回结果添加到列表


