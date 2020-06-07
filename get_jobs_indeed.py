import re
import requests
from pprint import pprint
from bs4 import BeautifulSoup

print("Welcome\n Search Your Preferred Job and Get One from Indeed.com\n")

job_str = input("Type a job that you want: ")

job_elem = job_str.lower()

print("Searching job for",job_str,".....")

URL = 'https://www.indeed.com/jobs?q=software%20engineer&l=USA&vjk=20a30344f3ebc4db'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('td', id='resultsCol')

job_elems = results.find_all(class_='jobsearch-SerpJobCard')

for job_elem in job_elems:
    raw_link = job_elem.find('a')['href']
    pre_raw_link = raw_link.replace("/rc/clk","https://www.indeed.com/viewjob")
    link = re.sub('&[^>]+&', '&from=serp&', pre_raw_link)

    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('span', class_='company')
    location_elem = job_elem.find('span', class_='location')
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print(f"Apply here: {link}\n")
    print()

#print(results.prettify())

#python_jobs = results.find_all('h2',string=lambda text:job_elem in text.lower())

'''
if python_jobs:
    for p_job in python_jobs:
        link = p_job.find('a')['href']
        print(p_job.text.strip())
        print(f"Apply here: {link}\n")
else:
    print("Sorry! At the mean time, we have no job for",job_str)
    print("Keep on Searching You will get it!!")
    '''
