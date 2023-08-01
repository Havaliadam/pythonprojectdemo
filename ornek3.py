#sayi=int(input("bir sayi değer giriniz:"))

#faktoriyel=1
#for i in range(1,sayi+1):
 #   faktoriyel=faktoriyel*i
  #  print("{}!".format(sayi)+str(faktoriyel))

sahipolanPara=2000
secim=input("kartı sokmak içim 's',ayrılmak için 'a'yazınız")

if secim=="s":
 while True:
   islem=int(input(""" 
   işlemler
   ---------------
   1-para çekme
   2-para yatırma
   3-kart bilgileri
   4-kart idade
   yapmak istediğiniz işlemini numarası girin
   """))
   if islem==1:
       cekilecekparamiktari=int(input("çekmek istediğniz para miktari çekiniz"))
       if sahipolanPara<cekilecekparamiktari:
           print("limit yetersiz")
       else:
           sahipolanPara-=cekilecekparamiktari
           if islem==2:
               yatiracakparamiktari=int(input("para tutarını giriniz"))
               sahipolanPara+=yatiracakparamiktari
               if islem==3:
                   print("hesap bilgileri\n**********\nhesap sahibi:ayhan çelik\nhesab ıban:TR80XXXXXXXXXXX\n sahip olunan para {}".format(sahipolanPara))
                   if islem==4:
                       print("karti iade alınız")
                       break
                   else:
                       print("atmden ayrılınız")