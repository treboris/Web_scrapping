from bs4 import BeautifulSoup
from datetime import datetime
from Data import Save
from tqdm import tqdm
import requests
import time
import re



id = []
corp = []
main = []
location = []
href = []
salary = []
datee =[]


def page_number(limit):
    url = (f"https://www.stepstone.de/work/it?page={limit}&fdl=en")
    req = requests.get(url)
    print(req)
    req.add_header('user-agent', 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20')
    client = urlopen(req)
    page = client.read()
    client.close()
    soup = BeautifulSoup(page.text,"html.parser")
    number = soup.find('span',class_='resultlist-kyg8or')
    return int(number.text)




def conn(limit):
    url = (f"https://www.stepstone.de/work/it?fdl=en&ef_id=CjwKCAiAu5agBhBzEiwAdiR5tFCjdCV5GMeemaFH0B4oY8eWT9AQtOLoAL31j5nd3GHmf8QALqqevRoCKXIQAvD_BwE:G:s&cid=SEA_GO_DE-EN-DIS002-GEN-ARE-P%7C%5BA%5D_c_it-jobs-abroad%7CCHLD0313-GEN001-ARE06_it%20job%20abroad_RL_RSA3&loc_interest=&loc_physical=1012130&s_kwcid=AL!523!3!624638611154!p!!g!!it%20job%20abroad")
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser')
    return soup




print(page_number(1))
