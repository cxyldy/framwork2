import json
import os

import jpype
import requests

from utils.read_config import jar_path, key


def get_rsa_sign(content):
    """
    调用java jar包，对入参进行rsa签名
    :param sign_raw:待签名字符串
    :return:signature:签名后的加密字符串
    """
    # 启动JVM
    jvmPath = jpype.getDefaultJVMPath()
    # 判断JVM是否启动
    if not jpype.isJVMStarted():
        # 加载jar包
        # jarpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "signaf.jar")
        jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" %jar_path)
    # 指定main class
    # JDClass = jpype.JClass("hld.common.tools.HztSignUtils")     open
    JDClass = jpype.JClass("Sign")

    # 创建类实例对象
    jd = JDClass()
    # 引用jar包类中的方法 rsa_sign
    signature = jd.hztSign(json.dumps(content),key)
    return str(signature)
    # 关闭JVM
    jpype.shutdownJVM()

