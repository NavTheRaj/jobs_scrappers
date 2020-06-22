import requests
from bs4 import BeautifulSoup

print("****** Welcome To Job Hunter Console ******\n")

job = input('Type the job you want: ')

job = job.replace(" ","+")

loc = input("Type your preferable location: ")

URL = f"https://www.indeed.com/jobs?q={job}&l={loc}"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

result = soup.find('td', id='resultsCol')

job_elems = result.find_all(class_='jobsearch-SerpJobCard')

print("*************Your Job Feeds*************\n")

if job_elems:
    for job in job_elems:
        title = job.find('h2',class_='title')
        company = job.find('span',class_='company')
        print("Job Title :" +title.text.strip())
        print("Company : "+company.text.strip())
        print()

else:
    print("Sorry! For this time there is no such jobs ..keep searching!!")















