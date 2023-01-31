import pandas as pd
from os.path import exists



class Save:


    def __init__(self,filename ,  *args):
        self.filename = filename
        try:
            self.args = dict(args)
        except TypeError:
            print("Invalid parameters or NULL parameters.")
        data_frame = pd.DataFrame(self.args)

        if (exist(f"data/{filename}")):

        else:
            data_frame.to_csv(f'data/{filename}.csv', sep=',', encoding='utf-8',index = False)
