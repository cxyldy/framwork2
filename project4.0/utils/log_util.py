import logging
import os.path
import time

from utils.read_config import log_path


class Logger():
    def __init__(self):
        # 定义日志位置和文件名
        self.log_name = os.path.join(log_path,"{}".format(time.strftime("%Y%m%d")))
        # 定义一个日志容器
        self.logger = logging.getLogger()
        # 设置日志输出总开关
        self.logger.setLevel(logging.DEBUG)
        # 创建日志输入格式
        self.formater = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]:%(message)s')
        # 创建日志处理器用来存放日志文件
        self.filelogger = logging.FileHandler(self.log_name,mode='a',encoding='UTF-8')
        # 常见日志处理器，在控制台打印日志
        self.console = logging.StreamHandler()
        # 设置控制台打印日志级别
        self.console.setFormatter(logging.DEBUG)
        # 设置文件打印日志级别
        self.filelogger.setLevel(logging.DEBUG)
        # 控制台打印日志格式
        self.console.setFormatter(self.formater)
        # 文件存放日志格式
        self.filelogger.setFormatter(self.formater)
        # 将日志输出渠道添加到日志受容器中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

logger = Logger().logger
# print(logger)

if __name__ =="__main__":
    logger.debug("我打印debug日志")
    logger.info("我打印info日志")
    logger.warning("我打印warning日志")
    logger.error("我打印error日志")
    logger.error("我打印error日志")


