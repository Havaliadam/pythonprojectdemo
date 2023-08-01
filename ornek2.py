def ogrenci_yazdir():
    vize = float ( input ( "vize notunuzu giriniz:" ) )
    final = float ( input ( "final notunuzu giriniz:" ) )
    bilgi = input ( "ad soyad :" )
    ortalama = vize * 0.4 + final * 0.6
    harf_notu = ""
    if ortalama >= 85:
        harf_notu = "AA"
    elif ortalama >= 70:
        harf_notu = "BB"
    elif ortalama >= 55:
        harf_notu = "CC"
    else:
        harf_notu = "FF"
    with open ( "notlar.txt" ,
                "w" ) as dosya:
        dosya.writelines ( "{} adlı öğrencinin bu derste elde ettiği harf notu: {}".format ( bilgi ,
                                                                                             harf_notu ) )
kac_ogrenci=int(input("kaç öğrenciyi gireceksiniz"))

for i in range(kac_ogrenci):
    ogrenci_yazdir()
