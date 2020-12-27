import requests,bs4,time,os,csv

f = open('url.txt',mode='r',encoding='utf-8', newline='')
txt= open('song.csv',mode='w',encoding='utf-8', newline='')
writer = csv.writer(txt)
writer.writerow(['name','arts','bpm','genre','simple','normal','hard','extra'])
lines=f.readlines()
for line in lines:
    url=line.strip()
    html = requests.get(url)
    html.encoding = 'utf-8'
    soup = bs4.BeautifulSoup(html.text, 'html.parser')
    gettext = soup.select_one("#container > div > section > div > div > div.title-block > h3 > span").text
    name = gettext.split('／')[0].strip()
    arts = gettext.split('／')[1].strip()
    print(name)
    print(arts)
    getgen = soup.select_one("#captions > div > div.btnback-block > p > a").get("href")
    sgen=getgen.split("/")[-1][1:]
    print(sgen)
    getbpm = soup.select_one("#container > div > section > div > div > div.song-block > div.param-block > div.details > ul > li.bpm").text
    print(getbpm)
    try:
        slv = soup.select_one("#container > div > section > div > div > div.song-block > div.param-block > div.difficulty > ul > li.simple > img").get("src")
        sslv = str(slv).split("_")[2].split(".")[0]
        print(sslv)
        nlv = soup.select_one("#container > div > section > div > div > div.song-block > div.param-block > div.difficulty > ul > li.normal > img").get("src")
        snlv = str(nlv).split("_")[2].split(".")[0]
        print(snlv)
        hlv = soup.select_one("#container > div > section > div > div > div.song-block > div.param-block > div.difficulty > ul > li.harder > img").get("src")
        shlv = str(hlv).split("_")[2].split(".")[0]
        print(shlv)
        elv = soup.select_one("#container > div > section > div > div > div.song-block > div.param-block > div.difficulty > ul > li.extra > img").get("src")
        selv = str(elv).split("_")[2].split(".")[0]
        print(selv)
        writer.writerow([name,arts,getbpm,sgen,sslv,snlv,shlv,selv,"0"])
    except Exception as e:
        print("none")
        writer.writerow([name,arts,getbpm,sgen,sslv,snlv,shlv,"","0"])
f.close()
txt.close()
