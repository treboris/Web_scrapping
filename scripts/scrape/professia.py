from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup ,NavigableString
from datetime import datetime
from modules.Data import Save
import modules.tools as tools
from tqdm import tqdm
import requests

initial = tools.initial()
exists = tools.f_exists('professia',initial)
date = datetime.today().strftime('%Y-%m-%d')

options = Options()
options.headless = True
driver = webdriver.Firefox(options = options)

limit_txt = "?page_num="
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

limit = 1
def conn(limit_txt,limit):
    url = (f"https://www.profesia.sk/praca/programator/{limit_txt}{limit}")
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,"html.parser")
    return soup

page = round(float(page_number()/20))

for limit in tqdm(range(0,page)):

    main_block = conn(limit_txt,limit).find('ul', class_='list')

    for li in main_block.select('.list-row:has(div)'):
        for h2 in li.find_all('h2'):
            for a in h2.find_all('a'):
                href.append(a.get('href'))
        for title in li.find_all('span',class_='title'):
            main.append(title.text)
        try:
            for loc in li.find_all('span',class_='job-location'):
                location.append(loc.text)
        except (AttributeError,TypeError):
                location.append("None")
        for corporation in li.find_all('span',class_='employer'):
            corp.append(corporation.text)
    labels = main_block.find_all('li',class_='list-row')
    if (len(labels) ==21):
        del labels[1]
    for l in labels:
        try:
            for sal in l.find('span',class_='label-group'):
                if(isinstance(sal,NavigableString)):
                    pass
                else:
                    splitted = sal.text.split()
                    if('Kč/mesiac' in splitted):
                        raise AttributeError
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
                    if('Zabezpečená' in splitted):
                        splitted.remove('Zabezpečená')
                    if('doprava' in splitted):
                        splitted.remove('doprava')
                    if('ubytovanie' in splitted):
                        splitted.remove('ubytovanie')
                    salary.append(' '.join(splitted).strip())
        except(AttributeError,TypeError):
            salary.append('None')
driver.quit()

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)

new_salary = []
for x in salary:
    if(x != ''):
        new_salary.append(x)
    else:
        pass

num = int(len(new_salary) - len(main))
del new_salary[-num:]
save_data = Save('professia',f'professia{initial}' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp),("Salary" , new_salary) , ("Href" , href),("Date" , datee) )
print('\a')
