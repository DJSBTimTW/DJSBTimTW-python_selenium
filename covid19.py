from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
from datetime import date
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
today = date.today().strftime("%Y-%m-%d")
print(today)

options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://epidemic.ncut.edu.tw/login?redirect=%2FbodyTemp%2Fhistory")
wait = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,'el-input__inner')))
uid = chrome.find_elements_by_class_name("el-input__inner")[0]
pwd = chrome.find_elements_by_class_name("el-input__inner")[1]
f = open("covid.txt",mode='r')
txtread = f.read().splitlines()
uid.send_keys(txtread[0].strip())
pwd.send_keys(txtread[1].strip())
f.close()
signin = WebDriverWait(chrome, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'el-button'))).click()
 
 
def typein(dateselect,history,history2,history3):
    chrome.get("https://epidemic.ncut.edu.tw/bodyTemp")
    getdatewait = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.CLASS_NAME,'el-input__inner')))
    getdate = chrome.find_elements_by_class_name("el-input__inner")[0]
    getdate.clear()
    getdate.send_keys(dateselect)
    time.sleep(0.5)
    ActionChains(chrome).move_by_offset(0, 0).click().perform() # 鼠標左鍵點擊0
    time.sleep(0.5)

    temp = chrome.find_element_by_class_name("el-radio-button")
    temp.click()
    time.sleep(0.5)

    his = chrome.find_elements_by_class_name("el-textarea__inner")[0]
    his.send_keys(history)
    time.sleep(0.5)
    his2 = chrome.find_elements_by_class_name("el-textarea__inner")[1]
    his2.send_keys(history2)
    time.sleep(0.5)
    his3 = chrome.find_elements_by_class_name("el-textarea__inner")[2]
    his3.send_keys(history3)
    time.sleep(0.5)
    save = chrome.find_element_by_css_selector("#main > div:nth-child(1) > div.el-row > div > form > button").click()
    time.sleep(1)
    print('表單送出')
 
 
dateselect = str(input('請輸入日期(格式為YYYY-MM-DD)(輸入空白則跳出):'))
while dateselect != "":
        history = str(input('請輸入活動紀錄(上午)(輸入空白為預設:工作(At work))'))
        if history =="":
            history=str("工作(At work)")
        history2 = str(input('請輸入活動紀錄(下午)(輸入空白為預設:工作(At work))'))
        if history2 =="":
            history2=str("工作(At work)")
        history3 = str(input('請輸入活動紀錄(晚上)(輸入空白為預設:家中(Home))'))
        if history3 =="":
            history3=str("家中(Home)")
        typein(dateselect,history,history2,history3)
        dateselect = str(input('請輸入日期(格式為YYYY-MM-DD)(輸入空白則跳出):'))
chrome.quit()
