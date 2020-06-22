import requests
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"

page = requests.get(url)

bs = BeautifulSoup(page.content,'html.parser')

for sibling in bs.find('table',{'id':'giftList'}).tr.next_siblings:
    print(sibling)
