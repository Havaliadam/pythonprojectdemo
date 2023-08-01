import pandas as pd 
import numpy as np 
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt 
data=pd.read_csv("C:/Users/ayhan/Desktop/Maas.csv")

veri=data.copy()

y=veri["Salary"]
x=veri["Level"]

y=np.array(y).reshape(-1,1)
x=np.array(x).reshape(-1,1)
dtmodel=DecisionTreeRegressor(random_state=0)
dtmodel.fit(x,y)
dttahmin=dtmodel.predict(x)
rfmodel=RandomForestRegressor(random_state=0)
rfmodel.fit(x,y)
rftahmin=rfmodel.predict(x)

plt.scatter(x,y,color="red")
plt.plot(x,dttahmin,color="red")
plt.plot(x,rftahmin,color="green")
plt.show()

