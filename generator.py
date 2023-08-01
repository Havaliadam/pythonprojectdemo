def sayiArttir():
    a=1
    yield a

    a+=1
    yield a
    a+=1
    yield a
for i in sayiArttir():
        print(i)