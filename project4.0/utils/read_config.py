"""该文件用于获取setting.ini中的配置信息、统一存放文件路径"""
import configparser
import os.path
import os
import datetime

# 获取当前文件的绝对路径


curfile_abs_path = os.path.abspath(__file__)
# print(curfile_abs_path)
# 获取当前项目路径
project_path = os.path.dirname(os.path.dirname(curfile_abs_path))
# print(project_path)
# 通过拼接的方法来获取log目录全路径
log_path = os.path.join(project_path, "log")
# log_path = project_path +os.sep +'log'
# print(log_path)
# 通过拼接的方法来获取report目录路径
report_path = os.path.join(project_path, "report")
# print(report_path)
# 通过拼接的方法来获取config目录全路径
config_path = os.path.join(project_path, "config")
# 获取配置文件路径
setting_path = os.path.join(config_path, "setting.ini")
# 通过拼接的方法来获取jar包路径
data_path = os.path.join(project_path, "data")
jar_path = os.path.join(data_path, "sign.jar")
# 通过拼接的方法获取测试用例路径
excel_path = os.path.join(data_path, "case.xls")
fanhui_parm_list = []


class ReadConfig():
    def __init__(self):
        self.conf_path = setting_path

    def read_conf(self):
        config = configparser.ConfigParser()
        config.read(self.conf_path, "utf-8")
        return config


# 创建实例对象
reconfig = ReadConfig()
# 调用读取配置文件方法
rc = reconfig.read_conf()
# 获取setting.ini中的接口地址域名
url = rc.get("middleground_test_section", "url")
key = rc.get("middleground_test_section", "key")
# 获取配置文件中SMTP邮件服务器地址
host_email = rc.get("send_mail", "host_email")
# 获取setting.ini中的发送邮件登录的邮箱
user_name = rc.get("send_mail", "user_name")
# 获取setting.ini中的邮件接收对象
to_email = rc.get("send_mail", "to_email")
print(to_email)
# 自动生成当前时间戳
timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
