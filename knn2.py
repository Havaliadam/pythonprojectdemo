import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
data=pd.read_csv("C:/Users/ayhan/Desktop/Kanser.csv")
veri=data.copy()
#print(veri)


veri=veri.drop(columns=["id","Unnamed: 32"],axis=1)
#print(veri)

veri.diagnosis=[1 if kod=="M"else 0 for kod in veri.diagnosis]
#print(veri)
y=veri["diagnosis"]
x=veri.drop(columns="diagnosis",axis=1)
#print(veri)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

model=KNeighborsClassifier(n_neighbors=9)
model.fit(x_train,y_train)
tahmin=model.predict(x_test)
acs=accuracy_score(y_test,tahmin)
print(acs)


#basari=[]

#for k in range(1,20):
    #knn=KNeighborsClassifier(n_neighbors=k)
    #knn.fit(x_train,y_train)
    #tahmin2=knn.predict(x_test)
    #basari.append(accuracy_score(y_test,tahmin2))
    #print(basari)11
    #print(max(basari))
     
#plt.plot(range(1,20),basari)
#plt.xlabel("k")
#plt.ylabel("Basari puanlari")
#plt.show()