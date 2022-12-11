import time

import schedule as schedule
import yagmail

from utils.log_util import logger
from utils.read_config import to_email, user_name, host_email


def do_job():
    try:
        username = user_name # 发送者账号
        # passwd = '授权码'  # 发送者授权码，如果不需要授权码就写成密码,此处不建议直接写到代码当中
        email = yagmail.SMTP(user=username, host=host_email)
        email.send(
            to=eval(to_email), # 收件人邮箱，如果多个收件人的话，写成list就行了
            subject='接口自动化测试结果',  # 邮件标题
            contents=['本条消息为系统自动发送的接口自动化测试邮件',
                      '测试报告详见附件压缩包'],
                      # yagmail.inline('核验148_211205.jpg'),],  # 邮件内容
            attachments=r'C:\Users\24113\ldproject\project3 .0\result.zip'
        )  # 发送附件，如果是win10系统，发送时找不到附件就将附件地址写成r'D:\\syz_python\\code\\day9\\签名规则'

        logger.info('发送成功')
        email.close()
    except Exception as e:
        logger.debug("发送失败！", e.args)

# schedule.every(10).minutes.do(do_job)
# schedule.every().hour.do(do_job)
# schedule.every().day.at("08:50").do(do_job)
# schedule.every(5).to(10).minutes.do(do_job)
# schedule.every().monday.do(do_job)
# schedule.every().wednesday.at("10:30").do(do_job)
# schedule.every().minute.at(":30").do(do_job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)






