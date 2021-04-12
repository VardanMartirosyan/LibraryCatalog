from Book.BookRepository import BookRepository
from Book.Book import Book
from Utilities.DataCalculator import DataCalculator


class BookService:
    def __init__(self):
        self.bookRepository = BookRepository()
        self.dataCalc = DataCalculator()
        self.bookRepository.getAllBooks()

    def setUserService(self, userService):
        self.userService = userService

    def userCheckoutBook(self, ISBNnumber, userName, checkoutDate):
        book = self.bookRepository.booksDictionary[ISBNnumber]
        if self.isAvailableBook(ISBNnumber):
            book.availableCount -= 1
            print("Book", ISBNnumber, " successfully checkouted.")
            self.userService.addUserInfo(userName, ISBNnumber, checkoutDate)
            print("Successfully added information in User Cart.")
            return
        else:
            print("Dear", userName, "not Available Book", ISBNnumber,
                  "you can Subscribe and we will let you know when we have available books.")

    def userReturnBook(self, ISBNnumber, userName):
        book = self.bookRepository.booksDictionary[ISBNnumber]
        self.getOverdueBook(userName)
        book.availableCount += 1
        self.userService.removeBookFromUserCart(ISBNnumber, userName)
        self.bookRepository.booksDictionary[ISBNnumber].reservedFrom.remove(userName)
        print("Book #", ISBNnumber, "successfully returned in to Library from", userName)
        if book.subscribersNames[0] != 'None':
            self.getNotificationsForReservedBooks(ISBNnumber, book.subscribersNames)

    def subscribeBook(self, ISBNnumber, subscriberName):
        book = self.bookRepository.booksDictionary[ISBNnumber]
        if self.isAvailableBook(ISBNnumber):
            print("Dear", subscriberName, "book", ISBNnumber, "available you dont need to Subscribe.")
        else:
            book.subscribersNames.append(subscriberName)
            print("Dear", subscriberName, "You successfully subscribe in to book #", ISBNnumber)

    def getSubscribersOfTheBook(self, ISBNnumber):
        if self.isAvailableBook(ISBNnumber):
            book = self.bookRepository.booksDictionary[ISBNnumber]
            if len(book.subscribersNames) > 0 and book.subscribersNames[0] != "None":
                print("Book - ", ISBNnumber, "has ", len(book.subscribersNames), " subscribers:")
                for subscriber in book.subscribersNames:
                    print("\t", subscriber)
                return
            elif book.subscribersNames[0] == "None":
                print("Book #", ISBNnumber, "have no Subscribers")
                return

    def getNotificationsForReservedBooks(self, ISBNnumber, subscibersNames):
        for subscriber in subscibersNames:
            print("Dear ", subscriber, 'now book #', ISBNnumber, "already exist in library.")

    def getOverdueBook(self, userName):
        if userName in self.userService.userRepository.usersDictionary.keys():
            user = self.userService.userRepository.usersDictionary[userName]
            for book in user.userExistingBooks:
                data = self.dataCalc.calculateData(91)
                if str(data) > str(book.checkoutDate):
                    print("Book #", book.ISBNnumber, "is Overdue in to user", user.name)
                    f_data = str(data).split(sep="-")
                    s_data = book.checkoutDate.split(sep="-")
                    self.getFineForOverdue(f_data, s_data)

    def getFineForOverdue(self, fistData, secondData):
        delta = self.dataCalc.getSubOfTwoDates(fistData, secondData)
        fine = int(delta / 7) * 5
        print("Fine is:", fine, "$")

    def isAvailableBook(self, ISBNnumber) -> bool:
        if ISBNnumber in self.bookRepository.booksDictionary.keys():
            book = self.bookRepository.booksDictionary[ISBNnumber]
            if int(book.availableCount) > 0:
                return True
            else:
                return False
        else:
            print("Sorry Book Not found in Library")
            return False

    def getUsersWhoCheckedOutBook(self, ISBNnumber):
        if ISBNnumber in self.bookRepository.booksDictionary.keys():
            book = self.bookRepository.booksDictionary[ISBNnumber]
            for user in book.reservedFrom:
                print("Book #", ISBNnumber, "checked out by", user)

    def addBook(self, ISBNnumber, title, pages, count, availableCount):
        if ISBNnumber in self.bookRepository.booksDictionary.keys():
            print("Book from: ", ISBNnumber, " already exists.")
            return
        currentBook = Book()
        currentBook.ISBNnumber = ISBNnumber
        currentBook.title = title
        currentBook.pages = pages
        currentBook.count = count
        currentBook.availableCount = availableCount
        self.bookRepository.booksDictionary[ISBNnumber] = currentBook

    def getBooksDictionory(self):
        return self.bookRepository.booksDictionary
