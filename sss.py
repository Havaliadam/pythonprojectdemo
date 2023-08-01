import pandas as pd 
import nltk
nltk.download('all')
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re 
nltk.download("wordnet")
import matplotlib.pyplot as plt
from word
lema=nltk.WordNetLemmatizer()
data=pd.read_csv("C:/Users/ayhan/Desktop/spam.csv",encoding="windows-1252")
veri=data.copy()

veri=veri.drop(columns=["Unnamed: 2","Unnamed: 3", "Unnamed: 4"],axis=1)
veri=veri.rename(columns={"v1":"etiket","v2":"sms"})


temiz=[]
ps=PorterStemmer()
for i in range(len(veri)):
    duzenle=re.sub('[^a-zA-Z]',' ',veri["sms"][i])
    duzenle=duzenle.lower()
    duzenle=duzenle.split()
    duzenle=[lema.lemmatize(kelime) for kelime in duzenle if not kelime in set(stopwords.words("english"))]
    duzenle=' '.join(duzenle)
    temiz.append(duzenle)

df=pd.DataFrame(list(zip(veri["sms"],temiz)),columns=["orjinal sms","temiz sms"])


frekans=(df["temiz sms"]).apply(lambda x:pd.value_counts(x.split(" "))).sum(axis=0).reset_index()
frekans.columns=["kelimeler","frekans"]










#veri2=veri["sms"].str.replace("[^\w\s]","",regex=True)
#veri3=veri2.str.lower()
#veri4=veri3.str.replace("[\d]","",regex=True)
#etkisiz=stopwords.words("english")
#ayır=veri4.str.split()

#veri5=veri4.apply(lambda x:" ".join(x for x in x.split() if x not in etkisiz))
#ps=PorterStemmer()
#print(ps.stem("waiting"))



