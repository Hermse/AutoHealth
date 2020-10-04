import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
stu_number = ' '     #学号
stu_psword = ' '       #密码
driver = webdriver.Edge(" ")           #Edge浏览器驱动
#https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/#downloads    Edge浏览器驱动下载地址




opt = Options()
# opt.add_argument('--headless')    #想要静默运行，则取消本代码注释
driver.get("https://app.ncepu.edu.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.ncepu.edu.cn%2Fncov%2Fwap%2Fdefault%2Findex")

elem = driver.find_element_by_css_selector("input[type=\"text\"]")
elem.send_keys(stu_number)
elem = driver.find_element_by_css_selector("input[type=\"password\"]")
elem.send_keys(stu_psword)
driver.find_element_by_class_name("btn").click()
time.sleep(0.5)
driver.find_element_by_name("area").click()
time.sleep(0.5)
driver.find_element_by_xpath("//div[@class=\"list-box\"]/div/a").click()
elem = driver.find_element_by_class_name("wapcf-btn-ok").click()
driver.close()
