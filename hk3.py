import pandas as pd 
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram,linkage
data=pd.read_csv("C:/Users/ayhan/Desktop/musteri.csv")
veri=data.copy()
#print(veri)
x=veri.iloc[0:20,2:4]
model=AgglomerativeClustering()
tahmin=model.fit_predict(x)
#print(veri)
#print(x)
x["label"]=tahmin
#print(x)
print(x["Age"][x["label"]==1])
plt.scatter(x["Age"][x["label"]==0],x["Annual Income (k$)"][x["label"]==0],c="red")
plt.scatter(x["Age"][x["label"]==1],x["Annual Income (k$)"][x["label"]==1],c="black")
plt.show()
link=linkage(x)
dendrogram(link)
plt.xlabel("veri noktaları")
plt.ylabel("mesafe")
plt.show()