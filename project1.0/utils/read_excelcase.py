import os

import xlrd
project_path
project_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
case_path = os.path.join(project_path, r'data\case.xls')


# print(case_path)
def get_casedata():


    book = xlrd.open_workbook(case_path)

    # 获取工作簿中所有sheet的名称
    # 通过name值进行读取sheet
    # sheet_names = book.sheet_names()
    # print(sheet_names)
    # sheet = book.sheet_by_name('xdvxc')
    # 获取Book对象中所有Sheet对象
    # sheet_objects = book.sheets()
    # print(sheet_objects)
    # print(sheet_objects[0])
    # 遍历所有的工作表，打印出行数、列数
    # for sheet in sheet_objects:
    #     sheet_rows = sheet.nrows
    #     sheet_ncols = sheet.ncols
    #     print(sheet_rows,sheet_ncols)
    # 判断Book对象中某个sheet是否导入
    # print(book.sheet_loaded(0),book.sheet_loaded('国通'))

    # 通过下标方法读取sheet值
    sheet = book.sheet_by_index(0) if book.sheet_loaded('国通') else False
    # 获取列表的总数
    nrows = sheet.nrows
    case_list = []
    for row in range(1, nrows):
        # if sheet.cell_value(row,0) !='title':
        row_value = sheet.row_values(row)
        case_list.append(row_value)
    return case_list

    # ncols = sheet.ncols
    # print(nrows,ncols)
    #
    # print(sheet.row_values(0),sheet.row_len(0))
    # print(sheet.row_slice(0,1,2))
    # print(sheet.row_types(0),sheet.cell_type(0,0))

    # print(sheet.col_values(0))
print(get_casedata())
