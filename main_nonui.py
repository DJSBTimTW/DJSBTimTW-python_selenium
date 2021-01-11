import musicbs4,appbs4,sqlcon,userinfo,os,platform,sys,time,appbs4_th

def screenclear():
    osver=platform.system()
    if (osver=='Linux' or osver=='Darwin'):
        os.system("clear")
    elif osver=='Windows':
        os.system("cls")

print("")
screenclear()
print("--------------------------\ngroove coaster資料抓取\nVer:1.0\n--------------------------\n輸入u:抓取玩家資料\n輸入p:抓取玩家遊玩資料\n輸入mu:抓取歌曲資料\n輸入mui:輸入URL抓取歌曲資料\n輸入q:退出\n--------------------------\n")
typein = input('請輸入:').strip()
while typein != 'q':
    if typein == 'u':
        screenclear()
        cidtype = str(input("CID:")).strip()
        pwrtype = str(input("PWR:")).strip()
        userinfo.getinfo(cidtype,pwrtype)
        screenclear()
    elif typein == 'p':
        screenclear()
        cidtype = str(input("CID:")).strip()
        pwrtype = str(input("PWR:")).strip()
        appbs4.playdata(cidtype,pwrtype)
        screenclear()
    elif typein == 'mu':
        screenclear()
        musicbs4.getmusicurl()
        musicbs4.getmusicbs4("0")
        screenclear()
    elif typein == 'mui':
        screenclear()
        ty = str(input("請輸入URL:")).strip()
        getmusicbs4(ty,'')
        screenclear()
    elif typein == 'q':
        sys.exit()
    elif typein == 't':
        screenclear()
        cidtype = str(input("CID:")).strip()
        pwrtype = str(input("PWR:")).strip()
        appbs4_th.playdata(cidtype,pwrtype)
    else:
        screenclear()
        print("輸入錯誤")
        time.sleep(1)
        screenclear()
    print("--------------------------\ngroove coaster資料抓取\nVer:1.0\n--------------------------\n輸入u:抓取玩家資料\n輸入p:抓取玩家遊玩資料\n輸入mu:抓取歌曲資料\n輸入mui:輸入URL抓取歌曲\n輸入q:退出\n--------------------------\n")
    typein = input('請輸入:').strip()

