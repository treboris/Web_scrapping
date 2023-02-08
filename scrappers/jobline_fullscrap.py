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
url = (f"https://jobline.hu/allas/szoftver_fejleszto/LA-4148#adtype=dirOA")
number = 1


options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get(url)

html = driver.page_source

page = requests.get(url)
soup = BeautifulSoup(html,"html.parser")
driver.quit()
full_page = soup.body

exists = os.path.exists(f"txt/jobline_job_{number}_{date}.txt")

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
    with open(f"txt/jobline_job_{number}_{date}.txt" , "w") as fil:
        fil.write(text)

os.remove("txt/temp.txt")
