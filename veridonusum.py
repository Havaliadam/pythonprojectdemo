#a=5.42

#print(type(int(a)))
#b=int(5.80)
#print(b)
#a="5000"
#print(int(a)+200)
#print("400"*4)#bunu dört kere yan yana yazdırdı
#print(400*3)
#print(int("500")*4)

#a="54545"
#b=int(a)
#sayi=123456789123
#print(len(str(sayi)))
a=int(input("sayi1:"))
b=int(input("sayi2:"))

secenek=int(input("1-topla\n2-cıkar\n3-carp\n4 bol"))
if secenek==1:
 print(a+b)
elif secenek==2:
    print(a-b)
elif secenek==3:
    print(a*b)
else:
 print(a/b)

