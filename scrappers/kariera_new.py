from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from tqdm import tqdm
from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
import requests

print("KARIERA.sk-scrapper STARTED")
date = datetime.today().strftime('%Y-%m-%d')

#DATA
id = []
corp = []
main = []
location = []
href = []
salary = []
datee =[]

#CONNECTION
def conn(limit_txt,limit):
    url = (f"https://kariera.zoznam.sk/pracovne-ponuky/informatika-software{limit_txt}{limit}")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    return soup


#GET-PAGE-NUMBER
def page_number():
    url = (f"https://kariera.zoznam.sk/pracovne-ponuky/informatika-software")
    page = requests.get(url)
    page_num = BeautifulSoup(page.text,"html.parser")
    div = page_num.find('div',class_= 'offer-list-content')
    h1 = div.find('sup').text.replace('(','').replace(')','')
    return(int(h1))

pages = round(page_number() / 30)
paginator = 0
limit_txt = "?od="
for limit in tqdm(range(pages)):

    fblock = conn(limit_txt,paginator).find('div' , class_= 'offer-list')
    for div1 in fblock.find_all('div' , class_= 'offer'):
        #MAIN
        for h2 in div1.find_all('h2' , class_= 'offer-title'):
            for a in h2.find_all('a'):
                href.append(a.get('href'))
            main.append(h2.text)
        #Corporation
        for div2 in div1.find_all('div', class_ = 'offer-employer'):
            corp.append(div2.text)
            #LOCATION
            try:
                for div3 in div1.find('div', class_= 'offer-locality'):
                    location.append(div3.text)
            except (AttributeError,TypeError):
                location.append(None)
            #SALARY
            try:
                for div4 in div1.find('div' , class_= 'offer-bottom-left'):

                    if (div4.text == '\n'):
                        pass
                    else:
                        salary.append((div4.text).replace('od',''))
            except (AttributeError,TypeError):
                location.append(None)

    paginator += 30

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)

save_data = Save(f'kariera1' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp),("Salary" , salary) , ("Href" , href),("Date" , datee) )