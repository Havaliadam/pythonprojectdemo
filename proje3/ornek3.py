def move_to_zeros(liste):
    for i in liste:
     if i==0:
        liste.remove(i)
        liste.append(i)

     return liste
    
print(move_to_zeros([12,5,2,1,0,2,0,0,2,5,0,1,25]))
