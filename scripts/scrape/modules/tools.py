import os


def initial():
    with open('/home/ferryman/Documents/Web_scrapping/scripts/scrape/initial.txt','r') as file:
        initial = file.read()
        return int(initial)

def f_exists(name ,initial):
    if(os.path.exists(f'../../data/{name}/{name}{initial}.csv')):
        print('The file is exists')
        print('\a')
        exit()
    else:
        pass
