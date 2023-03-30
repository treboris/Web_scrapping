import tkinter as tk
import matplotlib

import pandas as pd
import shutil
import glob
import re
import os
import time

corpustxt = {}
matches = {}
files = []


def corpus(name):
    with open(f"CORPUS/{name}.txt", 'r') as file:
        line = file.read().splitlines()
        for l in line:
            corpustxt[l] = 0

def file_count(path):
    file_count = len(glob.glob1(path,"*.txt"))
    for x in range(0,file_count):
        files.append(f'job{x}.txt')

def link_files():
    file_count('txt/3')
    with open('data/cvonline/main0.txt','wb') as main:
        for f in files:
            with open(f'txt/0/{f}','rb') as jobtxt:
                shutil.copyfileobj(jobtxt,main)

def keyword_search(limit):
    corpus('sulibantanultak')
    #link_files()

    with open(f'data/cvonline/main{limit}.txt') as main:
        lines = main.read().splitlines()
        for line in lines:
            print(line.casefold())
            #time.sleep(1)
            for corp in corpustxt.keys():
                pattern = re.search(f'{re.escape(corp)}',line.casefold())
                if (pattern):
                    print('talalt')
                    corpustxt[f'{corp}'] += 1
                else:
                    pass

    for match in corpustxt.keys():
        if(corpustxt.get(match) > 0):
            matches[f'{match}'] = corpustxt.get(match)



keyword_search('0')


print(f'Talalatok: {matches}')
