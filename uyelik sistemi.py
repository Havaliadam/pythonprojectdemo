import json
from random import randint

class sistem:
    def __init__(self):
        self.durum=True
        self.veriler=self.verilerial()
    def calistir(self):
        self.menuGoster()
        secim=self.menusecimiyap()
        if secim==1:
         self.girisyap()
        if secim==2:
            self.kayitol()
        if secim==3:
            self.sifremiunuttum()
        if secim==4:
            self.cikis()

    def menuGoster(self):
        print("""
        1-Giriş yap
        2-Kayıt ol
        3-Sifre unuttum
        4-Çıkış
        
        """)

    def menusecimiyap(self):
        while True:
            try:
                secim=int(input("Seçimi girin"))
                while secim<1 or secim>4:
                    secim = int (input("lütfen 1-4 arası değer girin"))
                    break
            except ValueError:
                print("lütfen sayi girin\n")

            return secim
    def girisyap(self):
        kadi=input("adınızı girin")
        sifre=input("sifrenizi girin")
        durum=self.kontrolet(kadi,sifre)
        if durum:
         self.girisbasarili()
        else:
            self.girisbasarisiz(" bilgiler yanlış")
    def kayitol(self):
        kadi=input("adinizi girin")
        while True:
         sifre=input("sifrenizi girin")
         tsifre=input("sifrenizi girin")

         if sifre==tsifre:
             break
         else:
             print("sifreler aynı değil tekrar deneyin")
        email=input("email giriniz")
        durum=self.kayitvarmi(kadi,email)
        if durum:
            print("kullanici adi veya email kayıtlı")
        else:
          aktivasyonkodu=self.aktivasyonKodugonder()
          akdurum=self.aktivasyonKontrolet(aktivasyonkodu)


        if akdurum:
                self.kaydet(kadi,sifre,email)
        else:
            print("kod geçersiz")


    def sifremiunuttum(self):
        email=input("email girin")
        if self.mailvarmi(email):
            with open("aktivasyon.txt","w")as dosya:
                aktivasyon=str(randint(1000,9999))
                dosya.write(aktivasyon)


        else:
            print("böyle bir email yok")
        akgir=input("sifreni değiştirmek için aktivasyon kodu girin")

        if akgir==aktivasyon:
            while True:
                yenisifre=input("yeni şifre girin")
                yenisifret = input ( "yeni şifre giriniz" )

                if yenisifre==yenisifret:
                    break

                else:
                    print("girdiğiniz şifre ayni değil tekrar girin")
            self.veriler = self.verilerial ()
            for kullanicilar in self.veriler["kullanici"]:
                if kullanicilar["email"] == email:
                  kullanicilar["sifre"] == str (yenisifre)

                with open("kullanici.json","w")as dosya:
                    json.dump(self.veriler,dosya)
                    print("sifre değiştirdi")
    def mailvarmi(self,email):
        self.veriler=self.verilerial()

        for kullancilar in self.veriler["kullanici"]:
            if kullancilar["email"]==email:
                return True
            else:
                return False
    def cikis(self):
        self.durum=False
    def kontrolet(self,kadi,sifre):
        self.veriler=self.verilerial()

        for kullanicilar in self.veriler["kullanici"]:
         if kullanicilar["kadi"]== kadi and kullanicilar["sifre"]==sifre and kullanicilar["timeout"]=="0" and kullanicilar["aktivasyon"]=="y":
            return True
         return False


    def timeoutvarmi(self):
        pass
    def aktifmi(self):
        pass
    def girisbasarisiz(self,sebep):
         print(sebep)
    def girisbasarili(self):
        print("hosgeldiniz")
        self.durum=False
    def kayitvarmi(self,kadi,mail):
        self.veriler=self.verilerial()
        try:
            for kullanicilar in self.veriler["kullanici"]:
                if kullanicilar["kadi"] == kadi and kullanicilar["mail"]==mail:
                    return True
        except KeyError:
            return False

        return False


    def kayitbasarisiz(self,sebep):
        pass
    def aktivasyonKodugonder(self):
        with open("aktivasyon.txt","w")as dosya:
         aktivasyon=(str(randint(1000,9999)))
         dosya.write(aktivasyon)
        return aktivasyon
    def aktivasyonKontrolet(self,aktivasyon):
        aktivasyonkodual=input("aktivasyon kodu girin")
        if aktivasyon==aktivasyonkodual:
            return True
        else:
            return False
    def kaydet(self,kadi,sifre,email):
        self.veriler=self.verilerial()
        try:
            self.veriler["kullanici"]=[]
            self.veriler["kullanici"].append({"kadi":kadi,"sifre":sifre,"mail":email,"aktivasyon":"y","timeout":"o"})
        except KeyError:
            self.veriler["kullanici"].append({"kadi":kadi,"sifre":sifre,"mail":email,"aktivasyon":"y","timeout":"o"})

        with open("kullanici.json","w")as dosya:
            json.dump(self.veriler,dosya)
            print("kayıt oluştu")

    def sifredegistir(self):
        pass
    def verilerial(self):
        try:
            with open("kullanici.json","r")as dosya:
                veriler=json.load(dosya)
        except FileNotFoundError:
            with open("kullanici.json","w")as dosya:
               dosya.write("{}")
        print(veriler)
        return veriler



Sistem=sistem()

while Sistem.durum:
    Sistem.calistir()













#import json
#with open("veriler.json","r")as dosya:
 #   veriler=json.load(dosya)
  #  for kullanici in veriler["kullancilar"]:
   #     if kullanici["kadi"]=="McKarakule42":
    #        print(kullanici["sifre"])

#veriler = {}

# veriler["kullancilar"]=[]
# veriler["kullancilar"].append({"kadi":"McKarakule42","sifre":"123456","mail":"mcKarakule@gmail.com"})
# veriler["kullancilar"].append({"kadi":"McKara42","sifre":"123456mm","mail":"Kara42@gmail.com"})

# with open("veriler.json","w")as dosya:
# json.dump(veriler,dosya)
