import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import colors
import colorsys
import squarify
from statistics import mean
import tkinter as tk
import pandas as pd
import os
import re


class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #1gorup
        self.label = tk.Label(self, text="Diagramok régió szerint",width= 20,height=2)
        self.label.grid(row=0, column=0)

        self.btn1 = tk.Button(self, text="Magyarország", command=self.magyarorszag,width=30, height=3)
        self.btn1.grid(row=1, column=0)

        self.btn2 = tk.Button(self, text="Szlovákia", command=self.szlovakia,width=30, height=3)
        self.btn2.grid(row=1, column=1)



        #2group
        self.label1 = tk.Label(self, text="Programozási nyelvek",width= 20,height=2)
        self.label1.grid(row=2, column=0)

        self.btn3 = tk.Button(self, text="Az összes állás", command=self.programozasi_nyelvek,width=30, height=3)
        self.btn3.grid(row=3, column=0)

        self.btn4 = tk.Button(self, text="Magyarország", command=self.programozasi_nyelvek_hun,width=30, height=3)
        self.btn4.grid(row=3, column=1)

        self.btn5 = tk.Button(self, text="Szlovákia", command=self.programozasi_nyelvek_svk,width=30, height=3)
        self.btn5.grid(row=3, column=2)

        self.btn6 = tk.Button(self, text="Külföld", command=self.programozasi_nyelvek_foreign,width=30, height=3)
        self.btn6.grid(row=3, column=3)


        self.labelx = tk.Label(self, text="Átlagbér Szlovákiában az IT szektorban",width= 30,height=3)
        self.labelx.grid(row=4, column=0)


        self.btn7 = tk.Button(self, text="Számítás", command=self.avg_salary,width=30, height=3)
        self.btn7.grid(row=5, column=0)

        self.labelx = tk.Label(self, text="---------",width= 30,height=3)
        self.labelx.grid(row=5, column=1)

        #3group
        self.label1 = tk.Label(self, text="Egyéb diagramok",width= 20,height=2)
        self.label1.grid(row=6, column=0)

        self.btn8 = tk.Button(self, text="Kördiagram", command=self.pie,width=30, height=3)
        self.btn8.grid(row=7, column=0)

        self.btn9 = tk.Button(self, text="WordCloud", command=self.word_cloud,width=30, height=3)
        self.btn9.grid(row=7, column=1)

        self.btn10 = tk.Button(self, text="Treemap", command=self.tree,width=30, height=3)
        self.btn10.grid(row=7, column=2)


    def magyarorszag(self):
        df = pd.read_csv('diagram_data/location_hun.csv')
        sorted_data = df.sort_values(by='count',ascending=False)
        data = dict(zip(sorted_data['city'], sorted_data['count']))

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
        )

        # Diagram létrehozása
        fig = go.Figure(data=[trace])

        # Tengelyek címkéinek hozzáadása
        fig.update_xaxes(title='Települések')
        fig.update_yaxes(title='Százalék')

        # Diagram megjelenítése
        fig.show()

    def szlovakia(self):
        df = pd.read_csv('diagram_data/location_svk.csv')
        sorted_data = df.sort_values(by='count',ascending=False)
        data = dict(zip(sorted_data['city'], sorted_data['count']))

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
        )

        # Diagram létrehozása
        fig = go.Figure(data=[trace])

        # Tengelyek címkéinek hozzáadása
        fig.update_xaxes(title='Települések')
        fig.update_yaxes(title='Százalék')

        # Diagram megjelenítése
        fig.show()


    def pie(self):
        df = pd.read_csv('diagram_data/piechart.csv')
        data = dict(zip(df['rank'], df['count']))

        # Convert data dictionary to lists
        labels = list(data.keys())
        values = list(data.values())

        # Calculate percentages
        total = sum(values)
        percentages = [round((val / total) * 100, 2) for val in values]

        # Create pie chart
        fig = go.Figure(data=[go.Pie(labels=labels, values=percentages)])

        # Set title
        fig.update_layout(title='Tapasztalati szintek')

        # Display chart
        fig.show()


    def programozasi_nyelvek(self):
        df = pd.read_csv('diagram_data/programing.csv')
        sorted_data = df.sort_values(by='count',ascending=False)
        data = dict(zip(sorted_data['languages'], sorted_data['count']))

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
        )

        # Diagram létrehozása
        fig = go.Figure(data=[trace])

        # Tengelyek címkéinek hozzáadása
        fig.update_xaxes(title='Programozási nyelvek és egyéb technológiák')
        fig.update_yaxes(title='Százalék')

        # Diagram megjelenítése
        fig.show()


    def programozasi_nyelvek_hun(self):
        df = pd.read_csv('diagram_data/programing_hun.csv')
        sorted_data = df.sort_values(by='count',ascending=False)
        data = dict(zip(sorted_data['languages'], sorted_data['count']))

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
        )

        # Diagram létrehozása
        fig = go.Figure(data=[trace])

        # Tengelyek címkéinek hozzáadása
        fig.update_xaxes(title='Programozási nyelvek és egyéb technológiák')
        fig.update_yaxes(title='Százalék')

        # Diagram megjelenítése
        fig.show()

    def programozasi_nyelvek_svk(self):
        df = pd.read_csv('diagram_data/programing_svk.csv')
        sorted_data = df.sort_values(by='count',ascending=False)
        data = dict(zip(sorted_data['languages'], sorted_data['count']))

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
        )

        # Diagram létrehozása
        fig = go.Figure(data=[trace])

        # Tengelyek címkéinek hozzáadása
        fig.update_xaxes(title='Programozási nyelvek és egyéb technológiák')
        fig.update_yaxes(title='Százalék')

        # Diagram megjelenítése
        fig.show()

    def programozasi_nyelvek_foreign(self):
        df = pd.read_csv('diagram_data/programing_foreign.csv')
        sorted_data = df.sort_values(by='count',ascending=False)
        data = dict(zip(sorted_data['languages'], sorted_data['count']))

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
        )

        # Diagram létrehozása
        fig = go.Figure(data=[trace])

        # Tengelyek címkéinek hozzáadása
        fig.update_xaxes(title='Programozási nyelvek és egyéb technológiák')
        fig.update_yaxes(title='Százalék')

        # Diagram megjelenítése
        fig.show()

    def avg_salary(self):
        salary_list = []
        initial = 0
        def professia(initial):
            data_professia = pd.read_csv(f'../../data/professia/professia{initial}.csv',keep_default_na=False)
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
            data_kariera = pd.read_csv(f'../../data/kariera/kariera{initial}.csv',keep_default_na=False)
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
        self.labelx.config(text= f'{int(mean(salary_list))}€')

    def tree(self):

        df = pd.read_csv('diagram_data/programing.csv')
        squarify.plot(sizes=df['count'], label=df['languages'].str.title(), alpha=.8)

        plt.axis('off')
        plt.show()


    def word_cloud(self):

        df = pd.read_csv('diagram_data/programing.csv')
        data = dict(zip(df['languages'],df['count']))

        def hsl_to_rgb(hsl):
            h, s, l = hsl
            return tuple(round(i * 255) for i in colorsys.hls_to_rgb(h / 360, l / 100, s / 100))
        def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
            return tuple(hsl_to_rgb((random_state.randint(0, 360), 80, 50)))

        wordcloud = WordCloud(width=480, height=480, margin=0, color_func=color_func).generate_from_frequencies(data)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.margins(x=0, y=0)
        plt.show()


root = tk.Tk()
app = App(master=root)
app.mainloop()
