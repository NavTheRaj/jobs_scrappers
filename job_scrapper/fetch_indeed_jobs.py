import requests
from bs4 import BeautifulSoup

print("********************Welcome to the job finder in console mode********************\n")

job = input("Type the job you want :")

loc = input("\nType you preferable location :")

job = job.replace(" ","+").lower()

URL = f'https://www.indeed.com/jobs?q={job}&l={loc}'

page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')

results = soup.find('td', id='resultsCol')

job_elems = results.find_all(class_='jobsearch-SerpJobCard')

print("\n*****************Your Job Feeds**********************\n")
if job_elems:
    for job in job_elems:
        title = job.find('h2',class_='title')
        company = job.find('span',class_='company')
        print("Job Title : "+title.text.strip())
        print("Company Name : "+company.text.strip())
        print("------------------------\n")









