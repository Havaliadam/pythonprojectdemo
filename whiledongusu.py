#a=10
#while(a>0):
    #print(a)
    #print("burasi döngü içi")

    #a-=1

    #print("döngü disi")
#liste=[1,2,"ayhan",5,6,"mühendis",True]
#liste_uzuluk=len(liste)
#sayac=0
#while sayac< liste_uzuluk:
 #   print(liste[sayac])

  #  sayac+=1

import random
yaziGelen=0
turaGelen=0
parayuzeyi=["tura","yazi"]
atilacakpara=int(input("kaç kere para atacaksiniz:"))
while atilacakpara>0:
   paraustu=random.choice(parayuzeyi)
   if paraustu=="tura":
       turaGelen+=1
       print("tura  geldi!")
   else:
       yaziGelen+=1
       print("yazi geldi!")
       atilacakpara-=1
       print("tura sayisi:{}\n yazı sayısı:{}".format(yaziGelen,turaGelen))
