import requests
from openpyxl import Workbook
baseurl = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/datasets/githubposting.json"

def get_number_of_jobs(technology):
    new_list = []
    number_of_jobs = 0
    response = requests.get(baseurl)
    data = response.json()
    tech = data.get('technology')
    jobs = data.get('number of job posting')

    for i in range(len(tech)):
        num = tech.get(str(i))
        if num == technology:
            new_list.append(str(i))

    for string in new_list:
        num = jobs.get(string)
        number_of_jobs = number_of_jobs + int(num)

    return technology, number_of_jobs


technologies = ["C", "C#", "C++", "Java", "JavaScript", "Python", "Scala", "Oracle", "SQL Server", "MySQL Server",
                "PostgreSQL", "MongoDB"]

wb = Workbook()
ws = wb.active

for technology in technologies:
    ws.append(get_number_of_jobs(technology))

wb.save("github-job-postings.xlsx")

