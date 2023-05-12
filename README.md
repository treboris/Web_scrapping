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


data
│
├── A data könyvtárban találhatóak a kinyert adatok szortírozva weboldal név szerint, továbbá itt 
│    találhatóak a  txt nevű könyvtárban a részletes leírásu állások szöveges fájl formában.
│    A full_main nevű könyvtár tartalmazza a full_main.txt szöveges fájlt, amelyben össze van fűzve mind az összes
│    állás részletes leírása. Terjedel több mint 1 millió sornyi szöveg windows jegyzettömb nem mindig tudja megnyitni.
│    Az svk_full_main könyvtár az összes szlovák nyelvű, a hun_full_main az összes magyar nyelvű és a foreign_full_full main pedig 
│    az össze külföldi álláshirdető portál állását összefűzve tartalmazza.
│
├──scripts
    A scripts nevű könyvtár tartalmazza az összes szkriptet szortírozva funkcionalitásuk szerint.
    ├── scrape
    │    A könyvtár tartalmazza a cvonline.hu, itpeople.hu, jobline.hu, kariera.sk, professia.sk, profession.hu és a stepstone.de 
    │    álláshirdető portálok automatikus adatgyűjtési szkriptjét. Továbbá tartalmaz egy inital.txt nevű szövegfájlt, amely a
    │    szkriptek mentésének a sorszámát tartalmazza. Futtatáskor érdemes megváltoztatni ellenben, ha az adott sorszámmal már létezik 
    │    a fájt, a szkript hibát dob és nem fut le. A könyvtár tartalmaz még egy start.sh bash szkriptet, amllyel futtatható az összes weboldal
    │    adatgyűjtő szkriptje egymás után automatikusan. Linux-specifikus parancsokat tartalmaz, Windows környezetben nem működik!
    │     ├──modules
    │        A könyvtár tartalmazza az adatgyűjtő szkriptek végén használt Data.py osztályt, amely minden lefuttatott web scraping szkript végén meghívódik.
