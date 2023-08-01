

def yazdir(func):
    def yildizla():
        print ( "*****************|**********" )
        func()
        return yildizla()

def yazdir1(yazi):
    print(yazi)

yildizliyazdir=yazdir(yazdir1)

yildizliyazdir()

yildizliyazdir()