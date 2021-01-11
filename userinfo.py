import requests,bs4,time,sqlcon
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def getinfo(CID,PWR):
    options = Options()
    options.add_argument("--disable-notifications")
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get("https://mypage.groovecoaster.jp/sp/login/auth.php")
    cardid = chrome.find_element_by_name("nesicaCardId")
    pwd = chrome.find_element_by_name("password")
    cardid.send_keys(CID)
    pwd.send_keys(PWR)
    pwd.submit()
    time.sleep(2)
    if chrome.current_url=='https://mypage.groovecoaster.jp/sp/#/':
        userdata = {}
        user=["cid","uid","tScore","aScore","pMusic","rank","avatar","title","clear","noMiss","fullChain","perfect","s","ss","sss","trophy","tRank"]
        soup = bs4.BeautifulSoup(chrome.page_source,'html.parser')
        playername = soup.find("div",class_='txtTopName').text.strip()
        userdata[str(user[0])]=CID
        userdata[str(user[1])]=playername
        finddata = soup.find("div",class_='bgTopCenter').find_all("div",class_='icnTop')
        u = 1
        for i in range(len(finddata)):
            u+=1
            userdata[str(user[u])]=finddata[i].text.strip()
        print(userdata)
        sqlcon.userinfo(userdata)
        chrome.quit()
        return('OK')
    elif chrome.current_url!='https://mypage.groovecoaster.jp/sp/#/':
        chrome.quit()
        return('error')