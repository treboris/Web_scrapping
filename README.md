# Web_scrapping

A feladat célja az volt, hogy a lokális (Szlovákia, Magyarország) munkaerőpiacon feltérképezzük,
hogy mire van szüksége az alkalmazott informatikai végzős diákoknak,
akik informatikai pozícióban szeretnének elhelyezkedni, 
továbbá Web scraping technika bemutatása és alkalmazása,
majd a kinyert adatok vizualizálása elsődlegesen Python környezetben.

A diagramok a requirements.txt-ben lévő könyvtárak feltelepítése után a scripts/visual/main.py python fájl futtatásával a megjelenő Tkinter alkalmazáson elérhetőek.

```bash
pip install requirements.txt
```

1.) Az adatok automatikus kigyűjtése lista nézetből a scripts/scrape/<oldalneve>.py fájl futtatásával hajtható végre.
    Az initial.txt szövegfájlban lévő szám lesz a kimentett .csv fájl sorszáma, ezt érdemes megváltoztatni.
    
```bash
python3 cvonline.py
```
2.) Ahhoz, hogy az állásokat egyenként kinyerjük .txt szövegfájlokba, el kellett végezni  az első lépést, 
    mert a lista nézetből elmentett .csv fájl tartalmazza az összes állás részletes leírásához a linket.
    A scripts/scrape/onebyone/<oldalneve>.py fájlt kell lefuttatni.
        
```bash
python3 cvonline_page.py
```
3.) A következő lépés a fájlok összefűzése.
    A scripts/visual/link_files/link_files.py szkript lefuttatásával történik meg a fájlösszefűzés.
    FIGYELEM!! A link_files.py forráskódjában a web_pages nevű lista alapértelmezetten tartalmazza mind a hat weboldal nevét.
                Csak azt a weboldal nevet kell bent hagyni amelynek az adatait kigyűjtöttük és szeretnénk összefűzni.
        
```bash
python3 link_files.py
```

 4.) A következő lépésben az összefűzött fájlokban vizsgálhatunk gyakoriságot, vagy kulcsszó gyakoriságot.
    Gyakoriság vizsgálathoz a scripts/visual/gyakorisag.py fájlt kell futtatni, amely kalibrációt igényel.
    Elsőször meg kell adni a szövegfájlt, amelyben szeretnénk végrehajtani az elemzést az input_txt változóban, másodszor pedig
    az outpu_csv változóban a kimeneti .csv fájl nevét.

```bash
python3 gyakorisag.py
```
    Kulcsszó gyakoriság elemzéshez a scripts/visual/keyword.py fájlt kell futtatni, parancssori argumentummal átadható a
    kulcsszavakat tartalmazó szövegfájl. Alapertelmezetten
    
```bash
python3 keywords.py
```
    
    
    

## A fájlok hierarchiája

