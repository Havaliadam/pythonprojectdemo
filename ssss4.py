import pandas as pd 
import nltk
nltk.download('all')
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re 
nltk.download("wordnet")
lema=nltk.WordNetLemmatizer()
from sklearn.feature_extraction.text import CountVectorizer

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

cv=CountVectorizer(max_features=500)
matrix=cv.fit_transform(temiz).toarray()
matrixdf=pd.DataFrame(matrix,columns=cv.get_feature_name())
print(matrixdf)


