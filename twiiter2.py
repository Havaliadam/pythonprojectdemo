import snscrape.modules.twitter as sntwitter
import pandas as pd 


liste=[]
veri=sntwitter.TwitterSearchScraper("Samsung near:Ankara").get_items()
for i in veri:
    if len(liste)==20:
        break
    else:
        liste.append(i.content)
df=pd.DataFrame(liste,columns=["Tweetler"])
print(df)        