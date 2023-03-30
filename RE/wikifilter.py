from tqdm import tqdm
import pandas as pd
import re
import os


languages = {}
matches = {}


with open("CORPUS/wikiproglanguage.txt", 'r') as file:
    line = file.read().splitlines()
    for l in line:
        languages[l] = 0

    for limit in tqdm(range(0,300)):
        with open(f'../scrappers/txt/cvonline/0/job{limit}.txt' , 'r') as f:
            lines = f.readlines()
            for line in lines:
                for lang_element in languages.keys():
                    word = re.match(f'{re.escape(lang_element)}' , line)
                    if (word):
                        languages[f'{lang_element}'] +=1
                    else:
                        pass


for v in languages.keys():
    if(languages.get(v) > 0):
        matches[f'{v}'] = languages.get(v)

print(matches)
