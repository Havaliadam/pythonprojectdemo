import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
data=pd.read_csv("C:/Users/ayhan/Desktop/Kanser.csv")

veri=data.copy()
#print(veri)

veri=veri.drop(columns=["id","Unnamed: 32"],axis=1)
#print(veri.info())

y=veri["diagnosis"]
x=veri.drop(columns="diagnosis",axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

model=LogisticRegression(random_state=0)
model.fit(x_train,y_train)
tahmin=model.predict(x_test)
print(tahmin)
