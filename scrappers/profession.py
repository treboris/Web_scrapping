from bs4 import BeautifulSoup
from datetime import date
from tqdm import tqdm

import pandas as pd
import time
import requests

print("Script STARTED")
start_time = time.time()




#DATA
id = []
corp = []
main = []
location = []
href = []
datee =[]


#PAGE COUNTER
def page_number():
    url = (f"https://www.profession.hu/allasok/1,10_25,0,0,200_201_393_448_75_76_202_363_450_80_449_69_338_72_70_365_77_73_79_78")
    page = requests.get(url)
    soup_number = BeautifulSoup(page.text,"html.parser")
    page_number = soup_number.find(id='jobs_block_count')
    string_split = (page_number.text).split()
    return round(int(string_split[0])/20)



def conn(limit):
    url = (f"https://www.profession.hu/allasok/{limit},10_25,0,0,200_201_393_448_75_76_202_363_450_80_449_69_338_72_70_365_77_73_79_78")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    return soup




for limit in tqdm(range(1,page_number())):
    fblock = conn(limit).find('ul',class_='job-cards')
    for card_body in fblock.find_all('div', class_='card-body'):
        print(card_body.text)



#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)
