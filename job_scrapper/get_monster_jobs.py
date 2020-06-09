import requests
from pprint import pprint
from bs4 import BeautifulSoup

print("Welcome\n Search Your Jobs and Get preferred one from Monster.com\n")

job_str = input("Type a job that you want: ")

job_elem = job_str.lower()


URL = 'https://www.monster.com/jobs/search/?q=Software-Engineering-Intern&where=USA'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

python_jobs = results.find_all('h2',string= lambda text: job_elem in text.lower())

if python_jobs:
    for p_job in python_jobs:
        link = p_job.find('a')['href']
        print(p_job.text.strip())
        print(f"Apply here: {link}\n")
else:
    print("Sorry! At the mean time, we have no job for",job_str)
    print("Keep on Searching You will get it!!")
