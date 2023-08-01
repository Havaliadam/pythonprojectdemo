class Sirket():
    def __init__(self,ad):
        self.ad=ad
        self.calisma=True
    def program(self):
        secim=self.menusecim()
        if secim ==1:
         self.calisanekle()
         if secim==2:
          self.calisancikar()
          if secim==3:
              ay_yil_secim=input("yıllık bazda görmek istermisiniz(E/H)")
              if ay_yil_secim=="e":
                  self.verilecekmaas(hesap="y")

           self.verilecekmaas()
        if secim==4:
            self.maasver()
            if secim==5:
               self.masrafgir()
            if secim==6:
                 self.gelirgir()

    def menusecim(self):
        secim=int(input("******{} otomasyona hoş geldiniz****\n\n1-çalışan ekle\n2-çalışan çıkar\n3-verielecekmaas\n4-maas ver\n5-masraf gir\n6-gelir gir\n seciminizi girin:".format(self.ad)))
        while secim< 1 or secim> 6:
            secim=int(input("lütfen 1-6 arasında deger giriniz"))

        return secim
    def calisanekle(self):
        id=1
        ad=input("çalışan adını giriniz")
        soyad=input("çalısan soyadını giriniz")
        yas=input("calışan yaşını giriniz")
        cinsiyet=input("çalişan çinsiyeti giriniz")
        maas=input("çalışan maaşını girinizi")
        with open("calışan.txt","r")as dosya:
            calisan_listesi=dosya.readlines()
            if len(calisan_listesi)==0:
                id=1
            else:
                with open("calışan.txt","r")as dosya:
                     id=int(dosya.readlines()[-1].split(")")[0])+1



        with open("calışan.txt","a+")as dosya:
            dosya.write("{}-{}-{}-{}-{}-{}\n".format(id,ad,soyad,yas,cinsiyet,maas))

    def calisancikar(self):
        with open("calışan.txt","r")as dosya:
           calisanlar=dosya.readlines()
           gcalisan=[]
        for calisan in calisanlar:
         gcalisan.append("".join(calisan[:-1].split("-")))
        for calisan in gcalisanlar:
            print(calisan)

            secim=int(input("lütfen çıkarmak istediğniz çalışanın numarasını giriniz(1-{}".format(gcalisan)))
            while secim <1 or secim>len(gcalisan):
             secim = int ( input ("lütfen (1-{}) arasına numara giriniz".format ( gcalisan ) ) )
            calisanlar.pop(secim-1)
            sayac=1
            msayi=len(calisanlar)
            dcalisan=[]
            for calisan in calisanlar:
             dcalisan.append(str(sayac)+")"+calisan.split(")")[1])
             sayac+=1
            with open("calışan.txt","w")as dosya:
                dosya.writelines(dcalisan)
    def verilecekmaas(self,hesap="a"):
        """hesap :a ise aylık,y ise yıllık:hesap"""
       with open("calışan.txt","r")as dosya:
        calisan=dosya.readlines()
        maaslar={}
        maaslar.append(int(calisan.split("-")[-1]))
    if hesap=="a":
    print("toplam bu ayki maaş ".format(sum(maaslar)))
    else:
    print ( "toplam bu ayki maaş ".format ( sum ( maaslar ))*12 )
     def maasver(self):
         with open ( "calışan.txt" ,
                     "r" ) as dosya:
             calisan = dosya.readlines ()
             maaslar = {}
             maaslar.append ( int ( calisan.split ( "-" )[-1] ) )
             toplammaas=sum(maaslar)
         if hesap == "a":
             print ( "toplam bu ayki maaş ".format ( sum ( maaslar ) ) )
          else:
             print ( "toplam bu ayki maaş ".format ( sum ( maaslar ) ) * 12 )
            with open("bütce.txt","r")as dosya:
            tbutce=int(dosya.readlines())[0]
    tbutce=tbutce-toplammaas
         with open("bütce.txt","w")as dosya:
         dosya.write(str(tbutce))


    def masrafgir(self):
        pass
    def gelirgir(self):
        pass


sirket=Sirket("ayhan çelik")

while sirket.calisma:
  sirket.program()