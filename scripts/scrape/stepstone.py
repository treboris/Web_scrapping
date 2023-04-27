from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from modules.Data import Save
from tqdm import tqdm
import modules.tools as tools
import requests

initial = tools.initial()
exists = tools.f_exists('stepstone',initial)

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)
date = datetime.today().strftime('%Y-%m-%d')

id = []
corp = []
main = []
location = []
href = []
datee =[]

def page_number():
    url = (f"https://www.stepstone.de/work/it?page=1&fdl=en")
    driver.get(url)
    number = driver.find_element(By.XPATH,f"/html/body/div[4]/div[1]/div/div/div[2]/div/div[2]/div[3]/div/nav/ul/li[8]/a/span/span/span")
    return int(number.text)

def conn(limit):
    url = (f"https://www.stepstone.de/work/it?page={limit}&fdl=en")
    return driver.get(url)

#WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "q")))
#REKURZIV FUGGVENY
def scrape(x):
    article = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'/html/body/div[4]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]')))
    href_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/h2/a')
    to_str = href_tag.get_attribute('href')
    href.append(to_str)
    main_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/h2/a/div/div/div')
    main.append(main_tag.text)
    corp_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[2]/span')
    corp.append(corp_tag.text)
    location_tag = article.find_element(By.XPATH,f'/html/body/div[4]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div/div/article[{x}]/div[1]/div[3]/div[1]/div[1]/span/span')
    location.append(location_tag.text)


testnum = 20
for limit in tqdm(range(1,testnum)):
    conn(limit)
    time.sleep(2)
    for x in range(1,26):
        scrape(x)

driver.quit()

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)

save_data = Save('stepstone',f'stepstone{initial}' ,('ID' , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp), ("Href" , href),('Date' , datee) )
print('\a')
