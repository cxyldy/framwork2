import json
import os
import time

import pytest
import schedule

from utils.compress_report import zipDir
from utils.read_config import excel_path, fanhui_parm_list
from utils.send_mail import do_job
from utils.wr_rwsponse import write_res
from utils.write_resopnse import Write_response

if __name__ == '__main__':

    # allure测试报告
    pytest.main(["--clean-alluredir",".\\testcase\\test_api.py","--alluredir",".\\report\\xml"])# 运行指定文件        删除历史记录
    # pytest.main(["-s","-p","no:faulthandler","./framework","--clean-alluredir","--alluredir","./report/xml"])# 运行目录下所有（test_*.py  和 *_test.py）
    # 生成静态报告数据
    # os.system("allure generate --clean ./report/xml/ -o ./result/html/")
    # 生成动态报告，并自动打开
    os.system("allure serve .\\report\\xml")

    # time.sleep(1)
    # 压缩文件
    # zipDir(r"C:\Users\24113\ldproject\project3 .0\result", r"C:\Users\24113\ldproject\project3 .0\result.zip")
    # time.sleep(2)
    # schedule.every().day.at("08:50").do(do_job)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    # --clean
    print(fanhui_parm_list)
    write_res(fanhui_parm_list)
    # for i in fanhui_parm_list:
    #     print(i,type(json.dumps(i)))