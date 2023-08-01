import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from  sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,roc_curve,roc_auc_score
import matplotlib.pyplot as plt  
data=pd.read_csv("C:/Users/ayhan/Desktop/Kanser.csv")

veri=data.copy()

veri=veri.drop(columns=["id","Unnamed: 32"],axis=1)
#print(veri)
veri.diagnosis=[1 if kod=="M" else 0 for kod  in veri.diagnosis]
#print(veri)
y=veri["diagnosis"]
x=veri.drop(columns="diagnosis",axis=1)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)
model=LogisticRegression(random_state=0)
model.fit(x_train,y_train)
tahmin=model.predict(x_test)
#print(tahmin)

cm=confusion_matrix(y_test,tahmin)
print(cm)
ac=accuracy_score(y_test,tahmin)
print(ac)
cr=classification_report(y_test,tahmin)
print(cr)

auc=roc_auc_score(y_test,tahmin)
fpr,tpr,tresold=roc_curve(y_test,model.predict_proba(x_test)[:,1])
plt.plot(fpr,tpr,label="model auc(alan=%0.2f)"% auc)
plt.plot([0,1],[0,1],"r--")
plt.xlabel("false postivi oranı")
plt.ylabel("true positive oranı")
plt.title("ROC")
plt.legend(loc="lower right")
plt.show()