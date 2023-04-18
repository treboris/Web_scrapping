from statistics import mean
import tkinter as tk
import matplotlib
import pandas as pd
import shutil
import glob
import re
import os
import time

salary_list = []
initial = 0

def professia(initial):
    data_professia = pd.read_csv(f'../data/professia/professia{initial}.csv',keep_default_na=False)
    salary_p = data_professia['Salary']
    for p in salary_p:
        if(p != 'nan'):
            try:
                text = ''.join(re.findall(r'\d+',p))
                #print(text)
                if (len(text) == 4):
                    salary_list.append(int(text))
            except (ValueError):
                pass

def kariera(initial):
    data_kariera = pd.read_csv(f'../data/kariera/kariera{initial}.csv',keep_default_na=False)
    salary_s = data_kariera['Salary']
    for s in salary_s:
        if(s != 'nan'):
            try:
                #print(''.join(re.findall(r'\d+',s)))
                salary_list.append(int(''.join(re.findall(r'\d+',s))))
            except (ValueError):
                pass

run = True
while(run):
    try:
        professia(initial)
    except (FileNotFoundError):
        initial =0
        while(True):
            try:
                kariera(initial)
            except (FileNotFoundError):
                run = False
                break
            initial +=1
    initial +=1

print(f'Jobs: {len(salary_list)}')
print(f'AVG salary: {int(mean(salary_list))}€')
