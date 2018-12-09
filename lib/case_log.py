
from conf import  config

def case_log(case_name,url,data,excepted_res,actual_res):

    config.logging.info("_"*50)
    config.logging.info("执行用例:{}".format("test_user_login_normal"))
    config.logging.info("接口地址:{}".format(url))
    config.logging.info("请求数据:{}".format(case_data[3]))
    config.logging.info("期望结果:{}".format(case_data[4]))
    config.logging.info("实际结果:{}".format(res.text))