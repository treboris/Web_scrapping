# Web_scrapping

A célja az volt, hogy a lokális (Szlovákia, Magyarország) munkaerőpiacon feltérképezzük,
hogy mire van szüksége az alkalmazott informatikai végzős diákoknak,
akik informatikai pozícióban szeretnének elhelyezkedni, 
továbbá Web scraping technika bemutatása és alkalmazása,
majd a kinyert adatok vizualizálása elsődlegesen Python környezetben.

A szkriptek futtatása különböző Python könyvtárak telepítését nélkül nem működnek!
Az alábbi könyvtárak telepítésére van szükség:

- selenium
- selenium webdriver
- beautifulSoup4
- requests
- tqdm
- pandas
- plotly
- matplotlib
- wordcloud
- squarify
- colorsys
- seaborn
```bash
.
├── data
│   ├── cvonline
│   │   ├── cvonline0.csv
│   │   ├── cvonline1.csv
│   │   ├── cvonline2.csv
│   │   ├── cvonline3.csv
│   │   ├── cvonline5.csv
│   │   ├── main0.txt
│   │   ├── main1.txt
│   │   ├── main2.txt
│   │   └── main3.txt
│   ├── foreign_full_main
│   │   └── foreign_full_main.txt
│   ├── full_main
│   │   └── full_main.txt
│   ├── hun_full_main
│   │   └── hun_full_main.txt
│   ├── itpeople
│   │   ├── itpeople0.csv
│   │   ├── itpeople1.csv
│   │   ├── itpeople2.csv
│   │   ├── itpeople3.csv
│   │   ├── main0.txt
│   │   ├── main1.txt
│   │   ├── main2.txt
│   │   └── main3.txt
│   ├── jobline
│   │   ├── jobline0.csv
│   │   ├── jobline1.csv
│   │   ├── jobline2.csv
│   │   ├── jobline3.csv
│   │   ├── main0.txt
│   │   ├── main1.txt
│   │   ├── main2.txt
│   │   └── main3.txt
│   ├── kariera
│   │   ├── kariera0.csv
│   │   ├── kariera1.csv
│   │   ├── kariera2.csv
│   │   ├── main0.txt
│   │   ├── main1.txt
│   │   ├── main2.txt
│   │   └── main3.txt
│   ├── professia
│   │   ├── main0.txt
│   │   ├── main1.txt
│   │   ├── main2.txt
│   │   ├── main3.txt
│   │   ├── professia0.csv
│   │   ├── professia1.csv
│   │   ├── professia2.csv
│   │   └── professia3.csv
│   ├── profession
│   │   ├── main0.txt
│   │   ├── main1.txt
│   │   ├── main2.txt
│   │   ├── main3.txt
│   │   ├── profession0.csv
│   │   ├── profession1.csv
│   │   ├── profession2.csv
│   │   ├── profession3.csv
│   │   └── profession5\012.csv
│   ├── stepstone
│   │   ├── main0.txt
│   │   ├── main1.txt
│   │   ├── main2.txt
│   │   ├── main3.txt
│   │   ├── stepstone0.csv
│   │   ├── stepstone1.csv
│   │   ├── stepstone2.csv
│   │   └── stepstone5.csv
│   ├── svk_full_main
│   │   └── svk_full_main.txt
│   └── txt
└── scripts
    ├── scrape
    │   ├── cvonline.py
    │   ├── initial.txt
    │   ├── itpeople.py
    │   ├── jobline.py
    │   ├── kariera_new.py
    │   ├── main.py
    │   ├── modules
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
        │   ├── cloudtechnologies.txt
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



data
│
├── A data könyvtárban találhatóak a kinyert adatok szortírozva weboldal név szerint, továbbá itt 
│    találhatóak a  txt nevű könyvtárban a részletes leírásu állások szöveges fájl formában.
│    A full_main nevű könyvtár tartalmazza a full_main.txt szöveges fájlt, amelyben össze van fűzve mind az összes
│    állás részletes leírása. Terjedel több mint 1 millió sornyi szöveg windows jegyzettömb nem mindig tudja megnyitni.
│    Az svk_full_main könyvtár az összes szlovák nyelvű, a hun_full_main az összes magyar nyelvű és a 
│     foreign_full_full main pedig az össze külföldi álláshirdető portál állását összefűzve tartalmazza.
│
├──scripts
    A scripts nevű könyvtár tartalmazza az összes szkriptet szortírozva funkcionalitásuk szerint.
    ├── scrape
    │    A könyvtár tartalmazza a cvonline.hu, itpeople.hu, jobline.hu, kariera.sk, professia.sk, profession.hu 
    │     és a stepstone.de 
    │    álláshirdető portálok automatikus adatgyűjtési szkriptjét. Továbbá tartalmaz egy inital.txt nevű szövegfájlt, 
    │     amely szkriptek mentésének a sorszámát tartalmazza. Futtatáskor érdemes megváltoztatni ellenben, ha az adott 
    │    sorszámmal már létezik a fájt, a szkript hibát dob és nem fut le. 
    │     A könyvtár tartalmaz még egy start.sh bash szkriptet, amllyel futtatható az összes weboldal
    │    adatgyűjtő szkriptje egymás után automatikusan. Linux-specifikus parancsokat tartalmaz, Windows környezetben nem működik.
    │     ├──modules
    │        A könyvtár tartalmazza az adatgyűjtő szkriptek végén használt Data.py osztályt, amely minden lefuttatott web scraping szkript végén meghívódik.
```
