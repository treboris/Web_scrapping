import matplotlib
import shutil
import glob
import re
import os




web_pages = ['cvonline','itpeople', 'jobline' , 'kariera' ,'professia','profession','stepstone']
files = []
count = 0
#COUNT JOB TXT FILES
def file_count(name ,path):
    global count
    file_count = len(glob.glob1(path,"*.txt"))
    count += file_count
    for x in range(0,file_count):
        files.append(f'{name}{x}.txt')

#LINK FILES
def link_files():
    for wp in web_pages:
        for value in range(0,4):
            with open(f'data/{wp}/main{value}.txt','wb') as main:
                file_count('job',f'txt/{wp}/{value}')
                for f in files:
                    with open(f'txt/{wp}/{value}/{f}','rb') as jobtxt:
                        shutil.copyfileobj(jobtxt,main)
                files.clear()
    for wp in web_pages:
        for value in range(0,3):
            with open(f'data/full_main/full_main.txt' , 'wb') as full_main:
                file_count('main',f'data/{wp}')
                for f in files:
                    with open(f'data/{wp}/{f}','rb') as maintxt:
                        shutil.copyfileobj(maintxt,full_main)
                files.clear()



link_files()
print(count)
