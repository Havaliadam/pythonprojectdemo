#sayi=1
#while sayi<10_000:
#print(sayi)
#sayi+=1
#for sayi in range(10_000):
#print(sayi)
#for i in range(1000):
 #print(i)
#for i in range(20,1000):
#print(i)
#for i in range(100,1000,5):
#print(i)
#sayi=1
#for sayi in range(1,100,2):
#print(sayi)
def asal_mi(sayi):
    for i in range(2,sayi):
        if sayi%i==0:
            return False
        return True
sayi=int(input("sayi giriniz:"))
asal_Sayilar=[]

for i in range(2,sayi+1):
    if asal_mi(i):
        asal_Sayilar.append(i)

print(len(asal_Sayilar))