import pandas as pd
import os

for file in os.listdir('.'):
    print(file)
    if file.endswith('.xlsx'):
        pd.read_excel(file).to_csv(file[:-4] + 'csv')