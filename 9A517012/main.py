import requests
import bs4

url ="https://irw.ncut.edu.tw/peterju/course/scripting/1091/index.html"
html = requests.get(url)
html.encoding = 'utf-8'
soup = bs4.BeautifulSoup(html.text, 'html.parser')

print("抓取檔尾文字:")
findget = soup.find("div",class_="copyright").div.find('p').text
findallget = soup.find("div",class_="copyright").div.find_all('p')[0].text
selectget = soup.select("body > div.copyright > div > p")[0].text
selectoneget = soup.select_one("body > div.copyright > div > p").text
print("find方法:{}".format(findget))
print("find_all方法:{}".format(findallget))
print("select_one方法:{}".format(selectoneget))
print("select方法:{}".format(selectget))
print("-------------------\n抓取參考項目並轉為markdown格式")
getdiv = soup.find("div",class_="footer").find("div",class_="col-md-4 twitter").find_all('a')
for i in range(len(getdiv)):
    print("[{}]({})".format(getdiv[i].text,getdiv[i].get('href')))
