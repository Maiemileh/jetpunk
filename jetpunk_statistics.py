import requests
from bs4 import BeautifulSoup

url = 'https://www.jetpunk.com/user-quizzes'

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

results = soup.find('table', class_='super-table')
	
rows = results.find_all('tr')

for row in rows:
    infos = row.find_all('td')
    if len(infos) == 5:
        print(infos[0].find(string=True), infos[1].find(string=True), infos[2].find(string=True), "quizzes, out of which", infos[3].find(string=True), "featured. Takes:", infos[4].find(string=True))





