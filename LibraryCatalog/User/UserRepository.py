from Utilities import XLUtils
from Environment.ENV import Env
from User.User import User
from User.UsersBook import UsersBook

class UserRepository:
    def __init__(self):
        self.usersDictionary = {}
        self.user = User()

    def getAllUsers(self):
        rowsCount = XLUtils.getRowCount(Env.dataPath, 'usersData')
        for r in range(2, rowsCount + 1):
             currentUser = User()
             currentUser.name = XLUtils.readData(Env.dataPath, "usersData", r, 1)
             book = UsersBook()
             book.ISBNnumber = XLUtils.readData(Env.dataPath, "usersData", r, 2)
             book.checkoutDate = XLUtils.readData(Env.dataPath, "usersData", r, 3)
             currentUser.userExistingBooks.append(book)
             if currentUser.name in self.usersDictionary.keys():
                 self.usersDictionary[currentUser.name].userExistingBooks.append(book)
             else:
                 self.usersDictionary[currentUser.name] = currentUser
