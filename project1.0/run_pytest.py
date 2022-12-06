
import os

import pytest


if __name__ == '__main__':

    # allure测试报告
    pytest.main(["--clean-alluredir",".\\testcase\\test_api.py","--alluredir",".\\report\\xml"])# 运行指定文件        删除历史记录
    # pytest.main(["-s","-p","no:faulthandler","./framework","--clean-alluredir","--alluredir","./report/xml"])# 运行目录下所有（test_*.py  和 *_test.py）
    # 生成静态报告数据
    # os.system("allure generate --clean ./report/xml/ -o ./result/html/")
    # 生成动态报告，并自动打开
    os.system("allure serve .\\report\\xml")
    # --clean


