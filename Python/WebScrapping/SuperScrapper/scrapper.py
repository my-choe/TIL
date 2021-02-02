import requests
from bs4 import BeautifulSoup

## 이전에 만들었던 stackoverflow 그대로 복사해서 하드 키워드 -> 변수로 수정

def get_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_pages = pages[-2].get_text(
        strip=True)  # 마지막값 가져오기 -1 하면 next가 가져와짐. strip으로 공백 제거
    return int(last_pages)


def extract_job(html):
    # 1. 구인분야
    title = html.find("h2", {"class": "fs-body3"}).find("a")["title"]

    # 2. fc-black-700 fs-body1 mb4라는 클래스 안에 회사 이름, 지역이 들어있음
    # 순서를 알고 있으니 각각 변수에 담아줌
    company, location = html.find("h3", {
        "class": "mb4"
    }).find_all("span", recursive=False)
    # recursive: span안에 span은 가져 오지 않게 함. 첫번째 요소만 가져오기(깊게 들어가지 않음)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)

    # 지원아이디
    job_id = html["data-jobid"]
    return {
        "title": title,
        "company": company,
        "location": location,
        "apply_link": f"https://stackoverflow.com/jobs/{job_id}"
    }


def extract_jobs(last_page, URL):
    jobs = []
    for page in range(last_page):
      print(f"[Scrapping Stackoverflow] Page: {page}")
      result = requests.get(f"{URL}&pg={page+1}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("div", {"class": "-job"})
      for result in results:
          job = extract_job(result)
          jobs.append(job)
      return jobs


def get_jobs(word):
  URL = f"https://stackoverflow.com/jobs?q={word}&sort=i"
  last_page = get_last_page(URL)
  jobs = extract_jobs(last_page, URL)
  return jobs
