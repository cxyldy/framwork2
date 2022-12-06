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
    key='MIICdwIBADANBgkqhkiG9w0BAQEFAASCAmEwggJdAgEAAoGBAIt1Ta/sDj7uo+QEoA8Ovj7bm4Drydy9GgPhjFz0N2eSTX4GanHUYz5kguCsVRc2yq5nESPpNPeIAbByNEK+u1MN4CJCJ8AHsFD8aax3rhZS0smWsxWhkxSMm6+9sxmnTMFwneFxlmaXyUzhK6DHyk5o4z62yu1B8ExAJjpR36fJAgMBAAECgYB50mmfsKQtI0e1arjrDmTwAeSQNOjsU6BDHacAmDFB31KkMTSQ5Qggu6p8Wu4lzi41NUGKzi//vyZCnTC70WNOdAemeeHSMSGwuRPWac9iHPqYNq/63Zr3VDzKcAqU9Bqfk2Bb9sJ4b6C7YsJhL3OovC0gKlKDpr699g/dAHEzEQJBAOejX54Zpi/uHGe+zPuK7uH/P8lZcgLeT35xQt2e7cMZIezMocMQH6fzC71ZDnc3hOsoVcOg501OS0hJa0gSCB0CQQCaIBOcpOdt3EjzSTfLIpq5TgobcWUQE+aedA2dlamsMOxzTb+Fv+qWRcq2wAKBfWzKCAAceZ++s9Mly+s7IAadAkEArvEcTfNhJ+HVYiUf+vo64EQ+kHsVOEVeFEjGD0rwluBsVsNViFStE9LjkuWnnzI3GMMlwtHK3v+6q6WHeK7loQJAMaxY5cl4FT5D/LUCWGPkvgha1ZFsYwwm7ba1lK5hqu9xpY/PREogTyJbPR8RL66+2zZM4uCIDaxjRvE79ShTOQJBAMo5CFw25ztjm0PtjaGlyhbA1JyPIM6TZgXRSGO8VPxVQQ641t8IDTC33Ev+UUSsW5OevVG20PZx2J3FNgtXlXk='
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
url = "https://hldopenapi-app-uat.3vast.net/openapi-mms/split/querySplitMhtStatus"
# 请求参数
content = {
    "randomData": "1234567890",
    "timestamp": "20211223201746",
    "characterSet": "UTF-8",
    "signType": "PUB_SIGN",
    "version": "1.0.0",
    "appId": "A00003019",
    "hmac": "yUgEkHj5f4BmByUtpIWH5Fy3MeTOyVRpd1vZuaYTqZ1BapPb/HbWS8W+dvOSfZ6OYP2XTZjzi+r3OOl+AGX2Yen0JF1YNkJ/DbJcvhSAv1SArELSE2Ny+TkQpdNheJcojvmZFhRolhxCGsdGYYKgk8vaGhl//Sx3u92qxlxQOrc=",
    "reqData": {
        "platformType": "0",
        "platformCode": "A00000901",
        "bizAreaId": "20220002",
        "merchantCode": "809000011892864",
        "merchantType":"0"
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
