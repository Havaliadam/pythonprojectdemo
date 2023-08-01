import pandas as pd
#import matplotlib.pyplot as plt 
import re 
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import numpy as np 
data=pd.read_csv("C:/Users/ayhan/Desktop/spam.csv",encoding="windows-1252")
veri=data.copy()
#print(veri)
veri=veri.drop(columns=["Unnamed: 2","Unnamed: 3", "Unnamed: 4"],axis=1)
#print(veri)
veri=veri.rename(columns={"v1":"etiket","v2":"sms"})
#print(veri.groupby("etiket").count())

veri=veri.drop_duplicates()
veri["karakter sayisi"]=veri["sms"].apply(len)
#print(veri)
#veri.hist(column="karakter sayisi",by="etiket",bins=50)
#plt.show() görselleştirme


veri.etiket=[1 if kod=="spam" else 0 for kod in veri.etiket]
#print(veri)

def harfler(cumle):
    yer=re.compile("[^a-zA-Z]")
    return re.sub(yer," ",cumle)
#print(harfler(",,?tuy,,RFT11"))
#print(veri["sms"][0])
#print(harfler(veri["sms"][0]))

durdurma=stopwords.words("english")
#print(durdurma)

spam=[]
ham=[]
tumcumleler=[]
for i in range(len(veri["sms"].values)):
    r1=veri["sms"].values[i]
    r2=veri["etiket"].values[i]
    
    
    temizcumle=[]
    cumleler=harfler(r1)
    cumleler=cumleler.lower()
   
    
    for kelimeler in cumleler.split():
        temizcumle.append(kelimeler)
        
        if r2==1:
            spam.append(cumleler)
        else:
            ham.append(cumleler)
            
            tumcumleler.append(" ".join(temizcumle))
            
veri["Yeni Sms"]=tumcumleler
 
veri=veri.drop(columns=["sms","karakter sayisi"],axis=1)
                   
                    
print(veri)
cv=CountVectorizer()
x=cv.fit_transform(veri["Yeni Sms"]).toarray()
y=veri["etiket"]
X=x        
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

for i in np.arange(0.0,1.1,0.1):
    model=MultinomialNB(alpha=i)
    model.fit(x_train,y_train)
    tahmin=model.predict(x_test)
    skor=accuracy_score()
    print("alpha {} değeri için skor:{}".format(round(i,1),round(skor*100,2)))
    
    


#model=MultinomialNB()
#model.fit(x_train,y_train)
#tahmin=model.predict(x_test)

#acs=accuracy_score(y_test,tahmin)
#print(acs*100)

 