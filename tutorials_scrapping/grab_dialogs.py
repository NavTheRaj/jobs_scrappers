import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page1.html"

page = requests.get(url)
bs = BeautifulSoup(page.content,'html.parser')
namelist = bs.find_all('',{'class':'red'})
print(namelist)
for name in namelist:
    print(name)
