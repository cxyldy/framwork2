import configparser
import os.path

conf_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"config","setting.ini")
class ReadConfig():
    def __init__(self):
        self.conf_path = conf_path
    def read_conf(self):
        config = configparser.ConfigParser()
        config.read(self.conf_path,"utf-8")
        return config
reconfig = ReadConfig()
# print(reconfig.read_conf()["request_host"]["hld_url"])



