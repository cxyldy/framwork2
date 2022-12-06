
import os
import time

import pytest
import schedule

from utils.compress_report import zipDir
from utils.send_mail import do_job

if __name__ == '__main__':

    # allure测试报告
    pytest.main(["--clean-alluredir",".\\testcase\\test_api.py","--alluredir",".\\report\\xml"])# 运行指定文件        删除历史记录
    # pytest.main(["-s","-p","no:faulthandler","./framework","--clean-alluredir","--alluredir","./report/xml"])# 运行目录下所有（test_*.py  和 *_test.py）
    # 生成静态报告数据
    # os.system("allure generate --clean ./report/xml/ -o ./result/html/")
    # 生成动态报告，并自动打开
    os.system("allure serve .\\report\\xml")
    # time.sleep(1)
    # # 生成bat文件，用于打开测试报告
    # with open(r'C:\Users\24113\ldproject\project3 .0\result\点击打开测试报告.bat', 'w') as f:
    #     f.write("""@echo off
    # echo open testreport
    # allure open .\html
    # pause
    #     """)
    # time.sleep(1)
    # 压缩文件
    # zipDir(r"C:\Users\24113\ldproject\project3 .0\result", r"C:\Users\24113\ldproject\project3 .0\result.zip")
    # time.sleep(2)
    # schedule.every().day.at("08:50").do(do_job)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    # --clean


