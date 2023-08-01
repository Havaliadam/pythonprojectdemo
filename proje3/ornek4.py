def pangram_checker(sentence):
    lsentence=sentence.lower()
    letters=['a','b','c','d','e','f','g','h','ı','i','j','k','l','m','n','o','ö','p','t','r','s','u','ü','y','z']
    for letter in lsentence:
        if letter in letters:
            try:
              letters.remove(letter)
            except:
                pass

    if len(letters)==0:
        return True
    else:
        return False

print(pangram_checker("hasta "))