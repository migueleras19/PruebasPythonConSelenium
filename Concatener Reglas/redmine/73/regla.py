
#Contatenar 2 archivos excel
import os
import pandas as pd

data_file_folder = '/media/qacore/data/PruebasPythonConSelenium/Concatener Reglas/redmine/73'

df = []

for file in os.listdir(data_file_folder):

    if file.endswith('.xls'):

        print('Carga de archivos {0} ...'.format(file))
        
        df.append(pd.read_excel(os.path.join(data_file_folder, file), sheet_name='A'))

df_master =pd.concat(df, axis=0)
df_master.to_excel('73.xlsx', index=False)

        
        