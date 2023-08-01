
while True:
 try:
    boy=float(input("lütfen boyunuzu metre cinsinden giriniz(örnek:1.85):"))
    break

 except:
    print("lütfen sayisi doğru girin")
while True:
    try:
       kilo=float(input("lütfen kilonuzu giriniz(örnek:55):"))
       break

    except:
        print("lütfen değeri dogru giriz")
print(kilo/boy**2)