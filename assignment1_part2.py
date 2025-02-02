class Book:
    def __init__(self, author, title):
        self.author = author
        self.title = title
    
    def display(self):
        book_details = "Title:" + " " + self.title + " | " + "Author: " + self.author
        print(book_details)
        pass


if __name__ == "__main__":
    book1 = Book("J K Rowling", "Harry Potter and the Goblet of Fire")
    book2 = Book("Walter Scott", "Ivanhoe A Romance")
    book3 = Book("Thorpe", "Beat the Dealer")
    
    book1.display()
    book2.display()
    book3.display()
        
    print("This is a assignment 1 part 2")
