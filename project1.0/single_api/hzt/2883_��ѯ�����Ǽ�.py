# #导入数据处理加密的包
# import hashlib
# import json
# import requests
# # 定义加密KEY值
# keyString="11111111111111111111111111111111"
# #所有发送或者接收到的数据定义为字典类型数据
# data = {
# "timestamp": "20220706134515",
# "appVersion": "1.4.0",
# "clientType": "WEB",
# "platFormCode": "01",
# "apiVersion": "1.0",
# "bizContent":{
# "shopCode": "889107400000321",
# "incomingType": "02",
# "reportType": 1,
# "mbrType": 0,
# "mbrName": "刘丹",
# "mbrShortName": "刘丹",
# "crpTel":"18117247432",
# "mbrEnglishName": "liudan",
# "crpName": "刘丹",
# "crpIdType": 1,
# "crpIdCard": "54455554",
# "crpIdCardStDt": "2012-02-03",
# "crpIdCardExpDt": "2022-02-03",
# "acctTypeCode": 1,
# "acctNo": "6214832614759228",
# "acctName": "刘丹",
# "bankCode": "5",
# "bankName": "招商银行",
# "acctBankCode": "308290003853",
# "acctBankName": "招商银行上海分行宝山支行",
# "provinceCode": "3",
# "cityCode": "2900",
# "smsCode":"111111",
# "acctMobileNumber": "18117247432",
# "settleType": 1,
# "acctSettleFeeRatio":"11",
# "mbrResourceFiles": [
# {
# "fileClassify": "01",
# "fileType": "01",
# "fileSource": "IOS",
# "fileId": "20220707000000704935979594895360"
# },
# {
# "fileClassify": "01",
# "fileType": "02",
# "fileSource": "IOS",
# "fileId": "20220707000000704935979594895360"
# }
# ]
# }
# }
# #定义函数作用：去除参数的值为空的元素，返回参与签名的字典类型数据
# def GetSignData(data):
#     signData={}
#     for key, value in data.items():
#         if value != "":
#             signData[key] = value
#     return  signData
#
# #对参数按照key=value的格式，并按照参数名ASCII字典序排序拼接成字符串stringA，最后拼接上key，返回拼接API密钥。
# def SignString(signData,key):
#    #定义空列表
#    list=[]
#    # 定义空字符串
#    stringA=""
#    #循环遍历字典数据的键值，取出存放到列表中
#    for key in signData.keys():
#        list.append(key)
#    #对列表的对象进行排序，默认升序，即按照ASCII码从小到大排序
#    list.sort()
#    #循环遍历排序后的列表，根据键值取出字典键对应的值
#    for i in list:
#        if i =='bizContent':
#            signData[i] = json.dumps(signData[i],ensure_ascii=False)
#        stringA += i+"="+f'{signData[i].replace(" ","")}'+"&"
#
#     # 去除最后一个&
#    stringA = stringA[:len(stringA) - 1]
#    # 参数拼接成需要加密的字符串
#    stringA += data['timestamp']+keyString
#    return   stringA
#
# #调用GetSignData函数，获取参与签名的参数，返回新的字典数据
# signData=GetSignData(data)
# #调`用函数，返回需要加密的字符串`
# signBody=SignString(signData,keyString)
# print(signBody)
#
# #创建对象md
# md=hashlib.md5()
# #对stringA字符串进行编码
# md.update(signBody.encode('utf-8'))
# #数据加密
# signValue=md.hexdigest().upper()
# print(signValue)
#
# # 调用接口
# url = "https://hldapi-testapp.3vast.cn/hztzt-admin-merchant/member/incoming"
# headers = {"Content-Type":"application/json",
#            "isBizCount":"true",
#            "sign":f"{signValue}"}
# print(headers)
# r = requests.post(url=url,json=data,headers=headers)
# print(r.url)
# print(r.json())
#
#







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
    key='11111111111111111111111111111111'
    jarpath = os.path.join(os.path.abspath('.'), "sign.jar")  # os.path.abspath这个函数用来获取当前 python 脚本所在的绝对路径

    # 启动JVM
    jvmPath = jpype.getDefaultJVMPath()
    # 判断JVM是否启动
    if not jpype.isJVMStarted():
        # 加载jar包
        jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s"% jarpath)
    # 指定main class
    JDClass = jpype.JClass("Sign")
    # 创建类实例对象
    jd = JDClass()
    # 引用jar包类中的方法 rsa_sign
    signature = jd.hztSign(str(content),key)
    return signature
    # 关闭JVM
    jpype.shutdownJVM()



# 调用接口
url = "https://hldapi-testapp.3vast.cn/hldzt-admin-org/openCard/getConfig"
# 请求参数
content = {
        "timestamp": "20220706134515",
        "appVersion": "1.4.0",
        "clientType": "WEB",
        "platFormCode": "01",
        "apiVersion": "1.0",
        "bizContent":{
  "orgCode": "44985",
  "orgName": "sada"
}
}
# 调用加密包传入请求参数获取签名
sign = get_rsa_sign(content)
# 将签名传值给请求头中的sign
headers = {"Content-Type":"application/json",
           "isBizCount":"true",
           "sign":f"{sign}"}
# 打印请求头
print(headers)
r = requests.post(url=url,data = json.dumps(content),headers=headers)
print(r.url)
print(r.json())


