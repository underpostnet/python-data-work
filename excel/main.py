import pandas as pd
import numpy as np



xl = pd.ExcelFile('data.xlsx')


data = [["sector", "pregunta", "respuesta"]]


for sheet in xl.sheet_names:
    
    df = xl.parse(sheet)
    
    dataSheet = np.array(df)
    headersSheet = np.array(df.columns)
    
    for row in dataSheet:
        # print(row)
        try:
            if row[3] == "Rutinaria":
                obj = [sheet, row[15], row[17]]
                # print(obj)
                data.append(obj)
        except IndexError:
            _ = ''
    
        


np.savetxt("consolidado.csv",  np.asarray(data), delimiter=";", fmt='%s')