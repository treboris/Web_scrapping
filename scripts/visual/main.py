import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import seaborn as sns
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import colors
import colorsys
import squarify
from statistics import mean
import tkinter as tk
import pandas as pd
import random
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

        self.btnx = tk.Button(self, text="Összehasonlitas", command=self.osszehasonlitas,width=30, height=3)
        self.btnx.grid(row=1, column=2)



        #2group
        self.label1 = tk.Label(self, text="Programozási nyelvek és technológiák",width= 30,height=1)
        self.label1.grid(row=2, column=0)

        self.btn3 = tk.Button(self, text="Az összes állás", command=self.programozasi_nyelvek,width=30, height=3)
        self.btn3.grid(row=3, column=0)

        self.btn4 = tk.Button(self, text="Magyarország", command=self.programozasi_nyelvek_hun,width=30, height=3)
        self.btn4.grid(row=3, column=1)

        self.btn5 = tk.Button(self, text="Szlovákia", command=self.programozasi_nyelvek_svk,width=30, height=3)
        self.btn5.grid(row=3, column=2)

        self.btn6 = tk.Button(self, text="Külföld", command=self.programozasi_nyelvek_foreign,width=30, height=3)
        self.btn6.grid(row=3, column=3)

        #3group
        self.label1 = tk.Label(self, text="Egyéb diagramok",width= 20,height=2)
        self.label1.grid(row=4, column=0)

        self.btn8 = tk.Button(self, text="Kördiagram", command=self.pie,width=30, height=3)
        self.btn8.grid(row=5, column=0)

        self.btn9 = tk.Button(self, text="WordCloud", command=self.word_cloud,width=30, height=3)
        self.btn9.grid(row=5, column=1)

        self.btn10 = tk.Button(self, text="Treemap", command=self.tree,width=30, height=3)
        self.btn10.grid(row=5, column=2)

    def osszehasonlitas(self):
           # Magyarország diagramja
        df_hun = pd.read_csv('diagram_data/location_hun.csv')
        sorted_data_hun = df_hun.sort_values(by='count',ascending=False)
        data_hun = dict(zip(sorted_data_hun['city'], sorted_data_hun['count']))

        # Százalékos értékek kiszámítása
        total_hun = sum(data_hun.values())
        percentages_hun = [(count / total_hun) * 100 for count in data_hun.values()]
        colors_hun = px.colors.qualitative.Plotly[:10]

        # Trace létrehozása
        trace_hun = go.Bar(
            x=list(data_hun.keys()),
            y=list(data_hun.values()),
            text=[f"{p:.2f}%" for p in percentages_hun],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
            marker=dict(color=colors_hun))

        # Diagram létrehozása
        fig_hun = go.Figure(data=[trace_hun])

        # Tengelyek címkéinek hozzáadása
        fig_hun.update_xaxes(title='Települések')
        fig_hun.update_yaxes(title='Százalék')
        fig_hun.update_layout(title_text="Magyarország")


        # Szlovákia diagramja
        df_svk = pd.read_csv('diagram_data/location_svk.csv')
        sorted_data_svk = df_svk.sort_values(by='count',ascending=False)
        data_svk = dict(zip(sorted_data_svk['city'], sorted_data_svk['count']))
        colors_svk = px.colors.qualitative.Plotly[:10]

        # Százalékos értékek kiszámítása
        total_svk = sum(data_svk.values())
        percentages_svk = [(count / total_svk) * 100 for count in data_svk.values()]

        # Trace létrehozása
        trace_svk = go.Bar(
            x=list(data_svk.keys()),
            y=list(data_svk.values()),
            text=[f"{p:.2f}%" for p in percentages_svk],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
            marker=dict(color=colors_svk))

        # Diagram létrehozása
        fig_svk = go.Figure(data=[trace_svk])

        # Tengelyek címkéinek hozzáadása
        fig_svk.update_xaxes(title='Települések')
        fig_svk.update_yaxes(title='Százalék')
        fig_hun.update_layout(title_text="Szlovákia")
        # Két diagram összeillesztése egyetlen ábrába
        fig = make_subplots(rows=1, cols=2)

        fig.add_trace(trace_hun, row=1, col=1)
        fig.add_trace(trace_svk, row=1, col=2)

        # Tengelyek címkéinek beállítása
        fig.update_xaxes(title_text="Magyarország", row=1, col=1)
        fig.update_xaxes(title_text="Szlovákia", row=1, col=2)
        fig.update_yaxes(title_text="Százalék", row=1, col=1)

        # A fő cím és a méretek beállítása
        fig.update_layout(title_text="Magyarország és Szlovákia összehasonlítása", title_x=0.5, width=1000, height=600)

        fig.show()
    def magyarorszag(self):
        df = pd.read_csv('diagram_data/location_hun.csv')
        sorted_data = df.sort_values(by='count',ascending=False)
        data = dict(zip(sorted_data['city'], sorted_data['count']))

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]
        colors = px.colors.qualitative.Plotly[:10]
        #colors = [f"rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})" for _ in data.keys()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
            marker=dict(color=colors))

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
        colors = px.colors.qualitative.Plotly[:10]

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
            marker=dict(color=colors))

        # Diagram létrehozása
        fig = go.Figure(data=[trace])

        # Tengelyek címkéinek hozzáadása
        fig.update_xaxes(title='Települések')
        fig.update_yaxes(title='Százalék')
        fig.update_layout(title_text="Szlovákia", title_x=0.5, width=800, height=600)
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
        colors = px.colors.qualitative.Plotly[:12]
        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
            marker=dict(color=colors))

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
        colors = px.colors.qualitative.Plotly[:10]

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
            marker=dict(color=colors))

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
        colors = px.colors.qualitative.Plotly[:10]

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
            marker=dict(color=colors))

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
        colors = px.colors.qualitative.Plotly[:10]

        # Százalékos értékek kiszámítása
        total = sum(data.values())
        percentages = [(count / total) * 100 for count in data.values()]

        # Trace létrehozása
        trace = go.Bar(
            x=list(data.keys()),
            y=list(data.values()),
            text=[f"{p:.2f}%" for p in percentages],  # százalékos értékek hozzáadása a szöveges jelöléshez
            textposition='auto',
            marker=dict(color=colors))

        # Diagram létrehozása
        fig = go.Figure(data=[trace])

        # Tengelyek címkéinek hozzáadása
        fig.update_xaxes(title='Programozási nyelvek és egyéb technológiák')
        fig.update_yaxes(title='Százalék')

        # Diagram megjelenítése
        fig.show()

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
