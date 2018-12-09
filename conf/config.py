
# 数据库配置
db_host = '115.28.108.130'
db_port = 3306
db_user = 'test'
db_password = '123456'
db = 'api_test'

#路径配置  计算文件的绝对路径
import os
#os.path.abspath()
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(project_path)
#数据文件目录
data_path = os.path.join(project_path,"data")
data_file = os.path.join(project_path,"data","data.xlsx")
# print(data_file)
#日志文件的根目录
log_file =  os.path.join(project_path,"log","log.txt")
report_file = os.path.join(project_path,"report","report.html")
# print(report_file)
# print(log_file)


#log配置
import  logging

# logging.basicConfig(level = logging.DEBUG,
#               format = "%(asctime)s  %(levelname)s  %(funcName)s  【%(filename)s-%(lineno)d】 %(message)s",
#               datefmt = "Y-%m-%d %H:%M:%S",
#               filename="../log/log.txt",
#               filemode="a"
#               )
logging.basicConfig(level=logging.DEBUG,
                    format = "%(asctime)s %(levelname)s %(funcName)s [%(filename)s-%(lineno)d] %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S",
                    filename=log_file,
                    )


#邮件配置
smtp_sever = "smtp.163.com"
smtp_user = "ivan-me@163.com"
smtp_password = "hanzhichao123"

receiver = "superhin@126.com"
subject = "接口测试报告"
body = "hi, all,\n附件中是接口测试报告,请查收."

is_send_report = False  #发送邮件开关

if  __name__ == "__main__":
    logging.info("hello , world")
    logging.info("中文日志")
    #print(os.path.abspath(__file__))