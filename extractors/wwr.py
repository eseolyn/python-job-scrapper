from requests import get
from bs4 import BeautifulSoup

def extract_wwr_jobs(keyword):
	base_url = "https://weworkremotely.com/remote-jobs/search?term="
	
	response = get(f"{base_url}{keyword}")
	if response.status_code != 200:
		print("Can't request website")
	else:
		results = []
		soup = BeautifulSoup(response.text,'html.parser')
		jobs = soup.find_all('section', class_='jobs')
		# 각각의 section에서 코드를 실행하기 위해 for loop 사용
		for job_section in jobs:
			job_posts = job_section.find_all('li')
			job_posts.pop(-1) # 마지막 li는 view all 버튼으로 지움
			for post in job_posts:
				anchors = post.find_all('a')
				# 첫번째 로고앵커X, 두번째 주소앵커O
				anchor = anchors[1]
				link = anchor['href']
				#앵커 안 span들에 접근하기 (list의 길이를 알 경우)
				company, kind, region = anchor.find_all('span', class_='company')
				title = anchor.find('span', class_='title')
				job_data = {
          'link': f"https://weworkremotely.com{link}",
				 	'company' : company.string,
					'kind' : kind.string,
					'location' : region.string,
					'position' : title.string
				}
				results.append(job_data)
		return results
