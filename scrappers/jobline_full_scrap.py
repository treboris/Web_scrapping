from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests

start_time = time.time()

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)

nov = 1

url = (f"https://jobline.hu/allasok/it_telekommunikacio-teljes_munkaido?p={nov}")
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,"html.parser")


links  = soup.find("h2",class_='job-title')


for l in links.children:
    print(l)
#href = links.find_all("a",href=True)

#for h in href:
#    print(h['href'])




driver.close()


print("--- %s seconds ---" % (time.time() - start_time))
