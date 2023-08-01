def yazdir(kisilistesi):
  yeniliste=[]
  for kisi in kisilistesi:
      yeniliste.append(kisi.strip().lower().capitalize())

  for kisi in yeniliste:
    sayi=yeniliste.count(kisi)
    if sayi>=2:
        print(kisi)
    for i in range(sayi):
      yeniliste.remove(kisi)

kisiler=["mehmet","mert","ali","tuncay","MehmET","mehmet    ","MeRt","Ecem","kaya","demir","ela","Ela","melisa"]
yazdir(kisiler)