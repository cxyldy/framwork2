import json

import allure
import pytest
import requests

from utils.encrypt_method import get_rsa_sign
from utils.read_config import reconfig
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
    def test_hld(self, case):
        # 判断excel文件中use_flag为N则跳过用例执行
        self.skip_case(case)
        allure.dynamic.title(case[0])
        title = case[0]
        url_host =  reconfig.read_conf()["request_host"]["hld_url"]
        url = url_host +case[1]
        body = eval(case[2])
        heasers = case[3]
        key = case[10]
        # 调用加密方法获取加密密钥
        get_hmac = get_rsa_sign(body, key)
        # 将获取的加密密钥更新至body中的hmac中
        body["hmac"] = get_hmac
        # print(key)
        try:
            r = requests.request(url=url, json=body, method='post')
        except Exception as e:
            logger.debug(f'请求接口出错，失败原因为{e}')
        # 暂且先断言响应状态码
        assert r.status_code == 200
        logger.info(f'测试场景为：{title}，\n请求的url为：{r.request.url}，\n请求体为{r.request.body.decode("unicode_escape")},\n请求头为：{r.request.headers}\n接口响应报文为：{r.json()}')
        # allure.dynamic.description(
        #     f'测试场景为：{title}，\n请求的url为：{r.request.url}，\n请求体为{r.request.body.decode("utf-8")},\n请求头为：{r.request.headers}\n接口响应报文为：{r.json()}')

        # r = requests.request(url = url,data = json.dumps(body,ensure_ascii=False,separators=(',',':')).encode("UTF-8"),method='post',headers=heasers)
        # with allure.step("打印接口请求信息"):
        #     print(f'测试场景为：{title}，\n请求的url为：{r.request.url}，\n请求体为{r.request.body.decode("utf-8")},\n请求头为：{r.request.headers}')
        #     # print('数据库和会计师康师傅')
        # with allure.step("打印接口响应报文"):
        #     print(f'接口响应报文为：{r.json()}')

        # print(type(eval(body)),json.dumps(eval(body),ensure_ascii=False,separators=(',',":")))
