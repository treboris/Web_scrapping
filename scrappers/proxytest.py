import requests
from pandas import *
import concurrent.futures



proxieslist = []



data = read_csv('proxylist.csv',sep=';')
ip = data['IP'].tolist()
port = data['PORT']

for y in range(len(port)):
    new_ip = ip[y] + ':' + str(port[y])
    proxieslist.append(new_ip)

def extract(proxy):
    try:
        r = requests.get('https://www.stepstone.de/work/it?page=1&fdl=en', proxies = {'http' : proxy , 'https' : proxy} , timeout = 2)
        print(r.json(),' - working')
    except:
        print("Not working....")
    return proxy




with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(extract,proxieslist)
