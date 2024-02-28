import requests
from bs4 import BeautifulSoup

# TODO: empty the text files HERE

langs = ["de", "es", "fr", "it", "nl", "pl", "pt", "fi", "ar", "bg", "cz", "dk", "ee", 
         "el", "hr", "hu", "jp", "no", "ru", "sr", "se", "te", "tr", "ve", "cn"]

for lang in langs:
    userid_dict = {}
    usernames_dict = {}
    for i in range(1000):
        index = i+1

        # Construct the URL
        url = 'https://www.jetpunk.com/' + lang + '/all/' + str(index)

        # URL is different on the first page
        if index == 1:
            url = 'https://www.jetpunk.com/' + lang + '/all'
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        # Find the main table
        results = soup.find('table', class_='super-table')

        try:
            rows = results.find_all('tr')
            for row in rows:
                infos = row.find_all('td')
                if len(infos) >= 2:

                    second_td = infos[1]
                    a_element_link = second_td.find_all('a', href=True)

                    for link in a_element_link:

                        split_link = link['href'].split("/")

                        # Increase the number in the dictionary by one
                        try:
                            userid_dict[split_link[2]] = userid_dict[split_link[2]] + 1
                        except:
                            userid_dict[split_link[2]] = 1
                            # Find the username
                            full_link = 'https://www.jetpunk.com' + link['href']
                            r2 = requests.get(full_link)
                            soup2 = BeautifulSoup(r2.content, "html.parser")
                            results2 = soup2.find('div', class_='screen-holder')
                            spans = results2.find_all('span')
                            usernames_dict[split_link[2]] = spans[1].find(string=True)

        except:
            break

    # Sort based on the number of quizzes
    sorted_dict = sorted(userid_dict.items(), key=lambda x:x[1], reverse=True)

    # Save the results in a text file
    for t in sorted_dict:
        filename = lang + ".txt"
        results_file = open(filename, 'a')
        results_file.write(usernames_dict[t[0]] + " " + str(t[1]) + "\n")
        results_file.close()


    
