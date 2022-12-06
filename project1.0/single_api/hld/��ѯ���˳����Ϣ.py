import datetime

import jpype
import os
import requests
import json

def get_rsa_sign(content):
    """
    调用java jar包，对入参进行rsa签名
    :param sign_raw:待签名字符串
    :return:signature:签名后的加密字符串
    """
    key = 'a3a283c0ac65419e9120fbc1da4805e4'
    jarpath = os.path.join(os.path.abspath('.'), "signaf.jar")  # os.path.abspath这个函数用来获取当前 python 脚本所在的绝对路径

    # 启动JVM
    jvmPath = jpype.getDefaultJVMPath()
    # 判断JVM是否启动
    if not jpype.isJVMStarted():
        # 加载jar包
        jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % jarpath)
    # 指定main class
    JDClass = jpype.JClass("hld.common.tools.HztSignUtils")
    # 创建类实例对象
    jd = JDClass()
    # 引用jar包类中的方法 rsa_sign
    signature = jd.hztSign(json.dumps(content),key)
    return str(signature)
    # 关闭JVM
    jpype.shutdownJVM()


# 调用接口
url = "https://hldopenapi-testapp.3vast.cn/openapi-mms/split/querySplitSndMrch"
# 请求参数
content = {
    "randomData":"1234567890asd",
    "timestamp":"20211223201746",
    "characterSet":"UTF-8",
    "signType":"PUB_SIGN",
    "version":"1.0.0",
    "hmac":"z/sT9FLq4l6VGmjw924C/wH+LaO+8L94zOCIVP1Wcl7tQi8t1FUmlvwqraiC7Cu6Wiah9TYU/GY09hx1m52lzkBmvToIiPsg/Mwc/KtfQuU4rBNHmi2y4QQDNf2J6g6hcaeA7PSGWCRFnMlkh/kbYGD0N+uVKBfx69LD4+jV2rk=",
    "reqData":{
        "platformCode":"909335010749869",
        "platformType":"1",
        "paymentMerchantCode":"909335010749402"
    }
}
# 服务商商圈1dD@
# 调用加密包传入请求参数获取签名
sign = get_rsa_sign(content)
print(f'调用jar包生成的签名为{sign}')
# print(type(content))
# 将hmac值修改为使用jar包生成的签名
content['hmac'] = sign
# print(type(content),content)
# print(json.dumps(str(content)))
print(content)
r = requests.post(url=url,data =json.dumps(content,ensure_ascii=False,separators=(",",":")).encode('UTF-8'),headers={"Content-Type": "application/json"})
# r = requests.post(url=url,json =content,headers={"Content-Type": "application/json"})

# r = requests.post(url=url, data=str(content).encode('utf-8'), headers={"Content-Type": "application/json"})
print(r.json())
