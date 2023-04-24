import matplotlib.pyplot as plt
import sys
import re

keywordtxt = {}
data_hungary = {}
data_slovakia = {}
data_foreign = {}

try:
    arg_kw = sys.argv[1]
except(IndexError):
    arg_kw = 'selyetanterv'

#FILL keywords LIST
def keyword(name):
    with open(f"keywords/{name}.txt", 'r') as file:
        line = file.read().splitlines()
        for l in line:
            keywordtxt[l.casefold()] = 0

def data_fill(name):
    with open(f"keywords/{name}.txt", 'r') as file:
        line = file.read().splitlines()
        for l in line:
            data_hungary[l.casefold()] = 0
            data_slovakia[l.casefold()] = 0
            data_foreign[l.casefold()] = 0


def hungary():
    global keywordtxt
    keyword(f'{arg_kw}')
    with open(f'../../data/hun_full_main/hun_full_main.txt') as main:
        lines = main.read().splitlines()
        for line in lines:
            for corp in keywordtxt.keys():
                pattern = re.compile(fr'(?<!\w){re.escape(corp)}(?!\w)')
                matches = pattern.findall(line.casefold())
                if matches:
                    data_hungary[f'{corp}'] += len(matches)
    print('Hungary \a')

def slovakia():
    keyword(f'{arg_kw}')
    with open(f'../../data/svk_full_main/svk_full_main.txt') as main:
        lines = main.read().splitlines()
        for line in lines:
            for corp in keywordtxt.keys():
                pattern = re.compile(fr'(?<!\w){re.escape(corp)}(?!\w)')
                matches = pattern.findall(line.casefold())
                if matches:
                    data_slovakia[f'{corp}'] += len(matches)
    print('Slovakia \a')

def foreign():
    keyword(f'{arg_kw}')
    with open(f'../../data/foreign_full_main/foreign_full_main.txt') as main:
        lines = main.read().splitlines()
        for line in lines:
            for corp in keywordtxt.keys():
                pattern = re.compile(fr'(?<!\w){re.escape(corp)}(?!\w)')
                matches = pattern.findall(line.casefold())
                if matches:
                    data_foreign[f'{corp}'] += len(matches)

def area_diagram():
    langs =list(keywordtxt.keys())
    hu_data = list(data_hungary.values())
    sk_data = list(data_slovakia.values())
    world_data = list(data_foreign.values())
    x = range(len(langs))
    plt.stackplot(x, hu_data, sk_data, world_data, labels=['Magyarország', 'Szlovákia', 'Külföld'],edgecolor='black')
    plt.xticks(x, langs, rotation=45)
    plt.xlabel('Programozási nyelvek')
    plt.ylabel('Gyakoriság')
    plt.title('Programozási nyelvek gyakorisága régió szerint.')
    plt.legend(loc='upper right')
    plt.show()

def bar_diagram():
    fig, ax = plt.subplots()
    width = 0.3  # az egyes oszlopok szélessége

    ax.bar([i - width for i in range(1, len(data_slovakia)+1)], data_slovakia.values(), width, color='steelblue', alpha=0.7, label='Szlovákia', edgecolor='black')
    ax.bar([i for i in range(1, len(data_hungary)+1)], data_hungary.values(), width, color='brown', alpha=0.7, label='Magyarország', edgecolor='black')
    ax.bar([i + width for i in range(1, len(data_foreign)+1)], data_foreign.values(), width, color='darkolivegreen', alpha=0.7, label='Külföld', edgecolor='black')
    # tengelyfeliratok beállítása
    ax.set_xticks([i for i in range(1, len(data_hungary)+1)])
    ax.set_xticklabels(data_slovakia.keys())

    plt.legend()
    plt.show()



data_fill(arg_kw)
slovakia()
foreign()
hungary()
print(data_hungary)
print(data_slovakia)
print(data_foreign)
area_diagram()
bar_diagram()
