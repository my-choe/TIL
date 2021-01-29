#https://kr.indeed.com/ 사이트에서 python 개발자 구인공고 스크래핑하기
from indeed import extract_indeed_pages, extract_indeed_jobs

last_indeed_pages = extract_indeed_pages()

indeed_jobs = extract_indeed_jobs(last_indeed_pages)

print(indeed_jobs)
