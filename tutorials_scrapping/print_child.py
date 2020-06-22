import requests
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"

page = requests.get(url)

bs = BeautifulSoup(page.content,'html.parser')

for child in bs.find('table',{'id':'giftList'}).children:
    print(child)
