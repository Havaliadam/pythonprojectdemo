import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
data=pd.read_csv("C:/Users/ayhan/Desktop/Kanser.csv")
veri=data.copy()

veri=veri.drop(columns=["id","Unnamed: 32"])

veri.diagnosis=[1 if kod== "M" else 0 for kod in veri.diagnosis]

#print(veri)
y=veri["diagnosis"]
x=veri.drop(columns="diagnosis",axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

nbg=GaussianNB()
nbg.fit(x_train,y_train)
tahmin=nbg.predict(x_test)
acs=accuracy_score(y_test,tahmin)
print(acs*100)
