# https://kr.indeed.com/ 사이트에서 python 구인공고 스크래핑하기
# 직업명, 회사명, 회사위치, 지원url 스크래핑

import requests
from bs4 import BeautifulSoup
# python 기본 라이브러리인 urllib을 사용할 수도 있지만 더 강력한 온라인 라이브러리인 requests를 사용
# requests : 파이썬에서 요청을 만드는 기능을 모아놓은 것
# repl.it 에서는 packages에서 reuqests: Python HTTP for Humans. 를 설치하여 사용할 수 있음

LIMIT = 50
URL = "https://www.indeed.com/jobs?as_and=python&limit={LIMIT}}"
def extract_indeed_pages():
  # indeed 스크래핑
  result = requests.get(URL)

  # beautifulsoup4를 이용해 페이징 정보 추출(.text는 html 다 가져오는 역할)
  soup = BeautifulSoup(result.text, "html.parser")

  #div의 class명이 pagination인 값 가져오기
  pagination = soup.find("div", {"class":"pagination"})

  # anchor찾기
  links = pagination.find_all('a')

  # anchor 안의 String을 가져와 integer로 변환
  pages = []
  for link in links[:-1]: # 마지막 'next' 제외
    pages.append(int(link.string))
  max_page = pages[-1] # 마지막 페이지
  return max_page

def extract_job(html):
  # 직업
  title = html.find("h2",{"class":"title"}).find("a")["title"]

  # 회사
  company = html.find("span",{"class":"company"})
  company_anchor = company.find("a")
  if company_anchor is not None:
    company = str(company_anchor.string)
  else:
    company = str(company.string)
  company = company.strip() # 양옆에 있는 공백 제거

  # 지역
  location = html.find("div",{"class":"recJobLoc"})["data-rc-loc"]

  # 직업 아이디
  job_id = html["data-jk"]
  
  
  return {"title" : title, "company": company, "location": location, "link":f"https://www.indeed.com/viewjob?jk={job_id}"}




# 직업 추출 함수
def extract_indeed_jobs(last_page):
  jobs = []
  for page in range(last_page):
    print(f"Scrapping page {page}")
    result = requests.get(f"{URL}&start={page*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("div", {"class":"jobsearch-SerpJobCard"})
    for result in results:
      job = extract_job(result)
      jobs.append(job)
  return jobs
