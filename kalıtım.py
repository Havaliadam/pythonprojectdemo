#class personel():
 #   def __add__(self, other):
  #      return 10+other

   # def __len__(self):
    #    for i in range(100):
     #       print(i)


#Personel=personel()
#print(Personel+100)

class Personel():
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
      self.ad=ad
      self.soyad=soyad
      self.yas=yas
      self.cinsiyet=cinsiyet
      self.maas=maas

    def bilgileriyazdir(self):
        print("""
         {} {} bilgileri sunlardır
         yas:{}
         cinsiyet:{}
         maas:{}
         """.format(self.ad,self.soyad,self.cinsiyet,self.yas,self.maas))
        def __str__(self):
           return """
         {} {} bilgileri sunlardır
         yas:{}
         cinsiyet:{}
         maas:{}
         """ .format(self.ad,self.soyad,self.cinsiyet,self.yas,self.maas)

personel=Personel("mert","demir","22","ERKEK","4500")
print(personel)
class Yönetici(Çalışan):

    def __init__(self, isim, yaş, maaş):
        super().__init__(isim, yaş, maaş)

        print("Yönetici sınıfının init fonksiyonu")

    def bilgileri_göster(self):
        super().bilgileri_göster()

        print(f"********* \nİsim: {self.isim} Bey yaş: {self.yaş} maaş: {self.maaş}\n*********")

Ahmet = Yönetici("Ahmet", 45, 5000)
Ahmet.bilgileri_göster()