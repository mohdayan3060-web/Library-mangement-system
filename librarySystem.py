class Library:
    def __init__(self,Name,Id_card_number, Enrollement_number):
        self.__name=Name
        self.__Id_card=Id_card_number
        self.__Enrollement=Enrollement_number
        pass


class display(Library):
        def show(self):
               print("wellcome to library")

               print("Choose your option")
               print("1. Student Login ")
               print("2. staff Login")
               print("3. Find Book")
               print("4. Rent the book")
               print("5. Fine ")
               print("6. Exit the program")
               choice=int(input("Enter your choice : "))
               if choice==1:
                   student_login()
               elif choice==2:
                   staff_login()
      
               elif choice == 3:
                   book_find()
      
               elif choice==4:
                   rentBook()
               elif choice ==5:
                   fine()
               elif choice==6:
                   exit()
               else:
                   print("please enter valid option")                           


class student_login(Library):
    def __init__(self,Name,Id_card_number, Enrollement_number):
        super().__init__(Name,Id_card_number, Enrollement_number)
        

        

class staff_login():
    pass

class book_find():
    pass

class rentBook():
    pass

class fine():
    pass

class exit():
    pass


obj=display("ayan",100867,2500101563)

obj.show()






