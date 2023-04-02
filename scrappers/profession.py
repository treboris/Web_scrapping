from bs4 import BeautifulSoup
from datetime import date
from Data import Save
from datetime import datetime

from tqdm import tqdm
import pandas as pd
import requests
import time
import re

date = datetime.today().strftime('%Y-%m-%d')

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
    tmp = 0
    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    for card_body in fblock.find_all('div', class_='card-body-header-company'):
        #MAIN-HREF
        for h2 in card_body.find_all('h2'):
            if(tmp1 < 2):
                pass
            else:
                strip = h2.text.strip()
                strip = re.sub('\n',"",strip)
                main.append(strip)
            tmp1 += 1

            for a in h2.find_all('a'):
                if(tmp <2):
                    pass
                else:
                    href.append(a.get('href'))
            tmp += 1
        #CORPORATION
        for div in card_body.find_all('a' , class_='link-icon'):
            if(tmp2 <2):
                pass
            else:
                strip = div.text.strip()
                strip = re.sub('\n',"",strip)
                corp.append(strip)
        tmp2 += 1

        #LOCATION - itt ott van a html elem de ''-kent itt nem jo a try/catch megoldas
        for span in card_body.find_all('span'):
            if(tmp3 < 2):
                pass
            else:
                if(span.get('title') == None):
                    pass
                else:
                    strip = span.get('title').strip()
                    if(strip == ''):
                        location.append(None)
                    else:
                        strip = re.sub('\n',"",strip)
                        if(strip == '' or strip == 'Legyen az első 5 jelentkező között!'):
                            pass
                        else:
                            location.append(strip)
        tmp3 += 1
#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)

save_data = Save(f'profession1' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp) , ("Href" , href),("Date" , datee) )

print("--- %s seconds ---" % (time.time() - start_time))
