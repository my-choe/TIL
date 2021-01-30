from indeed import get_jobs as get_indeed_jobs
from stackoverflow import get_jobs as get_so_jobs
from save import save_to_file

indeed_jobs = get_indeed_jobs()
stackoverflow_jobs = get_so_jobs()
jobs = stackoverflow_jobs + indeed_jobs
save_to_file(jobs)