```bash
.
├── data
│   │
│   │       A könyvtárban találhatóak a kinyert adatok szortírozva weboldal név szerint, továbbá itt 
│   │       találhatóak a  txt nevű könyvtárban a részletes leírásu állások szöveges fájl formában.
│   │       A full_main nevű könyvtár tartalmazza a full_main.txt szöveges fájlt, amelyben össze van fűzve mind az összes
│   │       állás részletes leírása. Terjedel több mint 1 millió sornyi szöveg windows jegyzettömb nem mindig tudja megnyitni.
│   │       Az svk_full_main könyvtár az összes szlovák nyelvű, a hun_full_main az összes magyar nyelvű és a 
│   │       foreign_full_full main pedig az össze külföldi álláshirdető portál állását összefűzve tartalmazza.
│   │
│   ├── cvonline
│   ├── foreign_full_main
│   │   └── foreign_full_main.txt
│   ├── full_main
│   │   └── full_main.txt
│   ├── hun_full_main
│   │   └── hun_full_main.txt
│   ├── itpeople
│   ├── jobline
│   ├── kariera
│   ├── professia
│   ├── profession
│   ├── stepstone
│   ├── svk_full_main
│   │   └── svk_full_main.txt
│   └── txt
│       └── ...
└── scripts
    │
    │         A könyvtár tartalmazza az összes szkriptet szortírozva funkcionalitásuk szerint.
    │        
    ├── scrape
    │   │       A könyvtár tartalmazza a cvonline.hu, itpeople.hu, jobline.hu, kariera.sk, professia.sk, profession.hu 
    │   │       és a stepstone.de 
    │   │       álláshirdető portálok automatikus adatgyűjtési szkriptjét. Továbbá tartalmaz egy inital.txt nevű szövegfájlt, 
    │   │       amely szkriptek mentésének a sorszámát tartalmazza. Futtatáskor érdemes megváltoztatni ellenben, ha az adott 
    │   │       sorszámmal már létezik a fájt, a szkript hibát dob és nem fut le. 
    │   │       A könyvtár tartalmaz még egy start.sh bash szkriptet, amllyel futtatható az összes weboldal
    │   │       adatgyűjtő szkriptje egymás után automatikusan. Linux-specifikus parancsokat tartalmaz, Windows környezetben nem működik.
    │   │
    │   ├── cvonline.py
    │   ├── initial.txt
    │   ├── itpeople.py
    │   ├── jobline.py
    │   ├── kariera_new.py
    │   ├── main.py
    │   ├── modules
    │   │   │        A könyvtár tartalmazza az adatgyűjtő szkriptek végén használt Data.py osztályt, 
    │   │   │        amely minden lefuttatott web scraping szkript végén meghívódik. Ezenfelül tartalmazza a
    │   │   │        a tools.py modult, amely bizonyos funkciókat lát el a web scraping szkriptekben. A one_by_one_scrape.py modul arra a
    │   │   │        célra keszült, hogy az összes állást mind a 6 weboldalon automatikusan tudjuk kigyűjteni. Sajnos csak megfelelően karban tartott
    │   │   │        szkriptek esetén működik, amely rengeteg energiát és időt igényel, ezért csak minta jelleggel szolgál, hogy meg lehet így is oldani.
    │   │   │                
    │   │   ├── Data.py
    │   │   ├── one_by_one_scrape.py
    │   │   └── tools.py
    │   ├── onebyone
    │   │   ├── cvonline_page.py
    │   │   ├── Data.py
    │   │   ├── it_people_page.py
    │   │   ├── jobline_page.py
    │   │   ├── kariera_page.py
    │   │   ├── professia_page.py
    │   │   ├── profession_page.py
    │   │   └── stepstone.py
    │   ├── professia.py
    │   ├── profession.py
    │   ├── start.sh
    │   └── stepstone.py
    └── visual
        │ 
        │             A gyakoriság és a kulcsszó gyakoriság elemzés eredményei a diagram_data könyvtárban tárolódnak.
        │             A keywords nevű könyvtárban a keresendő kulcsszavak vannak szöveg fájlokban.A link_files könyvtárban a fájl összefűzést 
        │             elvégző szkriptek találhatóak. Az avg_salary.py az átlagfizetést számít a szlovákiában feladott hirdetésekből. A location_hun.py és
        │             a locaton_svk.py az országban feladott hirdetések adatait gyűjti össze.
        │             A gyakorisag.py a gyakoriság elemzést elvégző szkript.
        │             A kezword_search.py a kulcsszó gyakoriságot elvégző szkript.
        │              A main.py egy tkinter alkalmazás amely lehetővé teszi a különböző diagramok közti böngészést és a diagramok generálását.
        │  
        ├── avg_salary.py
        ├── diagram_data
        │   ├── location_hun.csv
        │   ├── location_svk.csv
        │   ├── piechart.csv
        │   ├── programing.csv
        │   ├── programing_foreign.csv
        │   ├── programing_hun.csv
        │   ├── programing_svk.csv
        │   ├── top20.csv
        │   ├── top20new.csv
        │   ├── tree.csv
        │   ├── wordcloud.csv
        │   └── words.csv
        ├── gyakorisag.py
        ├── keywords
        │   ├── databases.txt
        │   ├── piechart.txt
        │   ├── tanterv.txt
        │   ├── top10.txt
        │   └── trend.txt
        ├── keyword_search.py
        ├── link_files
        │   ├── link_files_foreign.py
        │   ├── link_files_hun.py
        │   ├── link_files.py
        │   └── link_files_svk.py
        ├── location_hun.py
        ├── location_svk.py
        └── main.py
      
```
