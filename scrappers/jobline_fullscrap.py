from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
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
url = (f"https://jobline.hu/allas/it_kontroller/XQ-4102#adtype=dirCU")



url = (f"https://jobline.hu{url_piece}")
page = requests.get(url)
soup = BeautifulSoup(page.text,"html.parser")
print(soup.body)




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
