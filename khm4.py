import pandas as pd 
from scipy.cluster.hierarchy import dendrogram,linkage
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.cluster import AgglomerativeClustering
data=pd.read_csv("C:/Users/ayhan/Desktop/iris.csv")
veri=data.copy()
print(veri)
x=veri.drop(columns=["150","4"],axis=1)
print(x)
hcsingle=linkage(x,method="single")
hccomplete=linkage(x,method="complete")
hcaverage=linkage(x,method="average")
hccentroid=linkage(x,method="centroid")
hcmedian=linkage(x,method="median")
hcward=linkage(x,method="ward")
model=AgglomerativeClustering(n_clusters=2,linkage="median")
tahmin=model.fit_predict(x)

print(x)

labels=model.labels_
print(labels)
sns.scatterplot(x="setosa",y="versicolor",data=x,hue=labels,palette="deep")
plt.show()