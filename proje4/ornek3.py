def first_repeat(metin:str):
    liste=[]

    for c in metin:
        if c not in liste:
            liste.append(c)
        else:
            return c

print(first_repeat("BTKIROLKJM"))