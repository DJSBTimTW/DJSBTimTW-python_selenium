from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
 
options = Options()
options.add_argument("--disable-notifications")
 
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://mypage.groovecoaster.jp/sp/login/auth.php")
cardid = chrome.find_element_by_name("nesicaCardId")
pwd = chrome.find_element_by_name("password")
f = open("app.txt",mode='r')
txtread = f.read().splitlines()
cardid.send_keys(txtread[0].strip())
pwd.send_keys(txtread[1].strip())
f.close()
pwd.submit()

chrome.get("https://mypage.groovecoaster.jp/sp/#/")

userinfo = {}
time.sleep(5)

uid = chrome.find_elements_by_class_name("txtTopName")[0].get_attribute("innerHTML")
tScore = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.tScore.ng-binding")[0].get_attribute("innerHTML")
aScore = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.aScore.ng-binding")[0].get_attribute("innerHTML")
pMusic = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.pMusic.ng-binding")[0].get_attribute("innerHTML")
rank = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.rank > span")[0].get_attribute("innerHTML")
avatar = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.avatar.ng-binding")[0].get_attribute("innerHTML")
title = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.title.ng-binding")[0].get_attribute("innerHTML")
clear = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.clear.ng-binding")[0].get_attribute("innerHTML")
noMiss = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.noMiss.ng-binding")[0].get_attribute("innerHTML")
fullChain = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.fullChain.ng-binding")[0].get_attribute("innerHTML")
perfect = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.perfect.ng-scope.ng-binding")[0].get_attribute("innerHTML")
s = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.s.ng-binding")[0].get_attribute("innerHTML")
ss = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.ss.ng-binding")[0].get_attribute("innerHTML")
sss = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.sss.ng-binding")[0].get_attribute("innerHTML")
trophy = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.trophy.ng-scope.ng-binding")[0].get_attribute("innerHTML")
tRank = chrome.find_elements_by_css_selector("#view_area > div:nth-child(2) > div.bgTopCenter > div.icnTop.tRank.ng-scope > span")[0].get_attribute("innerHTML")

userinfo["uid"]=uid
userinfo["tScore"]=tScore
userinfo["aScore"]=aScore
userinfo["pMusic"]=pMusic
userinfo["rank"]=rank
userinfo["avatar"]=avatar
userinfo["title"]=title
userinfo["clear"]=clear
userinfo["noMiss"]=noMiss
userinfo["fullChain"]=fullChain
userinfo["perfect"]=perfect
userinfo["s"]=s
userinfo["ss"]=ss
userinfo["sss"]=sss
userinfo["trophy"]=trophy
userinfo["tRank"]=tRank

for i in userinfo.items():
    print("{}:{}".format(i[0],i[1]))


# wait = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div[3]/div[53]/a")))
# wait = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div[3]/div[54]/span[1]")))
# page = chrome.find_elements_by_xpath("/html/body/div[2]/div/div[3]/div[54]/span[1]")[0].get_attribute("innerHTML").split(' / ',1)
# for i in range(int(page[1])):
#     print((i+1))
#     wait = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/div[3]/div[53]/a")))
#     for u in range(50):
#         playpage1 = chrome.find_elements_by_xpath("/html/body/div[2]/div/div[3]/div["+str(u+4)+"]/a")[0].get_attribute("innerHTML").splitlines()
#         # playpage2 = chrome.find_elements_by_xpath("/html/body/div[2]/div/div[3]/div["+str(u+4)+"]/a")[0].get_attribute("href")
#         print(playpage1[1].strip())
#         # print(playpage2)
#     if i == 0:
#         pagebtn = chrome.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[54]/span[2]").click()
#     else:
#         pagebtn = chrome.find_element_by_xpath("/html/body/div[2]/div/div[3]/div[54]/span[3]").click()
#     print("")

chrome.execute_script("window.open();")
chrome.switch_to_window(chrome.window_handles[1])
chrome.get("https://mypage.groovecoaster.jp/sp/json/music_detail.php"+"?"+"music_id="+"669")