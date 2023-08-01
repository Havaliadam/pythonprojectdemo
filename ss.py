import pandas as pd 
import re
data=pd.read_csv("C:/Users/ayhan/Desktop/spam.csv",encoding="Windows-1252")
veri=data.copy()
veri=veri.drop(columns=["Unnamed: 2","Unnamed: 3", "Unnamed: 4"],axis=1)
veri=veri.rename(columns={"v1":"etiket","v2":"sms"})

veri2=veri["sms"].str.replace("[^\w\s]","")
veri3=veri2.str.lower()
veri4=veri2.str.replace("[\d]","")
#veri3=re.sub('[^a-zA-Z]'," ",veri["sms"][0])
print(veri3)
print(veri4)

