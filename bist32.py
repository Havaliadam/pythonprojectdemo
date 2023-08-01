#import requests
#from bs4 import BeautifulSoup
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import KMeans,AgglomerativeClustering
import matplotlib.pyplot as plt 
import seaborn as sns 
from scipy.cluster.hierarchy import linkage,dendrogram

sonuc=pd.read_csv("C:/Users/ayhan/Desktop/veri.csv")

ms=MinMaxScaler()
x=ms.fit_transform(sonuc.iloc[:,[1,2]])
x=pd.DataFrame(x,columns=["gelir","oynaklik"])

model=AgglomerativeClustering(n_clusters=6,linkage="single")
tahmin=model.fit_predict(x)
labels=model.labels_

sonuc["labels"]=labels
sns.scatterplot(x="labels",y="hisse",data=sonuc,hue="labels",palette="deep")
plt.show()



#kmodel=KMeans(n_clusters=6,random_state=0)
#kfit=kmodel.fit(x)
#labels=kfit.labels_
#sonuc["labels"]=labels

#sns.scatterplot(x="labels",y="hisse",data=sonuc,hue=labels,palette="deep")
#plt.show()

#grafik=KElbowVisualizer(kmodel,k=(2,20))
#grafik.fit(x)
#grafik.poof()
#sonuc.to_csv("C:/Users/ayhan/Desktop/veri.csv",index=False)
#url="https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/Temel-Degerler-Ve-Oranlar.aspx?endeks=03#page-1"
#r=requests.get(url)
#print(r)
#s=BeautifulSoup(r.text, "html.parser")
#print(s)
#tablo=s.find("table",{"id":"summaryBasicData"})
#print(tablo)
#tablo=pd.read_html(str(tablo),flavor="bs4")[0]
#print(tablo)
#hisseler=[]
#for i in tablo["Kod"]:
 #   hisseler.append(i)
    
#parametreler=(
 #   ("hisse",hisseler[0]),
  ##  ("startdate","28-11-2020"),
    #("enddate","28-11-2022"))
#url2="https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil?"
#r2=requests.get(url2,params=parametreler).json()["value"]
#print(r2)
#veri=pd.DataFrame.from_dict(r2)
#print(veri)
#print(veri)
#veri=veri.iloc[:,0:3]
#print(veri)
#veri=veri.rename({"HGDG_HS_KODU":"hisse","HGDG_TARIH":"tarih","HGDG_KAPANIS":"fiyat"},axis=1)
#print(veri)
#data={"tarih":veri["tarih"],veri["hisse"][0]:veri["fiyat"]}
#veri=pd.DataFrame(data)

#del hisseler[0]
#tumveri=[veri]

#for j in hisseler:
 #   parametreler=(
  #  ("hisse",j),
   # ("startdate","28-11-2020"),
    #("enddate","28-11-2022"))
    #url2="https://www.isyatirim.com.tr/_layouts/15/Isyatirim.Website/Common/Data.aspx/HisseTekil?"
    #r2=requests.get(url2,params=parametreler).json()["value"]

    #veri=pd.DataFrame.from_dict(r2)

    #veri=veri.iloc[:,0:3]   

    #veri=veri.rename({"HGDG_HS_KODU":"hisse","HGDG_TARIH":"tarih","HGDG_KAPANIS":"fiyat"},axis=1)

    #data={"tarih":veri["tarih"],veri["hisse"][0]:veri["fiyat"]}
    #veri=pd.DataFrame(data)
    #tumveri.append(veri)
#print(tumveri)    

#df=tumveri[0]
#for son in tumveri[1:]:
 #   df=df.merge(son,on="tarih")
#veri=df.drop(columns="tarih",axis=1)
#gelir=veri.pct_change().mean()*252
#sonuc=pd.DataFrame(gelir)
#sonuc.columns=["gelir"]

#sonuc["oynaklik"]=veri.pct_change().std()*np.sqrt(252)
#sonuc=sonuc.reset_index()
#sonuc=sonuc.rename({"index":"hisse"},axis=1)


