#def tamsayibolenler(sayi):
 #   bosliste=[]

  #  for i in range(1,sayi):
   #     if sayi%i==0:
    #     bosliste.append(i)


     #   return bosliste
#gelensayi=int(input("sayi giriniz"))
#print(tamsayibolenler(gelensayi))
def ekok(a,b):
    ekok=a*b
    for sayi in range(ekok,max(a,b)-1,-1):
        if sayi % a==0 and sayi%b==0:
            ekok=sayi
            return ekok

birincisayi=int(input("birinci sayi girin:"))
ikincisayi=int(input("ikinci sayi girin:"))
print(ekok(birincisayi,ikincisayi))