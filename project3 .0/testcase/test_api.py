import json

import allure
import pytest
import requests

from common import medium_api
from common.medium_api import MediumQueryMethod
from utils.encrypt_method import get_rsa_sign
# from utils.read_config import reconfig
from utils.read_config import host_url
from utils.read_excel import get_casedata
from utils.log_util import logger

@pytest.mark.parametrize("case", get_casedata())
@allure.feature("开放API测试")
class TestCase():
    @allure.story("分账模块")  # 标注Features功能模块下的分支功能
    @allure.severity('此处均先标识同样等级')  # 标注测试用例的重要级别
    # @allure.step("测试步骤一")

    def skip_case(self,case):
        if case[12] == 'N':
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
        jsonpaths=case[6]
        dependency=case[7]
        key = case[10]
        # 调用加密方法获取加密密钥
        get_hmac = get_rsa_sign(body, key)
        # 将获取的加密密钥更新至body中的hmac中
        body["hmac"] = get_hmac
        # print(key)
        logger.info("用例数据拆包开始。。。。")
        # 调用中间request方法发起请求
        res = medium_api.MediumQueryMethod().request(url, method,method_type, body,headers)
        # 响应结果
        result = res.json()
        logger.info("请求结果：{}".format(result))
