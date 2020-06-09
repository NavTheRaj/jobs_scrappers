import requests
from pprint import pprint
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Engineering-Intern&where=USA'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_='card-content')

for job_elem in job_elems:
    title = job_elem.find('h2', class_="title")
    company = job_elem.find('div', class_="company")
    location = job_elem.find('div', class_="location")
    if None in (title,company,location):
        continue
    print(title.text.strip())
    print(company.text.strip())
    print(location.text.strip())
    print("---------------------------\n"*2)
