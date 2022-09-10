from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
browser = webdriver.Chrome(options=options)

def get_page_count(keyword):
  base_url = 'https://kr.indeed.com/jobs?q='
  browser.get(f"{base_url}{keyword}")

  soup =BeautifulSoup(browser.page_source,'html.parser')
  pagination = soup.find("ul", class_="pagination-list")
  if pagenation == None:
    return 1
  pages = pagination.find_all("li", reqursive = False)
  print(len(pages))

get_page_count("nest")

def extract_indeed_jobs(keword):
  base_url = 'https://kr.indeed.com/jobs?q='
  browser.get(f"{base_url}{keyword}")
  
  results = []
  soup =BeautifulSoup(browser.page_source,'html.parser')
  job_list = soup.find("ul",class_="jobsearch-ResultsList")
  jobs = job_list.find_all("li",recursive=False)
  for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
      anchor = job.select_one("h2 a")
      title = anchor['aria-label']
      link = anchor['href']
      company = job.find("span",class_="companyName")
      location = job.find("div",class_="companyLocation")
      job_data = {
        'link':f"https://kr.indeed.com{link}",
        'company':company.string,
        'location':location.string,
        'position':title
      }
      results.append(job_data)