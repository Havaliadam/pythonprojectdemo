def clear_numbers(metin:str):
    liste=[]
    for c in metin:
        try:
            int(c)
        except:
            liste.append(c)

    return  "".join(liste)

print(clear_numbers("kflkfla53j5l3 lk35jjk3 2j5 22 mrr"))