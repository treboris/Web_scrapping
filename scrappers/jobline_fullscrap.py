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

full_page = soup.body

try:
    exists = os.path.exists(f"jobline_job_{number}_{date}.txt")
    print(exists)
    with open(f"txt/jobline_job_{number}_{date}.txt", "w") as file:
        file.write(full_page.text.strip('\t\r\n'))

except Exception as e:
    raise FileExistsError("File already exists.")
