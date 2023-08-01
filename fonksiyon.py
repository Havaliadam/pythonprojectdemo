#def topla(sayi,yazi):
 #   for i in range(sayi):
  #   print(yazi)
#topla(50,"python")
def ortakbolen(sayi1,sayi2):
    enkucuksayi=min(sayi1,sayi2)
    enbuyukortakbolen=1

    for i in range(1,enkucuksayi+1):
        if sayi1%i==0 and sayi2%i==0:
            enbuyukortakbolen=i
            print(f"{sayi1} ve {sayi2} en buyuk ortan bölen :{enbuyukortakbolen} dir")
ortakbolen(70,40)