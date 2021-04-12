from Book.Book import Book
from Utilities import XLUtils
from Environment.ENV import Env
from User.User import User
from User.UserRepository import UserRepository


class BookRepository:
    def __init__(self):
        self.booksDictionary = {}
        self.book = Book()

    def saveDataToFile(self):
        print("Hello")

    def getAllBooks(self):
        rowsCount = XLUtils.getRowCount(Env.dataPath, 'booksData')
        for r in range(2, rowsCount + 1):
            currentBook = Book()
            currentBook.ISBNnumber = XLUtils.readData(Env.dataPath, "booksData", r, 1)
            currentBook.title = XLUtils.readData(Env.dataPath, "booksData", r, 2)
            currentBook.pages = XLUtils.readData(Env.dataPath, "booksData", r, 3)
            currentBook.count = XLUtils.readData(Env.dataPath, "booksData", r, 4)
            currentBook.availableCount = XLUtils.readData(Env.dataPath, "booksData", r, 5)
            temp = str(XLUtils.readData(Env.dataPath, "booksData", r, 6))
            currentBook.subscribersNames = temp.split(sep=", ")
            temp = str(XLUtils.readData(Env.dataPath, "booksData", r, 7))
            currentBook.reservedFrom = temp.split(sep=", ")
            self.booksDictionary[str(currentBook.ISBNnumber)] = currentBook
