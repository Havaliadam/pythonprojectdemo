import pandas as pd 

data=pd.read_excel("C:/Users/ayhan/Desktop/Eticaret.xlsx")
data.to_csv("C:/Users/ayhan/Desktop/Eticaret.csv",index=False)

