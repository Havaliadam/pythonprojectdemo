import pandas as pd 
from 
data=pd.read_csv("C:/Users/ayhan/Desktop/Bakkal.csv",header=None)

veri=data.copy()
veri.columns=["Ürün"]
veri=list(veri["Ürün"].apply(lambda x:x.split(",")))
print(veri)