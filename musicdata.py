from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time,requests,os,csv
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("--disable-notifications")
chrome = webdriver.Chrome('./chromedriver', chrome_options=options)
chrome.get("https://groovecoaster.jp/music/")
def geturl():
    f = open('url.txt',mode='w',encoding='utf-8', newline='')
    time.sleep(2)
    for u in range(1,8):
        url=chrome.find_elements_by_xpath("/html/body/div[2]/div/section/div/div/div[3]/div/div["+str(u)+"]/ul")
        urlcount = len(url)
        print(len(url))
        for i in range(1,(urlcount+1)):
            try:
                for n in range(1,13):
                    nurl=chrome.find_elements_by_xpath("/html/body/div[2]/div/section/div/div/div[3]/div/div["+str(u)+"]/ul["+str(i)+"]/li["+str(n)+"]/a")[0].get_attribute("href")
                    print(nurl)
                    f.write(str(nurl))
                    f.write("\n")
            except Exception as e:
                print('none')
    f.close()

typein = str(input("n")).strip()
if typein == "n":
    geturl()
elif typein == "m":
    f = open('url.txt',mode='r')
    txt= open('song.csv',mode='w',encoding='utf-8', newline='')
    writer = csv.writer(txt)
    writer.writerow(['name','arts','bpm','genre','simple','normal','hard','extra'])
    lines=f.readlines()
    for line in lines:
        url=line.strip()
        print(url)
        chrome.execute_script("window.open();")
        chrome.switch_to_window(chrome.window_handles[1])
        chrome.get(url)
        wait = WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[2]/div/section/div/div/div[1]/h3/span")))
        gettext = chrome.find_elements_by_css_selector("#container > div > section > div > div > div.title-block > h3 > span")[0].get_attribute("innerHTML").strip()
        name = gettext.split('／')[0].strip()
        arts = gettext.split('／')[1].strip()
        print(name)
        print(arts)     
        getgen = chrome.find_elements_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/p/a")[0].get_attribute("href")
        sgen=getgen.split("/")[-1][1:]
        print(sgen)
        getbpm = chrome.find_elements_by_css_selector("#container > div > section > div > div > div.song-block > div.param-block > div.details > ul > li.bpm")[0].get_attribute("innerHTML")
        print(getbpm)
        try:
            slv = chrome.find_elements_by_css_selector("#container > div > section > div > div > div.song-block > div.param-block > div.difficulty > ul > li.simple > img")[0].get_attribute("src")
            sslv = str(slv).split("_")[2].split(".")[0]
            print(sslv)
            nlv = chrome.find_elements_by_css_selector("#container > div > section > div > div > div.song-block > div.param-block > div.difficulty > ul > li.normal > img")[0].get_attribute("src")
            snlv = str(nlv).split("_")[2].split(".")[0]
            print(snlv)
            hlv = chrome.find_elements_by_css_selector("#container > div > section > div > div > div.song-block > div.param-block > div.difficulty > ul > li.harder > img")[0].get_attribute("src")
            shlv = str(hlv).split("_")[2].split(".")[0]
            print(shlv)
            elv = chrome.find_elements_by_css_selector("#container > div > section > div > div > div.song-block > div.param-block > div.difficulty > ul > li.extra > img")[0].get_attribute("src")
            selv = str(elv).split("_")[2].split(".")[0]
            print(selv)
            writer.writerow([name,arts,getbpm,sgen,sslv,snlv,shlv,selv])
        except Exception as e:
            print("none")
            writer.writerow([name,arts,getbpm,sgen,sslv,snlv,shlv,""])
        chrome.close()
        chrome.switch_to_window(chrome.window_handles[0])
    f.close()
    txt.close()
    chrome.close()