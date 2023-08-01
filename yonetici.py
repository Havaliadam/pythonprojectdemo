class Personel():
    def __init__(self,ad,soyad,yas,cinsiyet,maas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.cinsiyet=cinsiyet
        self.maas=maas

    def bilgiyi_yazdir(self):
        print(f" isim:{self.ad} yas:{self.yas},maas:{self.maas}")
personel=Personel("mehmet","demir","22","erkek","4500")
personel.bilgiyi_yazdir()

class Yonetici(Personel):
    pass
personel=Yonetici("hakkı","demir","45","erkek","80000")
personel.bilgiyi_yazdir()