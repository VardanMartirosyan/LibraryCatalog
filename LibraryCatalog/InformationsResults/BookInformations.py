class BookInformations:
    def printAllBooks(self, booksList):
        for book in booksList.values():
            print("ISBN number is: [", book.ISBNnumber, "]")
            print("Title is: ", book.title)
            print("Pages is:", book.pages)
            print("Count is: ", book.count)
            print("Available Copies is: ", book.availableCount)
            if book.subscribersNames[0] != "None" or book.subscribersNames == None:
                print("Subscribers: ", book.subscribersNames)
            print("...\n")

    def printBookByISBNnumber(self, booksList, ISBNnumber):
        for book in booksList.values():
            if str(book.ISBNnumber) == str(ISBNnumber):
                print("ISBN number is: [", book.ISBNnumber, "]")
                print("Title is: ", book.title)
                print("Pages is:", book.pages)
                print("Count is: ", book.count)
                print("Available Copies is: ", book.availableCount)
                if book.subscribersNames[0] != "None" or book.subscribersNames == None:
                    print("Subscribers: ", book.subscribersNames)
                print("...\n")
