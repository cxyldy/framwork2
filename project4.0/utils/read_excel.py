import os
import xlrd
# project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# print(case_path)
from utils.log_util import logger
from utils.read_config import excel_path


def get_casedata():
    # 定义一个空列表，用于后续存放所有的测试用例
    case_list = []
    try:
        book = xlrd.open_workbook(excel_path)
    except Exception as e:
        # 将错误信息写入日志
        logger.info("文件不存在!"+str(e))
        return e
    else:
        logger.info('打开测试用例文件成功！')
    # try语句无异常时，通过下标方法读取sheet值
        sheet = book.sheet_by_index(0) #获取sheet页第一个
        try:
    # 获取列表的总数
            for row in range(1, sheet.nrows):
                row_value = sheet.row_values(row)
                case_list.append(row_value)
        except Exception as e:
            logger.info('excel格式不对'+str(e))
            return e
        else:
            logger.info('读取测试用例完毕')
            return case_list

if __name__ =="__main__":
    case = get_casedata()
    print(case)
