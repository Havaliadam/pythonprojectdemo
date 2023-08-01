yazi="www.mertmekatronik.com sitesinde ,bir sürü makale ve döküman var"
print(yazi.upper())
print(yazi.lower())
print(yazi.replace("döküman","kod"))
print(yazi.startswith("www"))
print(yazi.endswith("var"))
print(yazi.split("."))

print(yazi.strip("www"))
print(yazi.find("mertmekatronik"))


yazi2="""

Girintilere dayalı basit söz dizimi, dilin öğrenilmesini ve akılda kalmasını kolaylaştırır. Bu da ona söz diziminin ayrıntıları ile vakit yitirmeden programlama yapılmaya başlanabilen bir dil olma özelliği kazandırır.

Modüler yapısı, sınıf dizgesini (sistem) ve her türlü veri alanı girişini destekler. Hemen hemen her türlü platformda çalışabilir (Unix, Linux, Mac, Windows, Amiga, Symbian). Python ile sistem programlama, kullanıcı arabirimi programlama, ağ programlama, web programlama, uygulama ve veri tabanı yazılımı programlama gibi birçok alanda yazılım geliştirebilirsiniz. Büyük yazılımların hızlı bir şekilde prototiplerinin üretilmesi ve denenmesi gerektiği durumlarda da C ya da C++ gibi dillere tercih edilir.








"""
print(yazi2.count("a"))
yazi3="Mert30,Ece42,Mustafa18,Dilay20,Tolga27,Mahmut29,Melis42"
print("-".join(yazi3.split(",")))
