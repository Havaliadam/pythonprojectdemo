import snscrape.modules.twitter as sntwitter

import pandas as pd 
from itertools import islice

df=pd.DataFrame(islice(sntwitter.TwitterSearchScraper("Borsa").get_items(),1))
print(df.columns)


veri=sntwitter.TwitterSearchScraper("Borsa").get_items()
icerik=[]
for i in veri:
  if len(icerik)==50:
      break
  else:
      icerik.append([i.url,i.date,i.content])

df=pd.DataFrame(icerik,columns=["Link","Tarih","Tweetler"])
tarih=df.select_dtypes(include=['datetime64[ns, UTC]']).columns

for i in tarih:
    df[i]=df[i].dt.date 
    
print(df)    

    

