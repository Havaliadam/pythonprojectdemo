import  sqlite3

class University:
    def __init__(self,name,country):
        self.name=name
        self.country=country
        self.status=True
        self.connectDatabase()



    def run(self):
        self.menu()


        choice=self.choice()
        if choice==1:
           self.addStundent()
        if choice==2:
            self.deleteStundent()
        if choice==3:
            self.updateStundent()
        if choice==4:
            while True:
                try:
                   orderby=int(input("1)All\n2)Faculty\3)Department\n4)Type\5Status\n\nSelect:"))
                   if orderby<1 or orderby>5:

                       continue

                   break

                except ValueError:
                                 print("Must be integer!")

            self.showallStundents(orderby)
        if choice==5:
            pass


    def menu(self):
        print("******{} Administariton System******".format(self.name))
        print("\n1)Add Stundent\n2)Delete Stundent\n3)Update Stundent\n4)Show All Stundents\5)Exit\n")

    def choice(self):
       while True:
         try:
          process=int(input("Select:"))
          if process<1 or process>5:
              print("Operation number must be between 1-5 please select correct number!")
              continue
          break
         except ValueError:
          print("Operation is must be integer .Please write correct type.")
       return process
    def addStundent(self):
        print("***Stundent Information***")
        name=input("Stundent's Name:").lower().capitalize()
        surname=input("Surname ' s Name").lower().capitalize()
        faculty=input("Faculty 's Name").lower().capitalize()
        department=input("Department 's Name").lower().capitalize()
        stid=input("Stundent's ID")

        while True:
            try:
                typ=int(input("Stundent's Education Type:"))
                if typ<1 or typ>2:
                    print("Stundent's education Type must be 1 or 2.\n")
                    continue
                break
            except ValueError:
             print("Type must be integer(1 or 2)\n")
        status="Active"
        self.cursor.execute("INSERT INTO stundent VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(name,surname,faculty,department,stid,typ,status))
        self.connect.commit()

        print("The stundent name {} {} succesful ".format(name,surname))

    def deleteStundent(self):
        self.cursor.execute("SELECT*FROM stundent")

        allstundents=self.cursor.fetchall()

        convertallStr=lambda  x:[str(y) for y in x]
        for i,j in enumerate(allstundents,1):
            print("{}){}".format(i," ".join(convertallStr(j))))

            while True:
                try:
                    select=int(input("Select the stundent to be deleted:"))
                    break
                except ValueError:
                    print("Please write  correct type(int)")

            self.cursor.execute("DELETE FROM stundent Where rowid={}".format(select))

            self.connect.commit()


            print("\nThe stundent succesfully deleted ")

    def updateStundent(self):
        self.cursor.execute ( "SELECT*FROM stundent" )
        allstundents = self.cursor.fetchall ()
        convertallStr = lambda x: [str (y) for y in x]
        for i , j in enumerate (allstundents,1 ):
            print ("{}){}".format ( i ," ".join (convertallStr(j))))
            while True:
                try:
                    select=int(input("\nSelect the stundent to be update:" ) )
                    break
                except ValueError:
                    print ( "Please write  correct type(int)" )
                while True:
                    try:
                        updateSelect=int(input("1)Name\n2)Surname\n3)Faculty\n4)Department\n5)Stundent ID\n6)Education Type\n7)Status"))
                        if updateSelect<1 or updateSelect>7:
                            continue
                        break
                    except ValueError:
                        print("It must be int!")
            operations=["name","surname","faculty","department","stid","typ","status"]

            if updateSelect==6:
                while True:
                     try:
                         newValue=int(input("enter the new value"))
                         if newValue not in(1,2):
                            continue
                         break
                     except ValueError:
                        print("Please, it must be integer!\n")
                self.cursor.execute("UPDATE stundent SET typ={} WHERE rowid={}".format(newValue,select))
            else:
                newValue=input( "enter the new value" )
                self.cursor.execute("UPDATE stundent SET {}='{}' WHERE rowid={}".format(operations[updateSelect-1],newValue,select))



            self.connect.commit()
            print("Update succesffull!")




    def showallStundents(self,by):
        if by==1:
            self.cursor.execute ( "SELECT*FROM stundent" )
            allstundents = self.cursor.fetchall ()
            convertallStr = lambda x: [str ( y ) for y in x]
            for i , j in enumerate ( allstundents ,
                                 1 ):
                print ( "{}){}".format ( i ,
                                     " ".join ( convertallStr ( j ) ) ) )

        if by==2:
              self.cursor.execute("Select faculty FROM stundent")



              facukties=list(enumerate(list(set(self.cursor.fetchall())),1))

              for i,j in facukties:
                  print("{]){}".format(i,j[0]))
              while True:
                  try:
                     select=int(input("\nSelect:"))
                     break
                  except ValueError:
                      print("Must be integer!")


              self.cursor.execute("SELECT*FROM stundent WHERE faculty='{}'".format(facukties[select-1][1][0]))

              allstundents = self.cursor.fetchall ()
              convertallStr = lambda x: [str ( y ) for y in x]
              for i , j in enumerate ( allstundents ,1 ):

                  print ( "{}){}".format ( i ," ".join ( convertallStr ( j ) ) ) )
        if by==3:
            self.cursor.execute ( "Select department FROM stundent" )

            department= list ( enumerate ( list ( set ( self.cursor.fetchall () ) ) ,
                                           1 ) )

            for i , j in department:
                print ( "{]){}".format ( i ,
                                         j[0] ) )
            while True:
                try:
                    select = int ( input ( "\nSelect:" ) )
                    break
                except ValueError:
                    print ( "Must be integer!" )

            self.cursor.execute ( "SELECT*FROM stundent WHERE department='{}'".format (department[select - 1][1][0] ) )

            allstundents = self.cursor.fetchall ()
            convertallStr = lambda x: [str ( y ) for y in x]
            for i , j in enumerate ( allstundents ,
                                     1 ):
                print ( "{}){}".format ( i ,
                                         " ".join ( convertallStr ( j ) ) ) )
        if by==4:
            self.cursor.execute ( "Select typ FROM stundent" )

            type = list ( enumerate ( list ( set ( self.cursor.fetchall () ) ) ,
                                           1 ) )

            for i , j in type:
                print ( "{]){}".format ( i ,
                                         j[0] ) )
            while True:
                try:
                    select = int ( input ( "\nSelect:" ) )
                    break
                except ValueError:
                    print ( "Must be integer!" )

            self.cursor.execute ( "SELECT*FROM stundent WHERE type={}".format ( type[select - 1][1][0] ) )

            allstundents = self.cursor.fetchall ()
            convertallStr = lambda x: [str ( y ) for y in x]
            for i , j in enumerate ( allstundents ,
                                     1 ):
                print ( "{}){}".format ( i ," ".join ( convertallStr ( j ) ) ) )
        if by==5:
            self.cursor.execute ( "Select status FROM stundent" )

            status = list ( enumerate ( list ( set ( self.cursor.fetchall () ) ) ,
                                      1 ) )

            for i , j in status:
                print ( "{]){}".format ( i ,
                                         j[0] ) )
            while True:
                try:
                    select = int ( input ( "\nSelect:" ) )
                    break
                except ValueError:
                    print ( "Must be integer!" )

            self.cursor.execute ( "SELECT*FROM stundent WHERE status={}".format (status[select - 1][1][0] ) )

            allstundents = self.cursor.fetchall ()
            convertallStr = lambda x: [str ( y ) for y in x]
            for i , j in enumerate ( allstundents ,
                                     1 ):
                print ( "{}){}".format ( i ,
                                         " ".join ( convertallStr ( j ) ) ) )





    def systemexit(self):
        self.status=False

    def connectDatabase(self):
        self.connect=sqlite3.connect("odtu.db")
        self.cursor=self.connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS stundent(name TEXT,surname TEXT,faculty TEXT,department TEXT,stid TEXT,typ INT,status TEXT)")
        self.connect.commit()

ODTU=University("Orda Dogu Teknik Universitesi","Turkiye")
while ODTU.status:
    ODTU.run()