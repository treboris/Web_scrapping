import pandas as pd
import time



corp = ["asdasd", "asdasssd", "peter"]
main = ["544654","12331321"]

data_dict = {"Corporation" : corp ,"Main" : main}
data_frame = pd.DataFrame(data_dict)

print(type(data_frame))
#data_frame.to_csv('jobline_data.csv', sep=',', encoding='utf-8',index = False)
