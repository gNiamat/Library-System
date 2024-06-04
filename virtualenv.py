class Library:
    def __init__(self,books):
        self.books=books
    def displayAvailableBooks(self):
        print("Books Available in library are: ")    
        for  books in self.books:
            print(" *"+books)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"$$you have been issued the book {bookName}.PLZ kepp it safely and return it within 30 days.$$")        
            self.books.remove(bookName)
            with open("borrowList.txt","a") as f:
                        f.write(regNum+" ")
        else:
            print("$$Sorry, currently book is not available.You can check after somedays.$$")    
    def returnBook(self,bookName):
        print(f"$$Thanks for returning this book!.Hope you enjoyed it.$$")
        self.books.append(bookName)
class Student: 
    def requestBook(self):    
        self.book=input("inter the name of book you want to borrow: ")
        return self.book
    def returnBook(self):
        self.book=input("inter the name of book you want to return: ") 
        return self.book   
if __name__=="__main__":
    centerLibrary=Library(["Python","C Language","Java","Pandas","Flask","VirthulEnv"])
    studentArg=Student()
    while(True):
        welcomeMsg= '''======= WELCOME TO CENTER LIBRARY =======
        Please Inter Your Choice:
        1. Displaying list of books
        2. Borrowing Book
        3. Returning Book
        4. Exiting The Library
        '''
        print(welcomeMsg)
        Choice=int(input("->> "))
        if(Choice==1):
            centerLibrary.displayAvailableBooks()
        elif(Choice==2):
            regNum=input("Your regestration number: ")
            with open("borrowList.txt","r") as f:
                borrow=f.read()
                borrowlist=borrow.split(" ")
                if regNum in borrowlist:
                    print("$$You have already taken a book from library.plz return it first to take another book.$$")
                else:    
                    centerLibrary.borrowBook(studentArg.requestBook())
        elif(Choice==3):
            regNum=input("Your regestration number: ")
            with open("borrowList.txt","r") as f:
                data=f.read()
                if regNum in data:
                    newData=data.replace(regNum+" ","")
            with open("borrowList.txt","w") as f:
                f.write(newData)        
            centerLibrary.returnBook(studentArg.requestBook())
        elif(Choice==4):
            print("******Thank you for using Center Library******")            
            exit()
        else :
            print("You intered wrong choice")    
