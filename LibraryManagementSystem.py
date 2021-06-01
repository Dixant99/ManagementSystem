"""It continuously needs to run the program to remember the data.
You can perform a various tasks of library  management from this program  """


class Library:
    def __init__(self, library_name, *list_of_books):
        self.list_of_books = list(list_of_books)
        self.library_name = library_name
        self.lenders_dict = {}

    def display_books(self):
        """This is to display all the books in the library"""
        print("the books present in the library: \n")
        for book in self.list_of_books:
            print(book)

    def lender_books(self):
        """This is to if some one lend the book"""

        def lender_can_issue_book():
            for key, value in self.lenders_dict.items():
                if value == lenders_name:
                    return False
            return True

        lenders_name = input("Enter your name : ").lower()
        if lender_can_issue_book():
            book_to_issue = input("Enter the  name of book : ").lower()
            if book_to_issue in self.list_of_books:
                self.lenders_dict[book_to_issue] = lenders_name
                self.list_of_books.remove(book_to_issue)
                print("Book Updated Successful")
            else:
                print("There is no such book available ")
        else:
            print("No that book is available to issue for you. You already have one.")

    def add_book(self):
        """This is to donate the books in the library"""
        book = input("Enter the book : ").lower()
        self.list_of_books.append(book)
        print("Book added to library Successfully")

    def return_book(self):
        """This is to give back the issued book"""
        book = input("Enter the name of the book you want to return \n").lower()
        if book in self.lenders_dict:
            self.list_of_books.append(book)
            self.lenders_dict.pop(book)
            print("book returned Successfully")
        else:
            print("The book is not issued from here")

    def who_have_book(self):
        a = input("Enter the book name whose lender name you want : ")
        name = self.lenders_dict[a]
        print(f"{name} is having {a}")


dlib = Library("Name of library", 'roses are blue', 'changes', 'artist', 'how to be a engineer')
print("Welcome to ", dlib.library_name)


print("Enter 'display'-to see the books in the library \n"
      "'lent'- to issue the book from the library \n"
      "'donate'- to donate the book to the library \n"
      "'return'- to return the issued book to the library \n"
      "'who'- to know who lend required book"
      "'exit'- to exit the library")
while True:
    choice = input("Enter what you want to do in library \n").lower()
    if choice == "display":
        dlib.display_books()
    elif choice == "lent":
        dlib.lender_books()
    elif choice == "donate":
        dlib.add_book()
    elif choice == "return":
        dlib.return_book()
    elif choice == "who":
        dlib.who_have_book()
    elif choice == "exit":
        break
    else:
        print("Invalid command")
print("Library is closed")
