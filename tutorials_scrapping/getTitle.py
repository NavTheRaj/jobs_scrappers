from urllib.request import urlopen
from urllib.request import urlopen
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bs = BeautifulSoup(html.read(),'html5lib')
        title = bs.title
    except AttributeError as e:
        print(e)
        return None

def get_input():
    web_name = input("Please type in the web name for its title:\n")
    web_name = "https://www."+web_name+".com"
    return web_name

def main():
    title = getTitle(get_input())
    print("Searching...")
    if title == None:
        print("Title could not be found")
    else:
        print(title)
main()
