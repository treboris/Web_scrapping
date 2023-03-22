from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from tqdm import tqdm
from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
import requests
import time


print("KARIERA.sk-scrapper STARTED")
start_time = time.time()
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
    div = page_num.find('div',class_='right-content-top')
    for h1 in div.find('h1'):
        splitted = (h1.text).split()
        splitted_1 = (splitted[4].replace('(','')).replace(')','')
        return(int(splitted_1))


pages = round(page_number() / 30)
paginator = 0
limit_txt = "?od="
for limit in tqdm(range(pages)):

    fblock = conn(limit_txt,paginator).find('ul' , class_='search-list')
    for li in fblock.find_all('li' , class_='clearfix'):
        for div in li.find_all('div' , class_='column2'):
            for h2 in div.find_all('h2'):
                main.append(h2.text)
                for a in h2.find_all('a'):
                    href.append(a.get('href'))
            for emp in div.find_all('a' , class_='employer'):
                corp.append(emp.text)
            try:
                for span in div.find('span' , class_='place'):
                    location.append(span.text)
            except (AttributeError,TypeError):
                location.append(None)
        try:
            for span_salary in div.find('span' , class_='salary'):
                splitted = span_salary.text.replace('od','')
                salary.append(splitted)
        except (AttributeError,TypeError):
            salary.append(None)

    paginator += 30

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)






save_data = Save(f'kariera1' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp),("Salary" , salary) , ("Href" , href),("Date" , datee) )

print("--- %s seconds ---" % (time.time() - start_time))
