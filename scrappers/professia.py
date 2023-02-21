from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
import requests
import time


print("PROFESSIA.SK-scrapper STARTED")
start_time = time.time()
date = datetime.today().strftime('%Y-%m-%d')
options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)



limit_txt = "?page_num="
limit = 1



id = []
corp = []
main = []
location = []
href = []
salary = []
datee =[]


def page_number():
    url = (f"https://www.profesia.sk/praca/programator/{limit_txt}{limit}")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    number = soup.find('div',class_='offer-counter text-right bold')
    splitted = number.text.split()
    return(int(splitted[-1]))



def conn(limit_txt,limit):
    url = (f"https://www.profesia.sk/praca/programator/{limit_txt}{limit}")
    driver.get(url)
    html = driver.page_source
    page = requests.get(url)
    soup = BeautifulSoup(html,"html.parser")
    return soup

page = round(int(page_number()/20))



while(limit < page):

    main_block = conn(limit_txt,limit).find('ul', class_='list')
    for li in main_block.find_all('li',class_='list-row'):
        for h2 in li.find_all('h2'):
            for a in h2.find_all('a'):
                href.append(a.get('href'))
        for title in li.find_all('span',class_='title'):
            main.append(title.text)
        for loc in li.find_all('span',class_='job-location'):
            location.append(loc.text)
        for corporation in li.find_all('span',class_='employer'):
            corp.append(corporation.text)

    for x in range(1,21):
        try:
            label = driver.find_element(By.XPATH,f"//*[@id='content']/div/div/main/div/ul/li[{x}]/span[3]")
            splitted = (label.text).split()
            if('Od' in splitted):
                splitted.remove('Od')
            if('Можливість' in splitted):
                splitted.remove('Можливість')
                splitted.remove('для')
                splitted.remove('людей')
                splitted.remove('України')
            if('Reagujte' in splitted):
                splitted.remove('Reagujte')
                splitted.remove('bez')
                splitted.remove('životopisu')
            if('Ponuka' in splitted):
                splitted.remove('Ponuka')
                splitted.remove('onedlho')
                splitted.remove('končí!')
            if('з' in splitted):
                splitted.remove('з')
            salary.append(" ".join(splitted))
        except (NoSuchElementException):
            salary.append(None)

    limit += 1

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)






save_data = Save(f'Professia_{date}' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp),("Salary" , salary) , ("Href" , href),("Date" , datee) )



print("--- %s seconds ---" % (time.time() - start_time))
