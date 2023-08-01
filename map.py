#def kareal(x):
 #   return  x**2

#print(list(map(kareal,[1,2,3,4,5,6,7,8,9,10])))

users={
"mckarakule42":"4242bela4242",
"yarali34":"123456",
"hans landa":"klmn ?*xLKv/*",
"frank underwood":"Clarie"
}
def control(username,password):
    try:
        if users[username]==password:
            return True
    except KeyError:
        return False
results=list(map(control,["mckarakule42","frank underwood","sais","hans landa"],["4242bela4242","Clarie","fafafa","xxxcc"]))
print(results)
