import pandas as pd 
import re
import nltk
nltk.download("stopword")
nltk.download('all')
from nltk.corpus import stopwords
nltk.download("wordnet")
lema=nltk.WordNetLemmatizer()
import matplotlib.pyplot as plt 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
data=pd.read_csv("C:/Users/ayhan/Desktop/restoran.tsv",delimiter="\t")
veri=data.copy()
temiz=[]
for i in range(len(veri)):
    duzenle=re.sub('[^a-zA-Z]','',veri["Review"][i])
    duzenle=duzenle.lower()
    duzenle=duzenle.split()
    duzenle=[lema.lemmatize(kelime) for kelime in duzenle if not kelime in set(stopwords.words("english"))]
    duzenle=' '.join(duzenle)
    temiz.append(duzenle)
cv=CountVectorizer(max_features=1500)
matrix=cv.fit_transform(temiz).toarray()
#print(type(veri.iloc[:,1].values))
y=veri.iloc[:,1].values
x_train,x_test,y_train,y_test=train_test_split(matrix,y,test_size=0.2,random_state=0)
model=GaussianNB()
model.fit(x_train,y_train)
tahmin=model.predict(x_test)



model2=RandomForestClassifier(random_state=0)
model2.fit(x_train,y_train)
tahmin2=model2.predict(x_test)

skor=accuracy_score(y_test,tahmin)
print(skor*100)

skor2=accuracy_score(y_test,tahmin2)
print(skor2*100)

 
    
#df=pd.DataFrame(list(zip(veri["Review"],temiz)),columns=["orjinal yorum","temiz yorum"])



