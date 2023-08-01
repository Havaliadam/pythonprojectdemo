from statistics import linear_regression
import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,Ridge,Lasso,ElasticNet
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor ,RandomForestRegressor
import sklearn.metrics as mt
data=pd.read_csv("C:/Users/ayhan/Desktop/Reklam.csv")

veri=data.copy()

#print(veri.isnull().sum())

y=veri["Sales"]
x=veri.drop(columns="Sales",axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=42)

def modeltahmin(model):
    model.fit(x_train,y_train)
    tahmin=model.predict(x_test)
    r2=mt.r2_score(y_test,tahmin)
    rmse=mt.mean_squared_error(y_test,tahmin,squared=False)
    return [r2,rmse]

modeller=[LinearRegression(),Ridge(),Lasso(),ElasticNet(),SVR(kernel="linear"),DecisionTreeRegressor(random_state=0),BaggingRegressor(random_state=0),RandomForestRegressor(random_state=0)]
ad=["Linear Model","Ridge Model","Lasso model","Elasticnet model","SVR MODEL","karar agaci model","bag model","Random forest model"]


sonuc =[]

for i in modeller:
    sonuc.append(modeltahmin(i))
    
 
 
df=pd.DataFrame(ad,columns=["model ad"])
df2=pd.DataFrame(sonuc,columns=["R2","RMSE"])

df=df.join(df2)
print(df)




#print(df2)
 
 
 
 
#print(sonuc)   




# print(modeltahmin(LinearRegression()))

#print(modeltahmin(LinearRegression()))