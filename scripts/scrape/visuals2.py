import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

langs = []
counts = []

raw = {'python': 58, 'java': 265, 'flask': 2, 'programozó': 77, 'http protocol': 2, 'html': 38, 'css': 44,
 'flutter': 5, 'junior': 38, 'medior': 22, 'senior': 82, 'javascript': 76, 'sql': 142, 'oop': 44,
  'sap': 465, 'excel': 79, 'c#': 68, 'perl': 8, 'tex': 5, 'c++': 36, 'assembly': 4, 'udemi': 1,
   'microsoft': 53, 'english': 185, 'pandas': 3, 'cyber': 61, 'django': 2}

adatok = {}


for key ,value in raw.items():
    if (value > 10):
        adatok[key] = value
    else:
        pass

print(adatok)

for adat in adatok.keys():
    langs.append(adat)
for ada in adatok.values():
    counts.append(ada)




fig, ax = plt.subplots()


bar_colors = ['tab:red']

ax.bar(langs, counts, color=bar_colors)

ax.set_ylabel('Kifejezes elofordulas')
ax.set_title('Keresett programnyelvek')

plt.show()
