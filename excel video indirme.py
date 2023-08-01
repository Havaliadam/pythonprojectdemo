def sayilaritopla(sayilar):
    if type(sayilar)!=list:
        raise TypeError("parametre listesi objesi olmalı")

    toplam=0
    for i in sayilar:
     toplam+=i
    return toplam

#try:
 #  print(sayilaritopla([1,2,3,4,5,6]))
#except TypeError:
 #   print("buraya girdi")


