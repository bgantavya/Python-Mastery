class library:
    def __init__(self):
        self.nobook = 0
        self.books = []

    def addbook(self,book):
        self.books.append(book)
        self.nobook = len(self.books)

    def show(self):
        print(self.nobook, self.books)

l1 = library()
l1.addbook("harrypotter1")
l1.show()
