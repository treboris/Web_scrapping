import shutil
import glob
import re
import os

web_pages = ['stepstone']
files = []
count = 0
def file_count(name ,path):
    global count
    file_count = len(glob.glob1(path,"*.txt"))
    count += file_count
    for x in range(0,file_count):
        files.append(f'{name}{x}.txt')

def link_files():
    for wp in web_pages:
        for value in range(0,4):
            with open(f'../../../data/{wp}/main{value}.txt','wb') as main:
                file_count('job',f'../../../data/txt/{wp}/{value}')
                for f in files:
                    try:
                        with open(f'../../../data/txt/{wp}/{value}/{f}','rb') as jobtxt:
                            shutil.copyfileobj(jobtxt,main)
                    except (FileNotFoundError):
                        pass
                files.clear()
    for wp in web_pages:
        with open(f'../../../data/foreign_full_main/foreign_full_main.txt' , 'ab') as full_main:
            file_count('main',f'../../../data/{wp}')
            for f in files:
                with open(f'../../../data/{wp}/{f}','rb') as maintxt:
                    shutil.copyfileobj(maintxt,full_main)
            files.clear()

link_files()
print(count)
