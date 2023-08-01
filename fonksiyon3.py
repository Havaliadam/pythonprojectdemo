#def kucuk(a,b):
 #   if a<b:
  #      return a
   # elif b<a:
    #    return b
    #return a
#print(kucuk(10,20))
#print(min(10,20))


#def topla(*sayilar):
 #toplam=0
 #for sayi in sayilar:
  #   toplam+=sayi
   #  return toplam
#print(topla(50,60,70,80,90))
#def kuvvetal(sayi,kuvvet=2):
 #   return sayi**kuvvet
#print(kuvvetal(3,4))
#print("ayhan çelik","youtube",sep="********")
def degergoster(**degerler):
    for anahtar,deger in degerler.items():
        print(anahtar,deger)
degergoster(ayhan="mühendis",renk="kirmizi",yapi="dik")