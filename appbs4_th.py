import requests,bs4,time,os,csv,json,re,sqlcon,threading
from pprint import pprint,pformat
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def data_th(CID,PWR,lines,thnum):
    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get("https://mypage.groovecoaster.jp/sp/login/auth.php")
    cardid = chrome.find_element_by_name("nesicaCardId")
    pwd = chrome.find_element_by_name("password")
    cardid.send_keys(CID)
    pwd.send_keys(PWR)
    pwd.submit()
    time.sleep(3)
    line_all=len(lines)
    line_half=int(len(lines)/2)
    if thnum=='0':
        for i in range(0,line_half):
            if lines[i]!="":
                url=("https://mypage.groovecoaster.jp/sp/#/mc/"+str(lines[i]))
                chrome.get(url)
                wait = WebDriverWait(chrome,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(3) > div > div.txtMusicRslt.right > div:nth-child(2)")))
                soup = bs4.BeautifulSoup(chrome.page_source,'html.parser')
                playdata_th(soup,CID)
        chrome.quit()
    elif thnum=='1':
        try:
            for u in range(line_half,line_all+1):
                if lines[u]!="":
                    url=("https://mypage.groovecoaster.jp/sp/#/mc/"+str(lines[u]))
                    chrome.get(url)
                    wait = WebDriverWait(chrome,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(3) > div > div.txtMusicRslt.right > div:nth-child(2)")))
                    soup = bs4.BeautifulSoup(chrome.page_source,'html.parser')
                    playdata_th(soup,CID)
        except Exception as e:
            print("")
    elif thnum=='a':
        for u in range(0,line_all+1):
            if lines[u]!="":
                url=("https://mypage.groovecoaster.jp/sp/#/mc/"+str(lines[u]))
                chrome.get(url)
                wait = WebDriverWait(chrome,30).until(EC.visibility_of_element_located((By.CSS_SELECTOR,"#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(3) > div > div.txtMusicRslt.right > div:nth-child(2)")))
                # time.sleep(3)
                soup = bs4.BeautifulSoup(chrome.page_source,'html.parser')
                playdata_th(soup,CID)
    chrome.quit()


def playdata_th(soup,CID):
    sqlcon.playdb()
    data={}
    name = soup.find("div",class_="txtMusicDetail name ng-binding").text.strip()
    spc = soup.find("div",class_="hdrRslt simple").find("div",class_="txtMusicRslt left").find_all("div",class_="rslt ng-binding")[0].text
    sps = soup.find("div",class_="hdrRslt simple").find("div",class_="txtMusicRslt right").find_all("div",class_="rslt ng-binding")[0].text
    npc = soup.find("div",class_="hdrRslt normal").find("div",class_="txtMusicRslt left").find_all("div",class_="rslt ng-binding")[0].text
    nps = soup.find("div",class_="hdrRslt normal").find("div",class_="txtMusicRslt right").find_all("div",class_="rslt ng-binding")[0].text
    hpc = soup.find("div",class_="hdrRslt hard").find("div",class_="txtMusicRslt left").find_all("div",class_="rslt ng-binding")[0].text
    hps = soup.find("div",class_="hdrRslt hard").find("div",class_="txtMusicRslt right").find_all("div",class_="rslt ng-binding")[0].text
    try:
        epc = soup.find("div",class_="hdrRslt extra").find("div",class_="txtMusicRslt left").find_all("div",class_="rslt ng-binding")[0].text
        eps = soup.find("div",class_="hdrRslt extra").find("div",class_="txtMusicRslt right").find_all("div",class_="rslt ng-binding")[0].text
        data={'cid':CID,'name':name,'spc':spc,'sps':sps,'npc':npc,'nps':nps,'hpc':hpc,'hps':hps,'epc':epc,'eps':eps}
        sqlcon.palyda(data)
    except Exception as e:
        print("none ex")
        data={'cid':CID,'name':name,'spc':spc,'sps':sps,'npc':npc,'nps':nps,'hpc':hpc,'hps':hps,'epc':"0",'eps':"0"}
        sqlcon.palyda(data)

def playdata(CID,PWR):
    sqlcon.playdb()
    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get("https://mypage.groovecoaster.jp/sp/login/auth.php")
    cardid = chrome.find_element_by_name("nesicaCardId")
    pwd = chrome.find_element_by_name("password")
    cardid.send_keys(CID)
    pwd.send_keys(PWR)
    pwd.submit()
    time.sleep(3)
    if chrome.current_url=='https://mypage.groovecoaster.jp/sp/#/':
        soup = bs4.BeautifulSoup(chrome.page_source,'html.parser')
        pid = soup.select_one("#view_area > div.txtTopName.frnd.plyrNm.ng-scope.ng-binding").text.strip()
        chrome.get("https://mypage.groovecoaster.jp/sp/json/music_list.php")
        time.sleep(2)
        pre = chrome.find_element_by_tag_name("pre").text
        data = json.loads(pre)
        pdata = pformat(data).split('[',1)[1].rsplit(']',1)[0]
        ndata = re.split(r'{|},',pdata)
        with open('mdata.txt',mode='w',encoding='utf-8',newline='') as m:
            for i in range(len(ndata)):
                newline = str(ndata[i].replace("'","").replace("}","").replace(" ","").replace(",",""))
                if (newline!="\n")&(newline!=""):
                    newlines = newline.split(',')
                    m.write(newline)
                    m.write("\n")
        chrome.quit()
        with open('mdata.txt',mode='r',encoding='utf-8',newline='') as m:
            with open('nmdata.txt',mode='w',encoding='utf-8',newline='') as nm:
                lines=m.readlines()
                for line in lines:
                    nline = line.strip()
                    if (nline!="\n")&(nline!="")&(str(nline.split(':',1)[0])=="music_id"):
                        nm.write(nline.split(':',1)[1]+"\n")

        with open('nmdata.txt',mode='r',encoding='utf-8',newline='') as nmd:
            lines=nmd.readlines()
            one =threading.Thread(target = data_th, args =(CID,PWR,lines,'0'))
            two =threading.Thread(target = data_th, args =(CID,PWR,lines,'1'))
            one.start()
            two.start()
            one.join()
            two.join()
        return('OK')
    elif chrome.current_url!='https://mypage.groovecoaster.jp/sp/#/':
        chrome.quit()
        return('error')