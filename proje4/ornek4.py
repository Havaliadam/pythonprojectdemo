def maxc(metin:str):
    edict=dict()
    for c in metin:
        if c not in edict:
            edict[c]=1

        else:
            edict[c]+=1


    kayit=0
    karakter=""
    for c,n in edict.items():
        if n>kayit:
            kayit=n
            karakter=c

    return "{}:{}".format(karakter,kayit)

print(maxc("mert mekatronik udemy dersleri"))