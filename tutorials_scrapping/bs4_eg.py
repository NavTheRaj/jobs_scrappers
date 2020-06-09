from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

    
url = input("Type the name of web page you want to retrieve:\n")
url = "https://www."+url+".com"
print("Retrieving",url,"....")
try:
    html = urlopen(url)
except HTTPError as e:
    print(e)
except URLError as e:
    print(e)
else:
    bs = BeautifulSoup(html.read(), 'html5lib')
    print(bs.title)


