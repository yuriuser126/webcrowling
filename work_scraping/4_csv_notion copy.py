import requests
import csv
from bs4 import BeautifulSoup

url = "https://www.notion.so/17c35a8e2881802bbd86fc6ebf1cef5b"

filename = "노션 단축키_05.csv"

f =open(filename,"w",encoding="utf-8-sig")
writer = csv.writer(f)

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"html.parser")

data_rows = soup.find("div",attrs={"class":"notranslate"})

for row in data_rows :
    columns = row.find_all("div")
    if len(columns) ==1: 
        continue
    data = [column.get_text().strip() for column in columns]
    writer.writerow(data)