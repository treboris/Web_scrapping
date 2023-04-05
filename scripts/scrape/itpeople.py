from tqdm import tqdm
from bs4 import BeautifulSoup
from datetime import datetime
from modules.Data import Save
import modules.tools as tools
import requests
import time




initial = tools.initial()
exists = tools.f_exists('itpeople',initial)

date = datetime.today().strftime('%Y-%m-%d')

#DATA
id = []
corp = []
main = []
location = []
href = []
datee =[]

#CONNECTION
def conn(limit):
    url = (f"https://itpeople.hu/allasok/{limit}")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    return soup

#GET-PAGE-NUMBER
def page_number():
    url = (f"https://itpeople.hu/allasok/1")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,"html.parser")
    number = soup.find('div', class_='oldalJelzo')
    split = number.text.split()
    return int(split[-1])

page = page_number() +1

for limit in tqdm(range(1,page)):
    block_frame = conn(limit).find('div', class_='items')
    for h2 in block_frame.find_all('div', class_='cim2'):
        main.append(h2.text)
        for a in h2.find_all('a'):
            href.append(a.get('href'))
    for instructor_title in block_frame.find_all('div', class_='col-12 job-instructor-title'):
        tmp = True
        for span in instructor_title.find_all('span'):
            if (tmp):
                location.append(span.text)
                tmp = False
            else:
                corp.append(span.text)

#ID DATE
list_size = len(main)
for x in range(0, list_size):
    id.append(x)

for y in range(0, list_size):
    datee.append(date)

save_data = Save('itpeople',f'itpeople{initial}' ,("ID" , id), ("Main" , main) ,("Location" , location), ("Corporation" , corp) , ("Href" , href),("Date" , datee) )
