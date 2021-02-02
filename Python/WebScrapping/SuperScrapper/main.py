from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SupperScrapper")

# fakeDB 생성
db = {}


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs  #DB 조회 결과 넘겨줌
        else:
            jobs = get_jobs(word)
            db[word] = jobs  #DB 저장 역할
    else:
        return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultNumber=len(jobs),
                           jobs=jobs)


# csv 파일 저장
@app.route("/export")
def export():
  try:
    word = request.args.get('word').lower()
    if not word:
      raise Exception()
    jobs = db.get(word)
    if not jobs:
      raise Exception()
    save_to_file(jobs)
    return send_file("jobs.csv")
  except:
    return redirect("/")
  
      


@app.route("/<username>")
def contact(username):
    return f"Hello {username}! How are you?"


app.run(host="0.0.0.0", port=8080)
