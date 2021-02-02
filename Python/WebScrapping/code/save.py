import csv

#CSV(Comma Seperated Values)생성

def save_to_file(jobs):
  # 파일open시 모드 지정 가능
  # 읽기, 쓰기, 읽기전용, 쓰기전용 등
  # 현재 적용한 w모드는 실행할때마다  기존내용으로 초기화 및 쓰기 가능
  file = open("jobs.csv", mode="w")

  # csv 파일 작성
  writer = csv.writer(file) # (오픈한 파일에 csv 작성)
  writer.writerow(["title", "company", "location", "link"]) # 구분자(헤더)

  for job in jobs:
    # dictionary의 key값 제외 values 값만 가져와 list로 변형
    writer.writerow(list(job.values()))
   



  print("============> csv 파일 생성 완료!")
  return
