from turtle import color
import pandas as pd 
import matplotlib.pyplot as plt 


data=pd.read_csv("C:/Users/ayhan/Desktop/Kanser.csv")

veri=data.copy()

M=veri[veri["diagnosis"]=="M"]
B=veri[veri["diagnosis"]=="B"]

plt.scatter(M.radius_mean,M.texture_mean,color="red",label="kötü huylu tümör")
plt.scatter(B.radius_mean,B.texture_mean,color="green",label="iyi huylu tümör")
plt.legend()
plt.show()