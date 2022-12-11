import json
import operator

import allure
import pytest
import requests
from allure_commons.types import LinkType

from common import medium_api
from common.medium_api import MediumQueryMethod
from common.request_encrypt import RequestEnrypt
from utils.encrypt_method import get_rsa_sign
# from utils.read_config import reconfig
from utils.read_config import url, excel_path, fanhui_parm_list
from utils.read_excel import get_casedata
from utils.log_util import logger
from utils.write_resopnse import Write_response
# from requests.packages.urllib3.exceptions import InsecureRequestWarning

# @allure.parent_suite('慧徕店')
# @allure.suite('3196_Sim卡管理需求')
# @allure.sub_suite('接口测试用例')    不常用
@allure.epic("慧徕店")  # 敏捷里面的概念，定义史诗，相当于module级的标签
@allure.feature("3196_Sim卡管理需求")  # 功能点的描述，可以理解成模块，相当于class级的标签
@allure.story("接口测试用例")  # 故事，可以理解为场景，相当于method级的标签
class TestCase():

    # 判断文件中的用例标识，若为N，则跳过
    def skip_case(self, case):
        if case[10] == 'N':
            pytest.skip()

    @allure.link('https://www.baidu.com/', LinkType.LINK, '其他link地址')
    @allure.label('标签呀呀呀')
    @allure.issue('https://www.baidu.com/', '禅道bug链接')  # 记录用例的问题(超链接)
    @allure.testcase('https://www.baidu.com/', '禅道测试用例链接')
    @pytest.mark.parametrize("case", get_casedata())
    def test_common(self, case):
        # 调用跳过测试用力的实例方法
        self.skip_case(case)
        # 动态获取用例中用例的优先级
        allure.dynamic.severity(f'{case[11]}')
        # 动态获取用例标题
        allure.dynamic.title(f'{case[0]}')
        # 将用例标题赋值给title
        title = case[0]
        url = case[1]
        body = case[2]
        headers = case[3]
        method = case[4]
        method_type = case[5]
        jsonpaths = case[6]
        dependency=case[7]

        # 使用条件表达式替换掉url回车、换行、制表符等信息
        url=url.replace('\r', '').replace('\n', '').replace('\t', '') if url is not None else url
        # 使用条件表达式替换掉body中的回车、换行、制表符等信息
        body = body.replace('\r', '').replace('\n', '').replace('\t', '').replace('null','None') if body is not None else body
        # 使用条件表达式替换掉jsonpath中的回车、换行、制表符等信息
        jsonpaths = jsonpaths.replace('\r', '').replace('\n', '').replace('\t', '').replace('null','None') if jsonpaths is not None else jsonpaths

        """
        logger.info("*********开始查找替换依赖变量*********")
        # 假如body\header中存在变量依赖符号$，调用convertBody重新对变量进行转化
        body = operatorConvert().convertBody(body) if operator.contains(body, "$")  else body
        headers = operatorConvert().convertBody(headers) if (headers is not None and operator.contains(headers, "$")) else headers
        header = "" if header is None else header
        logger.info("*********开始查找替换需要生成的随机变量*********")
        # 假如body中存在随机变量符号@RANDOM，调用convertBody_random重新对变量进行转化
        body = operatorConvert().convertBody_random(body) if  operator.contains(body, "@RANDOM") else body
"""

        #实时生成body时间戳，生成加密签名,替换到headers中
        body,encrypt_headers = RequestEnrypt().request_encrypt_method(body,headers)
        logger.info("**********发起请求************")
        # 调用中间request方法发起请求
        # requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        res = medium_api.MediumQueryMethod().request(url, method, method_type, body, encrypt_headers,verify=False)
        # 响应结果
        result = res.json()
        logger.info("请求结果：{}".format(result))
        # 将接口返回结果逐个添加到接口请求结果列表中
        fanhui_parm_list.append(result)  # 把返回结果添加到列表
