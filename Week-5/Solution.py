import pprint

class Book():

    def __repr__(self):
        return (f"{self.Title} - By Author: {self.Author}")

    def __init__(self, title, author, pageCount = 0, isbn = 000000):
        
        self.Title = title
        self.Author = author
        self.Isbn = isbn
        self.PageCount = pageCount



def main():
    myBook = Book(title="Dune", author="Frank Herbert", pageCount = 444)
    anotherBook = Book(title="Guardians", author="Dan Abnett")
    
    print(myBook)


if __name__ == "__main__":
    main()

    myList = list("a", "b")
    myList.append("c")
    myList.reverse()
