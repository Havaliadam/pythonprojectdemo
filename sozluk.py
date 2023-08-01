#sozluk={}
#print(type(sozluk))
#kisiler={"melis":20,"mahmut":40,"ali":50,"mehmet":35,"melike":80}
#print(kisiler["ali"])
#uyeler={"üye":{"ayhan","mehmet","hakkı"},"modaretor":{"xxxxx","ela","ali"},"yönetici":{"dark","mavi","yeşil"}}
#print(type(uyeler))
#print(uyeler["üye"])
uyeler={"üye":{"ayhan","mehmet","hakkı"},"modaretor":{"xxxxx","ela","ali"},"yönetici":{"dark","mavi","yeşil"}}
while True:
    islem=int(input("yapmak istediğiniz işlemi seçiniz:\n1-kişi kaldır\n2-kişi ekle"))
    if islem==1:
        yetki=input("yetkiyi kaldınız(üye,modaretor,yonetici")
        if yetki=="üye":
            print(uyeler["üye"])
            isim=input("kaldırmak istediğiniz uyenin nick name")
            uyeler["üye"].remove(isim)
            if yetki=="modaretor":
                print ( uyeler["modaretor"] )
                isim = input ( "kaldırmak istediğiniz uyenin nick name" )
                uyeler["modaretor"].remove ( isim )
                if yetki=="yonetici":
                    print ( uyeler["yönetici"] )
                    isim = input ( "kaldırmak istediğiniz uyenin nick name" )
                    uyeler["yönetici"].remove ( isim )
                    print ( uyeler )

                elif islem==2:
                    yetki = input ( " eklemek yetkiyi kaldınız(üye,modaretor,yonetici" )
                    if yetki == "üye":
                        print ( uyeler["üye"] )
                        isim = input ( "ekle istediğiniz uyenin nick name" )
                        uyeler["üye"].append(isim)
                        if yetki == "modaretor":
                            print ( uyeler["modaretor"] )
                            isim = input ( "ekleme istediğiniz uyenin nick name" )
                            uyeler["modaretor"].append(isim)
                            if yetki == "yonetici":
                                print ( uyeler["yönetici"])
                                isim = input ("eklemek istediğiniz uyenin nick name" )
                                uyeler["yönetici"].append(isim)
                                print(uyeler)
        else:
             break
print(uyeler)