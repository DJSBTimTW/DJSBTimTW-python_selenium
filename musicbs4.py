import requests,bs4,time,os,csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pprint import pprint
import userinfo,sqlcon,appbs4
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def getmusicurl():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
    chrome.get("https://groovecoaster.jp/music/")
    with open('url.txt',mode='w',encoding='utf-8', newline='') as urls:
        time.sleep(2)
        for u in range(1,8):
            ul=chrome.find_elements_by_xpath("/html/body/div[2]/div/section/div/div/div[3]/div/div["+str(u)+"]/ul")
            ulcount = len(ul)
            print(len(ul))
            for i in range(1,(ulcount+1)):
                for n in range(1,13):
                    try:
                        nurl=chrome.find_elements_by_xpath("/html/body/div[2]/div/section/div/div/div[3]/div/div["+str(u)+"]/ul["+str(i)+"]/li["+str(n)+"]/a")[0].get_attribute("href")
                        print(nurl)
                        urls.write(str(nurl))
                        urls.write("\n")
                    except Exception as e:
                        print('')

def getmusicbs4(ty):
    if ty == "0":
        with open('url.txt',mode='r',encoding='utf-8', newline='') as urls:
            songinfo={}
            lines=urls.readlines()
            for line in lines:
                url=line.strip()
                getsongdata(url)
    else:
        getsongdata(ty)

def getsongdata(url):
    sqlcon.songdb()
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    try:
        title = soup.find("div",class_="title-block").h3.span.text.strip()
        try:
            ts=title.split("／",2)
            name=ts[0].strip()
            arts=ts[1].strip()
            print("{}:{}".format(ts[0].strip(),ts[1].strip()))
        except Exception as e:
            ts=title.split("／",1)
            name=ts[0].strip()
            arts=ts[1].strip()
            print("{}:{}".format(ts[0].strip(),ts[1].strip()))
        getgen = soup.find("div",class_="btnback-block").p.a.get("href")
        gen = getgen[3:]
        print(gen)
        bpm = soup.find("li",class_="bpm").text
        print(bpm)
        slv = soup.find("li",class_="simple").find("img").get("src")
        nlv = soup.find("li",class_="normal").find("img").get("src")
        hlv = soup.find("li",class_="harder").find("img").get("src")
        sslv = str(slv).split("_")[2].split(".")[0]
        snlv = str(nlv).split("_")[2].split(".")[0]
        shlv = str(hlv).split("_")[2].split(".")[0]
        try:
            elv = soup.find("li",class_="extra").find("img").get("src")
            selv = str(elv).split("_")[2].split(".")[0]
            print("{}:{}:{}:{}\n".format(sslv,snlv,shlv,selv))
            songinfo={'name': name, 'arts': arts, 'bpm': bpm, 'gen': gen, 'simple': sslv, 'normal': snlv, 'hard': shlv, 'extra': selv, 'del': '0'}
            sqlcon.songdata(songinfo)
        except Exception as e:
            print("{}:{}:{}:{}\n".format(sslv,snlv,shlv,""))
            songinfo={'name': name, 'arts': arts, 'bpm': bpm, 'gen': gen, 'simple': sslv, 'normal': snlv, 'hard': shlv, 'extra': '0', 'del' :'0'}
            sqlcon.songdata(songinfo)
    except Exception as e:
        print("none url")

def getmusic():
    getmusicurl()
    getmusicbs4("0")

def manualmusic(songinfo):
    try:
        sqlcon.songdb()
        try:
            sqlcon.songdata(songinfo)
            return('OK')
        except Exception as e:
            return('daerror')
    except Exception as e:
        return('dberror')

typein = str(input("n")).strip()
if typein == "n":
    cidtype = str(input("CID")).strip()
    pwrtype = str(input("PWR")).strip()
    userinfo.getinfo(cidtype,pwrtype)
    appbs4.playdata(cidtype,pwrtype)
elif typein == "p":
    getmusicurl()
elif typein == "z":
    ty = str(input("URL")).strip()
    getmusicbs4(ty)
elif typein == "c":
    CID = str(input('CID')).strip()
    lv = str(input('lv')).strip()
    sqlcon.playdataget(CID,lv)