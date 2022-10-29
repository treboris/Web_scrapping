from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import pandas as pd
#import save_data as data
import time

#SELENIUM HEADLESS MODE
options = Options()
options.headless = True


start_time = time.time()


company = []

class Scrapping:


    def __init__(self ,name,url):
        self.name = name
        self.url = url

        #Alapbol meghivom inicializalaskor
        self.conn()




    def conn():
        browser = webdriver.Firefox(options=options)
        browser.get(self.url)






    def start_scrap(self):


        search_by_class = browser.find_elements(By.CLASS_NAME,"mt-md-4 mt-lg-0")


        #WEBPAGE TO TXT
        soup  = BeautifulSoup(browser.page_source, "html.parser")
        pretty = soup.prettify()


        #export to html
        # try:
        #     with open("profession.html", "w") as file:
        #         file.write(str(pretty))
        #         print("||SAVED||")
        # except:
        #     print("Nem irta ki.")

        title = soup.find('title')
        print(title.string)



        #ISEMPTY?
        if (search_by_class):
            pass
        else:
            print("Not found.")



        for elements in search_by_class:
            company.append(elements.text)
        dict = {"Company": company}
        data_frame = pd.DataFrame(dict)
        return print(data_frame)



        browser.quit()
        print("Scrapping time was: %s seconds" % (time.time() - start_time))



#first_object = Scrapping("Professia","https://www.profession.hu/allasok/0,0,0,python%401%401?keywordsearch")
