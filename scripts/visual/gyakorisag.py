from collections import Counter
import pandas as pd

# Fájl megnyitása és beolvasása
with open('../../data/full_main/full_main.txt', 'r') as f:
    text = f.read().casefold()

# A kihagyandó szavak
df_hun = pd.read_csv('diagram_data/words.csv')

comma = ['support,','time,','office,','véleményét,','programátor,','állásértesítőnket,','kérjük,','állásértesítőnket,','munkaidő,','it,','budapest,','programozó,','kérjük']
excluded_words = df_hun['words'].to_list()
excluded_words.extend(comma)

# Szavak kinyerése a szövegből
words = text.split()

# Szavak gyakoriságának meghatározása
word_counts = Counter(word for word in words if word not in excluded_words)
dict_counts ={}
# Leggyakoribb 50 szó kiírása
for word, count in word_counts.most_common(25):
    dict_counts[word] = count
    print(f'{word} {count}')

# A gyakoriság szótár konvertálása DataFrame-mé
df = pd.DataFrame.from_dict(dict_counts, orient='index', columns=['Count'])

# Adatok mentése CSV-fájlba
df.to_csv('diagram_data/wordcloud.csv', sep=',', index_label='Word')
