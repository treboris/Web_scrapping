import re
from tqdm import tqdm





languages = {'C#' : 0 , 'Python' : 0 , 'SQL' : 0 , 'HTML' : 0 , 'CSS' : 0,
    'cafeteria' : 0 , 'java' :0 , 'Java' : 0 , 'JAVA' : 0 ,'Python' : 0,'angol' :0,'Budapest' :0 ,
    'asd' : 0 , 'C++' : 0

            }


for limit in tqdm(range(0,579)):
    with open(f'../scrappers/txt/cvonline/0/job{limit}.txt' , 'r') as f:
        lines = f.readlines()
        for line in lines:
            for lang_element in languages.keys():
                word = re.search(f'^{lang_element}' , line)
                if (word):
                    languages[f'{lang_element}'] +=1
                else:
                    pass



print(languages)
