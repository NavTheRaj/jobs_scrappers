import requests
from bs4 import BeautifulSoup
import re

url = "https://en.wikipedia.org/wiki/Rajneesh"
page = requests.get(url)
bs = BeautifulSoup(page.content,'html.parser')
for link in bs.find('div',{'id':'bodyContent'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])
