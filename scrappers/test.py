from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import time
import requests
import re

print("STARTED")
start_time = time.time()

options = Options()
#options.headless = True


print("driver = webdriver")
driver = webdriver.Firefox()
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")



url = (f"https://www.cvonline.hu/hu/allashirdetesek/it-informatika-0?page=1")
print("driver.get(url)")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html,"html.parser")
print("DRIVER CLOSED")
driver.close()

print("Execution time: %s seconds ---" % (time.time() - start_time))
