# python3.7.6
# -*- coding: utf-8 -*-
# @Time    : 2022/12/11 11:41
# @Author  : liudan
# @File    : convert_data.py
# @Software: PyCharm
# @Email : liudan@shxgroup.net
# @Project : framwork2
# @version : v4.0
import json
import random
import string

import jsonpath

from utils.log_util import logger

depend = {}

class DataConvert():
    # 匿名函数用于生成随机长度的字符串
    generate_random_str = lambda self,x: ''.join(random.choices(string.digits + string.ascii_letters, k=x))
    # def generate_random_str(self,length: int) -> str:
    #     """
    #     length: 指定随机字符串长度
    #     """
    #     base_str = string.digits + string.ascii_letters
    #     random_str = ''.join(random.choices(base_str, k=length))
    #     return random_str

    def convertBody(self, body):
        logger.info("找出存在可变变量区间块。。。。")
        # 找出变量区间块
        # strsplitvar = body.split('$')[1]
        try:
            listsplitvar = body.split('$')
            num = 0
            for strrequest in listsplitvar:
                logger.info("分割字符串。。。。")
                # 从$分割字符串，奇数的得到要取代的块
                if num % 2 == 1:
                    # 取代的块赋值给strchuck
                    strchuck = strrequest
                    # 找到全局变量名称
                    logger.info("找块中全局变量的名称。。。。")
                    stevar = strchuck[:strchuck.find('.')]
                    # 从depend获取变量值
                    logger.info("获取全局变量json值。。。。")
                    varvalue = depend[stevar]
                    # varvalue = str(varvalue, encoding="utf-8")
                    # 得到变量后面的jsonpath
                    logger.info("获取块中jsonpath。。。。")
                    varjsonpath = strchuck[strchuck.find('.') + 1:]
                    varjsonresult = json.loads(varvalue)

                    # 从全局变量中获取到jsonpath里面的值
                    logger.info("由jsonpath从全局变量里面取值并替换变量块。。。。")
                    varchuck = jsonpath.jsonpath(varjsonresult, expr='$.' + varjsonpath)
                    listsplitvar[num] = str(varchuck[0])

                num = num + 1

            strsplitvar=''.join(listsplitvar)
        except Exception as e:
            logger.error("替换变量块出错，请查看问题！原因: s%", e)

        return strsplitvar
if __name__ =="__main__":
    # print(DataConvert().generate_random_str(10))
    body ={
	"store": {
		"book": [{
				"category": "reference",
				"author": "Nigel Rees",
				"title": "Sayings of the Century",
				"price": 8.2
			}, {
				"category": "fiction",
				"author": "Evelyn Waugh",
				"title": "Sword of Honour",
				"price": 2.99
			}, {
				"category": "fiction",
				"author": "Herman Melville",
				"title": "Moby Dick",
				"isbn": "0-553-21311-3",
				"price": 8.09
			}, {
				"category": "fiction",
				"author": "J. R. R. Tolkien",
				"title": "The Lord of the Rings",
				"isbn": "0-395-19395-8",
				"price": 2.99
			}
		],
		"bicycle": {
			"color": "red",
			"price": 19.95
		}
	}
}
print(DataConvert().convertBody(json.dumps(body,ensure_ascii=False)))




