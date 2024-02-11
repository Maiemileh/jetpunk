import requests
from bs4 import BeautifulSoup

url = 'https://www.jetpunk.com/user-quizzes'

# Get the webpage
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# Find the table from the page
results = soup.find('table', class_='super-table')

# Get the rows of the table
rows = results.find_all('tr')

# Print the information from rows with users
for row in rows:
    infos = row.find_all('td')
    if len(infos) == 5:
        print(infos[0].find(string=True), infos[1].find(string=True), infos[2].find(string=True), "quizzes, out of which", infos[3].find(string=True), "featured. Takes:", infos[4].find(string=True))





