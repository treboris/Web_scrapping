from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import time
import requests

print("Script STARTED")
start_time = time.time()


#BF-EL CSAK A DOM VEGET JELENITI MEG szoval marad a SELENIUM
options = Options()
options.headless = True



driver = webdriver.Firefox(options = options)


####################################CVONLINE#####################################

#CSAK A HIRDETES CIMET AZ ALCIMKEKET ES A CEG NEVET HELYSZINT SCRAPPELI

upload_date = []
corp = []
main = []
labels = []
location = []



#PAGE COUNTER
url = (f"https://www.cvonline.hu/hu/allashirdetesek/it-informatika-0")
page = requests.get(url)
soup_number = BeautifulSoup(page.text,"html.parser")
page_number = soup_number.find('h1', class_='search-result-header')
string_split = (page_number.text).split()
max_page_number = round(int(string_split[0])/20)
print(f"Jobs: {string_split[0]}")
print(f"Pages to scrap: {max_page_number}")



#SCRAP SCRIPT
i = 0
while i < max_page_number:
    url = (f"https://www.cvonline.hu/hu/allashirdetesek/it-informatika-0?page={i}")
    driver.get(url)
    html = driver.page_source

    soup = BeautifulSoup(html,"html.parser")
    main_tag = soup.find_all("h2", class_='node__title')

    corp_tag = soup.find_all('div', class_="description")
    del corp_tag[0]

    labels_tag = soup.find_all('div', class_='terms')

    location_tag = soup.find_all('div',class_ = 'location')



    for m in main_tag:
        m_ = m.text.replace("\n","")
        main.append(m_)

    #CORP TAG AND DATE
    for c in corp_tag:
        splitted = (c.text).split()
        upload_date.append(splitted.pop(0))
        corp_text = ""
        for split in splitted:
            corp_text += split
            corp_text += " "
        corp.append(corp_text)

    for labels in labels_tag:
        lab = (labels.text).split()
        for la in lab:
            if(la == '/') or (la == '|'):
                lab.remove(la)
        #labels.append(lab)

    for l in location_tag:
        l_ = l.text.replace("\n","")
        location.append(l_)

    i += 1
driver.quit()
################################################################################
#LOG

#DATA-SAVE

def data_save():



log_file = open("scrapLOG.txt", "a" )
log_file.write(f"Cv online")
log_file.write(f"\nScrapping was Successful.\nDate: {date.today()}")
log_file.write(f"\nExecution time: {time.time() - start_time}\n")
log_file.close()



print("Execution time: %s seconds ---" % (time.time() - start_time))
