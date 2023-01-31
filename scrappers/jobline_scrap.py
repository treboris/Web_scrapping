from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
import requests
from Data import Save

print("JOBLINE-scrapper STARTED")
start_time = time.time()

#BF-EL CSAK A DOM VEGET JELENITI MEG szoval marad a SELENIUM
options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)

####################################JOBLINE#####################################
#CSAK A HIRDETES CIMET AZ ALCIMKEKET ES A CEG NEVET HELYSZINT SCRAPPELI
corp = []
main = []
labels = []

#PAGE COUNTER
url = (f"https://jobline.hu/allasok/it_telekommunikacio-teljes_munkaido?p=1")
page = requests.get(url)
soup_number = BeautifulSoup(page.text,"html.parser")
page_number = soup_number.find('h4', class_='align_center')
string_split = (page_number.text).split()
max_page_number = round(int(string_split[0])/20)
print(f"Jobs: {string_split[0]}")
print(f"Pages to scrap: {max_page_number}")


nov = 1
while nov < max_page_number:
    url = (f"https://jobline.hu/allasok/it_telekommunikacio-teljes_munkaido?p={nov}")
    driver.get(url)

    html = driver.page_source

    soup = BeautifulSoup(html,"html.parser")
    main_tag = soup.find_all('div',class_='job-main')
    corp_tag = soup.find_all('div',class_='job-info')
    #labels_tag = soup.find_all('div',class_='job-labels')

    #AZERT KELL KIVENNI A SORTORESEKET MERT A KOMPLETT DIV-ET KEREM LE, MERT NEM MINDEN KULON TAG-NAK VAN CLASS ATTRIBUTUMA
    #ES NEHOL MIKOR VISSZAKEREM A .TEXT AKKOR A BF4 AZ EGESSZET ADJA VISSZA A TOBBI TAGGEL EGYUTT,

    for x in soup.find_all('div',class_="job-labels"):
        splitted = x.text.split('\n')
        for s in splitted:
            if (s == ''):
                splitted.remove(s)
                joined = ';'.join(splitted)
        labels.append(joined)
        #splitted.clear()

    for c in corp_tag:
        c_ = c.text.replace("\n","")
        corp.append(c_)

    for m in main_tag:
        m_ = m.text.replace("\n","")
        main.append(m_)

    nov += 1
driver.quit()

#DATA-SAVE

save_data = Save(f'Jobline' , ("Corporation" , corp) , ("Main" , main) , ("Labels" , labels))




################################################################################

print("--- %s seconds ---" % (time.time() - start_time))
