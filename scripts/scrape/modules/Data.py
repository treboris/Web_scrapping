import pandas as pd
import os

class Save:

    def __init__(self,path ,filename ,  *args):
        self.filename = filename
        self.path = path
        try:
            self.args = dict(args)
        except TypeError:
            print("Invalid parameters or NULL parameters.")
        data_frame = pd.DataFrame(self.args)
        exists = os.path.exists(f"../../data/{path}/{filename}.csv")
        if (exists):
            data_frame.to_csv(f'../../data/{path}/{filename}.csv',mode = 'a' , sep = ',',encoding='utf-8',index = False)
        else:
            data_frame.to_csv(f'../../data/{path}/{filename}.csv', sep=',', encoding='utf-8',index = False)
