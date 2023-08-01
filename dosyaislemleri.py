dosya=open("planlar.txt","r",encoding="utf-8")
#print(dosya.read(14))
#print(dosya.readline(50))#bulunduğu saturu okur
#print(dosya.read(20))
#print(dosya.readlines()[0])
#print(dosya.read(50))
#print(dosya.tell())# nerede oldugu soyle
#print(dosya.seek(8))
dosya.seek(5)
print(dosya.read(8))
dosya.write("asdadas")

dosya.close()
