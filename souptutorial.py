from bs4 import BeautifulSoup
import urllib.request
r = urllib.request.urlopen('http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts')
soup = BeautifulSoup(r,"html.parser")
#print(type(soup))
#print(soup.prettify()[0:1000])
from IPython.display import HTML
HTML('<iframe src=http://www.aflcio.org/Legislation-and-Politics/Legislative-Alerts width=700 height=500></iframe>')
letters = soup.find_all("div", class_="ec_statements")
#print(type(letters))
#print(letters[0])
lobbying = {}
for element in letters:
    lobbying[element.a.get_text()] = {}
prefix = "www.aflcio.org"
for element in letters:
    lobbying[element.a.get_text()]["link"] = prefix + element.a["href"]
for element in letters:
    date = element.find(id="legalert_date").get_text()
    lobbying[element.a.get_text()]["date"] = date
for item in lobbying.keys():
    print(item + ": " + "\n\t" + "link: " + lobbying[item]["link"] + "\n\t" + "date: " + lobbying[item]["date"] + "\n\n")
import json

with open("lobbying.json", "w") as writeJSON:
    json.dump(lobbying, writeJSON)