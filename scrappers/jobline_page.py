from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
import pandas as pd
import requests
import time
import os


print("JOBLINE-scrapper STARTED")

text = ""
date = datetime.today().strftime('%Y-%m-%d')
data = pd.read_csv('data/Jobline_2023-02-10.csv')


id = data['ID']
href = data['Href']
for i in id:
    print(i)

for url_piece in href:
    url = (f"https://jobline.hu{url_piece}")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    full_page = soup.body




exists = os.path.exists(f"txt/jobline_job_{date}.txt")

if exists:
    print("File has already exists.")
else:
    with open(f"txt/temp.txt" , "w") as f: #read&write
        f.write(full_page.text)
        f.close()
    with open(f"txt/temp.txt" , "r") as f:
        for line in f:
            if(line.strip()):
                text += line
    with open(f"txt/jobline_job_{date}.txt" , "w") as fil:
        fil.write(text)

os.remove("txt/temp.txt")
