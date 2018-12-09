# 1.组装邮件
# 2.组装邮件头
# 3.链接SMTP服务器并发送

import smtplib  #连接SMTP服务器并发送邮件
from email.mime.text import MIMEText
from email.mime.multipart import  MIMEMultipart

#1.组装邮件正文
msg = MIMEMultipart()        #混合格式消息体
body = MIMEText("python发送的文件","plain","utf-8")     #plain纯文字
msg.attach(body)    #         将正文添加到msg对象中

#2.组装邮件头
msg["From"] = "test_results@sina.com"
msg["To"] = "784134325@qq.com"
msg["Subject"] = "from python"

#附件

with open("../report/report.html","rb") as f:
    att_file = f.read()

att = MIMEText(att_file, 'base64',"utf-8")
att["Content-Type"] = 'application/octet-stream' # 声明附件的内容格式 MIME数据流格式
att["Content-Disposition"] = "attachment;filename='report.html'" # 附件描述信息 filename是附件显示的文件名
msg.attach(att)    #将附件添加到消息对象中
#链接SMTP服务器并发送
smtp = smtplib.SMTP("smtp.163.com")  #建立连接
smtp.login("ivan-me@163.com","hanzhichao123")  #登录
smtp.sendmail("ivan-me@163.com","784134325@qq.com",msg.as_string())   #将mime格式邮件转化成字符串发送
