from User.UserRepository import UserRepository
from User.User import User
from User.UsersBook import UsersBook


class UserService:
    def __init__(self):
        self.userRepository = UserRepository()
        self.userRepository.getAllUsers()

    def setBookService(self, bookService):
        self.bookService = bookService

    def addUserInfo(self, name, ISBNnumber, checkoutDate):
        if name in self.userRepository.usersDictionary.keys():
            user = self.userRepository.usersDictionary[name]
            book = UsersBook()
            book.ISBNnumber = ISBNnumber
            book.checkoutDate = checkoutDate
            user.userExistingBooks.append(book)
            print("Successfully added User information for user", name, "inside existing user.")
            return
        currentUser = User()
        currentUser.name = name
        bookData = UsersBook()
        bookData.ISBNnumber = ISBNnumber
        bookData.checkoutDate = checkoutDate
        currentUser.userExistingBooks.append(bookData)
        self.userRepository.usersDictionary[name] = currentUser
        print("User", name, " Successfully added.")

    def removeBookFromUserCart(self, ISBNnumber, userName):
        if userName in self.userRepository.usersDictionary.keys():
            user = self.userRepository.usersDictionary[userName]
            for book in user.userExistingBooks:
                if str(book.ISBNnumber) == str(ISBNnumber):
                    user.userExistingBooks.remove(book)
                    return
        else:
            print("User", userName, "not found.")

    def getUsersDictionary(self):
        return self.userRepository.usersDictionary
