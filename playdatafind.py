import sqlcon,platform
from pprint import pprint

def screenclear():
    osver=platform.system()
    if (osver=='Linux' and osver=='Darwin'):
        os.system("clear")
    elif osver=='Windows':
        os.system("cls")
screenclear()
cid = input('請輸入CardID')
while cid !='' :
    data = sqlcon.infocheck(cid)
    if data =='not found':
        print("not found")
    elif data =='error':
        print("error")
    else:
        pprint(data)
    cid = input('請輸入CardID')
