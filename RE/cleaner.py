import resource
import os



file_name = 'data/cvonline/main0.txt'

txt_file = open(file_name)


for line in txt_file:
    print(line.casefold())


txt_file.close()
