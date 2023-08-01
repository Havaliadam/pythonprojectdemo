import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
import datetime as dt 
from sklearn.preprocessing import MinMaxScaler
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans
data=pd.read_csv("C:/Users/ayhan/Desktop/Müsteriler.csv")
veri=data.copy()
veri=veri.dropna()
veri["total"]=veri["Quantity"]*veri["UnitPrice"]
veri=veri.drop(veri[veri["total"]<=0].index)
#sns.boxplot(veri["total"])
#plt.show()
Q1=veri["total"].quantile(0.25)
Q3=veri["total"].quantile(0.75)
IQR=Q3-Q1

altsinir=Q1-1.5*IQR
ustsinir=Q3+1.5*IQR

veri=veri[~~((veri["total"]>ustsinir) | (veri["total"]<altsinir))]
veri=veri.reset_index(drop=True)
#print(len(veri["CustomerID"].unique()))
#print(veri["InvoiceNo"].nunique())
veri["CustomerID"]=veri["CustomerID"].astype("int")
veri["InvoiceDate"]=pd.to_datetime(veri["InvoiceDate"])
#print(veri.info())
bugün=veri["InvoiceDate"].max()
bugün=dt.datetime(2011,12,9,12,49,0)
r=(bugün-veri.groupby("CustomerID").agg({"InvoiceDate":"max"})).apply(lambda x:x.dt.days)
f=veri.groupby(["CustomerID","InvoiceNo"]).agg({"InvoiceNo":"count"})
f=f.groupby("CustomerID").agg({"InvoiceNo":"count"})

m=veri.groupby("CustomerID").agg({"total":"sum"})

RMF=r.merge(f,on="CustomerID").merge(m,on="CustomerID")
RMF=RMF.reset_index()
RMF=RMF.rename(columns={"CustomerID":"Customer","InvoiceDate":"Recency","InvoiceNo":"Frequency","total":"Monetary"})


df=RMF.iloc[:,1:]


sc=MinMaxScaler()
dfnorm=sc.fit_transform(df)
dfnorm=pd.DataFrame(dfnorm,columns=df.columns)
kmodel=KMeans(random_state=0,n_clusters=4,init="k-means++")
kfit=kmodel.fit(df)
labels=kfit.labels_
RMF["labels"]=labels

print(RMF.groupby("labels").mean().iloc[:,1:])





#sns.scatterplot(x="labels",y="Customer",data=RMF,hue=labels,palette="deep")
#plt.xlim([-1,5])
#plt.show()
