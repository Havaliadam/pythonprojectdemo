#yazi="tbmm"# elemanları parametre olarak almasını sağlar
#print(*yazi,sep=".")
def sayilartopla(*degerler):
    toplam=0
    for deger in degerler:
        toplam+=deger

    return toplam
sayilar=[x for x in range(1,1001)]
print(sayilartopla(*sayilar))