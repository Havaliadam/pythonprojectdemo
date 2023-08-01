
#def islem(b,c):
 #   print(a)
  #  return b*c*a
#a=10
#print(islem(4,5))
#def bol(a,b):
 #   print(a/b)
  #  c=10
#bol(12,3)
#print(c)
#c=10
#def carp(a,b):
 #   c=5
  #  print("fnk içinde c:",c)
   # print(a*b)
#carp(2,9)
#print("fnk dısında c:",c)

c = 10

#def carp(a,b):

#	global c
#	c = 5

#	print("fonksiyonun içinde c : ",c)
#	print(a*b)

#carp(2,9)
#print("fonksiyonun dışında c : ",c)
def kuvvet_al(taban,kuvvet):
    return taban**kuvvet
print(kuvvet_al(4,3))

tek_mi=lambda sayi:sayi%2==1

print(tek_mi(22))
kuvvetini_al = lambda taban,kuvvet : taban ** kuvvet

print(kuvvetini_al(4,3))