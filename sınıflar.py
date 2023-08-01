class Araba():
    def __init__(self,marka,model,fiyat,renk):

          self.gelenMarka=marka
          self.gelenModel=model
          self.gelenFiyat=fiyat
          self.gelenRenk=renk

    marka="renult"
    model="clio"
    fiyat=50_000
    renk="kırmızı"
    def __str__(self):
        return  self.bilgileriYazdir()

    def bilgileriYazdir(self):
     return self.gelenMarka+""+self.gelenModel+""+str(self.gelenFiyat)+""+self.gelenRenk+""
    def renkdegisti(self,renk):
        self.gelenRenk=renk



araba=Araba("ford","fiesta",50_000,"kırmızı")
araba2=Araba("fiat","linear",60_000,"yeşil")
araba.bilgileriYazdir()
araba.renkdegisti("yeşil")
print(araba)
araba2.bilgileriYazdir()
sayilar=[1,2,3,4,5,6]
sayilar.append(20)
print(sayilar)