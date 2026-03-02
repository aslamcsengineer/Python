#The library Tracker basics

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.is_checked_out = False 
    def borrow_book(self):
        if(self.is_checked_out==True):
            print(f"Sorry book : {self.title} is not available")
        else:
            self.is_checked_out = True
            print("Book is Successfully Borrowed")
    def return_book(self):
        self.is_checked_out = False 
        print(f"{self.title} has been returned To Library")
    def __str__(self):
        status  = self.is_checked_out
        if(status == True):
            return f"{self.title} is Not Available"
        else:
            return f"{self.title} is Available"
            
book1 = Book("Secret of Success","Jai")
print(book1)
book1.boorow_book()
book1.boorow_book()
print(book1)
book1.return_book()
print(book1)
    
