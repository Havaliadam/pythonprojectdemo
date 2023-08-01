from random import choice
class MP3Calar():
    def __init__(self,sarkilistesi= []):
        self.suancalarSarki=""
        self.ses=100
        self.sarkilistesi=sarkilistesi
        self.durum=True

    def sarkisec(self):
        sayac = 1
        for sarki in self.sarkilistesi:
            print ( "{}){}".format ( sayac ,
                                     sarki ) )
            sayac += 1
            secilensarki = int ( input ( "silmek istediğiniz sarkinin numarası giriniz" ) )
            while secilensarki < 1 or secilensarki > len ( self.sarkilistesi ):
                secilensarki = int ( input ( "silmek istediğiniz sarkinin numarası giriniz(1- {}".format ( self.sarkilistesi ) ) )
                self.suancalarSarki = self.sarkilistesi ( secilensarki - 1 )
def sesartir(self):
        if self.ses == 100:
            pass
        else:
self.ses +=10
def sesazalt(self):
        if self.ses == 0:
            pass
    else:
self.ses -= 10
def rastgelesarkisec(self):
        rssec = choice ( self.sarkilistesi )
        self.suancalarSarki = rssec
    def sarkiekle(self):
        sanatci = input ( "sanatci grubu giriniz" )
        sarki = input ( "sarki giriniz" )

        self.sarkilistesi.append ( sanatci + "-" + sarki )

    def sarkisil(self):
        sayac = 1
        for sarki in self.sarkilistesi:
            print ( "{}){}".format ( sayac ,
                                     sarki ) )
            sayac += 1
            silineceksarki = int ( input ( "silmek istediğiniz sarkinin numarası giriniz" ) )

            while silineceksarki < 1 or silineceksarki > len ( self.sarkilistesi ):
                silineceksarki = int ( input ( "silmek istediğiniz sarkinin numarası giriniz(1- {}".format ( self.sarkilistesi ) ) )
            self.sarkilistesi.pop ( silineceksarki - 1 )
    def kapat(self):
        self.kapa ()
    def menugoster(self):
     print("""
     ------Ayhan hosgeldiniz
    Sarki listesi:{}
    Suan çalan şarkı:{}
    Ses düzeyi:{}
    1)Sarki seç
    2)ses arttır
    3)ses azalt
    4)rastgele sarki seç
    5)sarki ekle
    6) sarki sil
    7) kapat
    """.format(self.sarkilistesi,self.suancalarSarki,self.ses))
    def secim(self):
        sec=int(input("seciminizi girin:"))

        while sec<1 or sec>7:
         sec = int ( input ( "seciminizi yanliş tekrar deneyeliniz(1-7):" ) )
         return sec

    def calistir(self):
    self.menugoster()
    secim=secim()
    if secim==1:
     self.sarkisec()
    if secim==2:
        self.sesartir()
if secim==3:
    self.sesazalt()
if secim==4:
 self.rastgelesarkisec()
 if secim==5:
  self.sarkiekle()
if secim==6:
 self.sarkisil()

if secim==7:
 self.kapat()

mp3calar=MP3Calar
while mp3calar.durum:
    mp3calar.calistir()
    print ( "program sonladı" )