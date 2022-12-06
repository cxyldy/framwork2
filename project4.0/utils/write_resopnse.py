# 复制原表，把返回的参数写入复制好的Excel表格

import copy
from datetime import datetime

import xlrd

from utils.read_config import excel_path

class Write_response():
    def write_excel(self,excel_path,write_hang_no,fanhui_parm_list):

        # 使用xlrd打开Excel
        excel_open_file = xlrd.open_workbook(excel_path)

        # 复制Excel并保留原格式
        self.ex_open_file_cp = copy.copy(excel_open_file)

        # 定位到表格
        cp_sheet = self.ex_open_file_cp.sheet_by_index(0) if self.ex_open_file_cp.sheet_loaded('国通') else False
        # 使用循环把返回结果写入Excel表格
        write_hang_no =0
        for i in fanhui_parm_list:
            if len(i) > 32767:
                cp_sheet.write(write_hang_no,3,'字符串长度超出32767会报错')
                cp_sheet.write()
                continue
            cp_sheet.write(write_hang_no, 9, str(i))# 把对应的结果写入Excel
            cp_sheet.write(write_hang_no,14,str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))# 在第四列对应的行写入当前时间,写入Excel需要转成字符串否则时间会变成一串数字（时间戳）
            write_hang_no += 1
        print('写入成功！！')

    # 保存Excel方法
    def baocun_excel(self,baocun_filename):
        # 保存新的表格名字为test_tuihuo_api
        self.ex_open_file_cp.save(baocun_filename)
        print('保存新表格 %s 成功'%baocun_filename)