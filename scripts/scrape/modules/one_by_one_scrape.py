from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import requests
import time
import os


def size(folder,csv):
    data = pd.read_csv(f'../../../../../data/{folder}/{csv}')
    return (data['ID'].size) -1

def file_write(name,href,id,initial):

    def conn(href):
        try:
            if (name == 'jobline'):
                page = requests.get(f'https://jobline.hu{href}' , timeout = 5)
                soup = BeautifulSoup(page.text,'html.parser')
                return soup.body
            elif(name == 'kariera'):
                page = requests.get(f'https://kariera.zoznam.sk/{href}' , timeout = 5)
                soup = BeautifulSoup(page.text,'html.parser')
                return soup.body
            elif(name == 'professia'):
                page = requests.get(f'https://www.profesia.sk{href}' , timeout = 5)
                soup = BeautifulSoup(page.text,'html.parser')
                return soup.body
            else:
                page = requests.get(f'{href}' , timeout = 5)
                soup = BeautifulSoup(page.text,'html.parser')
                return soup.body
        except requests.exceptions.ConnectionError:
            print('Connection ERROR')
            time.sleep(5)
            conn(href)

        except requests.exceptions.Timeout:
            print('Timeout')
            conn(href)
        except requests.exceptions.TooManyRedirects:
            print("Bad URL")

    cond = False
    text = ''

    #SOUP
    #with open(f'txt/{name}/{initial}/soup/soup{id}.html','w') as f_soup:
    #    f_soup.write(conn(href).prettify())
    with open(f"txt/{name}/{initial}/temp.txt" , "w") as f:
        f.write(conn(href).text)
    with open(f"txt/{name}/{initial}/temp.txt" , "r") as f:

#DATA CLEANING

        if (name == 'jobline'):
            for line in f:
                if(line.strip()):
                    if (' Belépés ›' in line):
                        cond = True
                    if (cond):
                        text += line
                    if ('Neked ajánlott állások' in line):
                        break

        elif (name == 'itpeople'):
            for line in f:
                if(line.strip()):
                    if ('Közösség' in line):
                        cond = True
                    if (cond):
                        text += line
                    if ('Hasznos linkek' in line):
                        break

        elif (name == 'profession'):
            for line in f:
                if(line.strip()):
                    if ('Belépésálláskeresőknek' in line):
                        cond = True
                    if (cond):
                        text += line
                    if ('Értékelem' in line):
                        break

        elif(name == 'cvonline'):
            for line in f:
                if(line.strip()):
                    if ('ÁLLÁSHIRDETÉS FELADÁS' in line):
                        cond = True
                    if (cond):
                        text += line
                    if ('Jelentkezem' in line):
                        break

        elif(name == 'professia'):
            for line in f:
                if(line.strip()):
                    if ('                    Prihlásiť' in line):
                        cond = True
                    if (cond):
                        text += line
                    if ('                Všetky ponuky' in line):
                        break

        elif (name == 'kariera'):
            for line in f:
                if(line.strip()):
                    if ('				© 2023 Zoznam, s.r.o. Všetky práva vyhradené.' in line):
                        cond = True
                    if (cond):
                        text += line
                    if ('Späť na pracovné ponuky' in line):
                        break

    with open(f"txt/{name}/{initial}/job{id}.txt" , "w") as f:
        try:
            f.write(text)
        except (AttributeError):
            print('AttributeError')
            pass


    os.remove(f"txt/{name}/{initial}/temp.txt")
