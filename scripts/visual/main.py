import matplotlib.pyplot as plt
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
        self.btn1 = tk.Button(self, text="Location Hungary", command=self.location_hun,width=30, height=3)
        self.btn1.pack(side="left")

        self.btn2 = tk.Button(self, text="Location Slovakia", command=self.location_svk,width=30, height=3)
        self.btn2.pack(side="left")

        self.btn3 = tk.Button(self, text="Ranks", command=self.rank,width=30, height=3)
        self.btn3.pack(side="left")

        self.btn4 = tk.Button(self, text="Piechart", command=self.programing,width=30, height=3)
        self.btn4.pack(side="left")

        self.btn5 = tk.Button(self, text="Area diagram", command=self.area,width=30, height=3)
        self.btn5.pack(side="left")

        self.btn6 = tk.Button(self, text="AVG salary in Slovakia", command=self.avg_salary,width=30, height=3)
        self.btn6.pack(side="left")

        self.label = tk.Label(self, text="")
        self.label.pack()

    def location_hun(self):
        df1 = pd.read_csv('diagram_data/location_hun.csv')
        region = dict(zip(df1['city'], df1['count']))

        def add_labels():
            labels = []
            for x in region.values():
                labels.append(x)
            for i in range(len(labels)):
                plt.text(i, labels[i], labels[i], ha = 'center')

        fig, ax = plt.subplots(layout='constrained')
        add_labels()
        fig.set_figheight(15)
        fig.set_figwidth(15)
        data = region
        plt.title("Feladott hirdetések települések szerint")
        ax.set_title('Települések')
        ax.bar(*zip(*data.items()), color=['brown' , 'darkolivegreen','steelblue' , 'chocolate'])
        ax.set_ylim(0, 5500)
        ax.set_ylabel('Gyakoriság')
        plt.show()

    def location_svk(self):
        df2 = pd.read_csv('diagram_data/location_svk.csv')
        region1 = dict(zip(df2['city'], df2['count']))

        def add_labels():
            labels = []
            for x in region1.values():
                labels.append(x)
            for i in range(len(labels)):
                plt.text(i, labels[i], labels[i], ha = 'center')

        fig, ax = plt.subplots(layout='constrained')
        fig.set_figheight(15)
        fig.set_figwidth(15)
        data = region1
        add_labels()
        plt.title("Feladott hirdetések települések szerint")
        ax.set_title('Települések')
        ax.bar(*zip(*data.items()), color=['brown' , 'darkolivegreen','steelblue' , 'chocolate'],label = 'Sine')
        ax.set_ylim(0, 2200)
        ax.set_ylabel('Gyakoriság')
        plt.plot()
        plt.show()

    def rank(self):
        df3 = pd.read_csv('diagram_data/piechart.csv')
        matches = dict(zip(df3['rank'], df3['count']))
        fig = plt.figure(figsize=(15,15))
        ax = fig.add_subplot(111)
        data = {k.capitalize(): v for k, v in matches.items()}
        wedges, labels, _ = ax.pie(data.values(), labels=data.keys(), autopct='%1.1f%%')
        labels = [f"{label}: {value}" for label, value in data.items()]
        ax.legend(wedges, labels, loc="center right", bbox_to_anchor=(1.2, 0.5),fontsize = 15)
        fig.set_size_inches(8, 6)
        plt.tight_layout()
        plt.show()

    def programing(self):
        df4 = pd.read_csv('diagram_data/programing.csv')
        counts = dict(zip(df4['languages'], df4['count']))

        def add_labels():
            global max_value
            labels = []
            for x in counts.values():
                labels.append(x)
            for i in range(len(labels)):
                plt.text(i, labels[i], labels[i], ha = 'center')
            max_value = max(counts,key=counts.get)

        fig, ax = plt.subplots(layout='constrained')
        add_labels()
        fig.set_figheight(15)
        fig.set_figwidth(15)
        data = counts
        plt.title("Kulcsszógyakoriság")
        ax.set_title('Programozási nyelvek')
        ax.bar(*zip(*data.items()), color=['brown' , 'darkolivegreen','steelblue' , 'chocolate'])
        ax.set_ylim(0,data[max_value]+1000)
        ax.set_ylabel('Gyakoriság')
        plt.show()

    def area(self):
        df5 = pd.read_csv('diagram_data/programing_hun.csv')
        df6 = pd.read_csv('diagram_data/programing_svk.csv')
        df7 = pd.read_csv('diagram_data/programing_foreign.csv')

        data_hungary = dict(zip(df5['languages'], df5['count']))
        data_slovakia = dict(zip(df6['languages'], df6['count']))
        data_foreign = dict(zip(df7['languages'], df7['count']))

        langs =list(data_hungary.keys())
        hu_data = list(data_hungary.values())
        sk_data = list(data_slovakia.values())
        foreign_data = list(data_foreign.values())
        fig = plt.figure(figsize=(15,15))
        ax = fig.add_subplot(111)
        x = range(len(langs))
        plt.stackplot(x, hu_data, sk_data, foreign_data, labels=['Magyarország', 'Szlovákia', 'Külföld'],edgecolor='black')
        plt.xticks(x, langs, rotation=45)
        plt.xlabel('Programozási nyelvek')
        plt.ylabel('Gyakoriság')
        plt.title('Programozási nyelvek gyakorisága régió szerint.')
        plt.legend(loc='upper right')
        plt.show()

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
        self.label.config(text= int(mean(salary_list)))

root = tk.Tk()
app = App(master=root)
app.mainloop()
