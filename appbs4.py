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
time.sleep(0.5)
pre = chrome.find_element_by_tag_name("pre").text
data = json.loads(pre)
pdata = pformat(data).split('[',1)[1].rsplit(']',1)[0]
ndata = re.split(r'{|},',pdata)
m = open('mdata.txt',mode='w',encoding='utf-8',newline='')
for i in range(len(ndata)):
    newline = str(ndata[i].replace("'","").replace("}","").replace(" ",""))
    if (newline!="\n")&(newline!=""):
        newlines = newline.split(',')
        for u in range(len(newlines)):
            newdata = str(newlines[u])
            m.write(newdata)
        m.write("\n"+"\n")
m.close
rm = open('mdata.txt',mode='r',encoding='utf-8',newline='')
nm = open('nmdata.txt',mode='w',encoding='utf-8',newline='')
lines=rm.readlines()
for line in lines:
    nline = line.replace("'","").replace(",","").strip()
    if str(nline.split(':',1)[0])=="music_id":
        nm.write(nline.split(':',1)[1]+"\n")
    # if str(nline.split(':',1)[0])=="music_id":
    #     url=("https://mypage.groovecoaster.jp/sp/#/mc/"+str(nline.split(':',1)[1]))
    #     chrome.get(url)
    #     time.sleep(0.5)
    #     soup = bs4.BeautifulSoup(chrome.page_source,'html.parser')
    #     songname = soup.select_one("#view_area > div > div > div.bgMusicDetail.top > div > div.txtMusicDetail.name.ng-binding").text
    #     nm.write(songname+"\n")
    #     try:
    #         arts = soup.select_one("#view_area > div > div > div.bgMusicDetail.top > div > div.txtMusicDetail.artist.ng-scope.ng-binding").text
    #         nm.write(arts+"\n")
    #         playcount = soup.select_one("#view_area > div > div > div.bgMusicDetail.top > div > div:nth-child(6)").text
    #     except Exception as e:
    #         playcount = soup.select_one("#view_area > div > div > div.bgMusicDetail.top > div > div:nth-child(4)").text
    #         print("none arts")
    #     nm.write("總遊玩次數："+playcount.split(':',1)[1]+"\n")
    #     nm.write("\n")
nm.close()
rm.close()
# npdata = open('nmdata.txt',mode='r',encoding='utf-8',newline='')
# mpdata = open('mpdata.txt',mode='w',encoding='utf-8',newline='')
# lines=npdata.readlines()
# for line in lines:
#     pline = re.sub(r'[\'{},\s]*',"",line)
#     mpdata.write(pline)
#     mpdata.write("\n")
# npdata.close()
# mpdata.close()
