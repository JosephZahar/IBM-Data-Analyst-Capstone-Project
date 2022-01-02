from bs4 import BeautifulSoup
import requests
import csv

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/Programming_Languages.html"
data = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")

table = soup.find('table')
with open('popular-languages.csv', 'a') as writeFile:
    writer = csv.writer(writeFile)
    for row in table.find_all('tr'):
        cols = row.find_all('td')
        language_name = cols[1].getText()
        annual_average_salary = cols[3].getText()
        writer.writerow([language_name, annual_average_salary])
        