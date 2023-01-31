from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date
from csv import writer
import pandas as pd
import time
import requests

print("Script STARTED")
start_time = time.time()


options = Options()
options.headless = True


driver = webdriver.Firefox(options = options)



####################################PROFESSION#####################################
#CSAK A HIRDETES CIMET AZ ALCIMKEKET ES A CEG NEVET HELYSZINT SCRAPPELI


#feltoltes kerdeses
upload_date = []

corp = []
main = []
location = []
salary = []





i = 0
while i < 10 :
    url = (f"https://www.profesia.sk/praca/?search_anywhere=python&page_num={i}")
    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html,"html.parser")

    main_tag = soup.find_all('span' ,class_='title')
    for m in main_tag:
        main.append(m.text)

    employer_tag = soup.find_all('span' , class_='employer')
    for emp in employer_tag:
            corp.append(emp.text)

    location_tag= soup.find_all('span', class_='job-location')
    for loc in location_tag:
        location.append(loc.text)

    salary_tag = soup.find_all('span' , class_='label-group')
    for sal in salary_tag:
        splitted = (sal.text).split()

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
        if(splitted[-1] == 'з'):
            splitted.remove('з')
        salary.append(" ".join(splitted))

    i += 1

driver.quit()


print(corp[-1])
print(main[-1])
print(location[-1])
print(salary[-1])
data_dict = {"Corporation" : corp ,"Main" : main , "Location" : location , "Salary" : salary }
data_frame = pd.DataFrame(data_dict)

data_frame.to_csv('/data/professia_data.csv', sep=',', encoding='utf-8',index = False)









print("Execution time: %s seconds ---" % (time.time() - start_time))
