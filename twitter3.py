import snscrape.modules.twitter as sntwitter
import pandas as pd 
from openpyxl import Workbook,load_workbook
liste=[]

veri=sntwitter.TwitterSearchScraper("Borsa lang:tr").get_items()
for i in veri:
    if len(liste)==100:
        break
    else:
        liste.append([i.date,i.content])
        
df=pd.DataFrame(liste,columns=["Tarih","Twitter"])
tarihduzelt=df.select_dtypes(include=['datetime64[ns, UTC]']).columns
for i in tarihduzelt:
    df[i]=df[i].dt.date 
    df.to_excel("C:/Users/ayhan/Desktop/Twet.xlsx",df.to_csv,index=False) 