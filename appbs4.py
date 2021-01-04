import requests,bs4,time,os,csv,json,re,sqlcon
from pprint import pprint,pformat
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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

    with open('mdata.txt',mode='r',encoding='utf-8',newline='') as m:
        with open('nmdata.txt',mode='w',encoding='utf-8',newline='') as nm:
            lines=m.readlines()
            data={}
            print(str(len(lines)))
            for line in lines:
                nline = line.strip()
                if (nline!="\n")&(nline!="")&(str(nline.split(':',1)[0])=="music_id"):
                    nm.write(nline.split(':',1)[1]+"\n")
                if str(nline.split(':',1)[0])=="music_id":
                    url=("https://mypage.groovecoaster.jp/sp/#/mc/"+str(nline.split(':',1)[1]))
                    chrome.get(url)
                    time.sleep(0.5)
                    soup = bs4.BeautifulSoup(chrome.page_source,'html.parser')
                    name = soup.select_one("#view_area > div > div > div.bgMusicDetail.top > div > div.txtMusicDetail.name.ng-binding").text
                    nm.write(name+"\n")
                    spc = soup.select_one("#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(1) > div > div.txtMusicRslt.left > div:nth-child(2)").text
                    sps = soup.select_one("#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(1) > div > div.txtMusicRslt.right > div:nth-child(2)").text
                    npc = soup.select_one("#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(2) > div > div.txtMusicRslt.left > div:nth-child(2)").text
                    nps = soup.select_one("#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(2) > div > div.txtMusicRslt.right > div:nth-child(2)").text
                    hpc = soup.select_one("#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(3) > div > div.txtMusicRslt.left > div:nth-child(2)").text
                    hps = soup.select_one("#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(3) > div > div.txtMusicRslt.right > div:nth-child(2)").text
                    nm.write("簡單遊玩次數:{}\n簡單遊玩分數:{}\n普通遊玩次數:{}\n普通遊玩分數:{}\n困難遊玩次數:{}\n困難遊玩分數:{}\n".format(spc,sps,npc,nps,hpc,hps))
                    try:
                        epc = soup.select_one("#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(4) > div > div.txtMusicRslt.left > div:nth-child(2)").text
                        eps = soup.select_one("#view_area > div > div > div._bgMusicDetail.center > div:nth-child(2) > div > div:nth-child(4) > div > div.txtMusicRslt.right > div:nth-child(2)").text
                        nm.write("EX遊玩次數:{}\nEX遊玩分數:{}\n".format(epc,eps))
                        nm.write("總遊玩次數:"+str(int(spc)+int(npc)+int(hpc)+int(epc))+"\n")
                        data={'cid':CID,'name':name,'spc':spc,'sps':sps,'npc':npc,'nps':nps,'hpc':hpc,'hps':hps,'epc':epc,'eps':eps}
                        sqlcon.palyda(data)
                    except Exception as e:
                        nm.write("總遊玩次數:"+str(int(spc)+int(npc)+int(hpc))+"\n")
                        print("none ex")
                        data={'cid':CID,'name':name,'spc':spc,'sps':sps,'npc':npc,'nps':nps,'hpc':hpc,'hps':hps,'epc':"",'eps':""}
                        sqlcon.palyda(data)
                    nm.write("\n")
    chrome.quit()