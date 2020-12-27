import requests,bs4,time,os,csv,json,re
from pprint import pprint,pformat
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
pwd.submit()

userinfo = {}
userdata = {}
user=["uid","tScore","aScore","pMusic","rank","avatar","title","clear","noMiss","fullChain","perfect","s","ss","sss","trophy","tRank"]

testcsv= open('player.csv',mode='w',encoding='utf-8', newline='')
writer = csv.writer(testcsv)
writer.writerow(["ID","uid","tScore","aScore","pMusic","rank","avatar","title","clear","noMiss","fullChain","perfect","s","ss","sss","trophy","tRank"])

time.sleep(3)

soup = bs4.BeautifulSoup(chrome.page_source,'html.parser')
playername = soup.select_one("#view_area > div.txtTopName.frnd.plyrNm.ng-scope.ng-binding").text.strip()
userdata[str(user[0])]=playername
finddata = soup.find("div",class_='bgTopCenter').find_all("div",class_='icnTop')
u = 0
for i in range(len(finddata)):
    u+=1
    userdata[str(user[u])]=finddata[i].text.strip()
pprint(userdata)
writer.writerow([txtread[0].strip(),userdata["uid"],userdata["tScore"],userdata["aScore"],userdata["pMusic"],userdata["rank"],userdata["avatar"],userdata["title"],userdata["clear"],userdata["noMiss"],userdata["fullChain"],userdata["perfect"],userdata["s"],userdata["ss"],userdata["sss"],userdata["trophy"],userdata["tRank"]])
f.close()
testcsv.close()
chrome.get("https://mypage.groovecoaster.jp/sp/json/music_list.php")
pre = chrome.find_element_by_tag_name("pre").text
data = json.loads(pre)
pdata = pformat(data).split('[',1)[1].rsplit(']',1)[0]
ndata = re.split(r'{|},',pdata)
m = open('mdata.txt',mode='w',encoding='utf-8',newline='')
for i in range(len(ndata)):
    m.write(ndata[i])
m.close
rm = open('mdata.txt',mode='r',encoding='utf-8',newline='')
nm = open('nmdata.txt',mode='w',encoding='utf-8',newline='')
lines=rm.readlines()
for line in lines:
    nline = line.replace("'","").replace(",","").strip()
    nm.write(nline)
    nm.write("\n")
rm.close()
nm.close()