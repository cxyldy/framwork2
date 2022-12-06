import json
import os.path
import time

import xlrd

from utils.log_util import logger
from utils.read_config import excel_path, data_path
from xlutils.copy import copy


def check_res(res,check_data):
    # 对接口返回的结果进行处理
    new_res = res.replace(' ','').replace('":"','='.replace('":','='))
    for check in check_data.split(";"):
        if  check in new_res:
            pass
        else:
            logger.debug('测试不通过，预期结果是{},实际结果是{}'.format(check_data,res))
            return '失败'
    return '通过'

def write_res(res_list):
    book = xlrd.open_workbook(excel_path)
    new_book = copy(book)
    sheet = new_book.get_sheet(0)
    count = 1
    for res in res_list:
        sheet.write(count,9,json.dumps(res,ensure_ascii=False))
        count +=1
    new_filename = time.strftime("%Y%m%d%H%M%S"+'test_case.xls')
    new_book.save(os.path.join(data_path,new_filename))
