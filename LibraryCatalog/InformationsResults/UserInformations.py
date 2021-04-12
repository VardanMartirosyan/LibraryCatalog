class UserInformations:
    def printUserByName(self, usersList, userName):
        if userName in usersList.keys():
            user = usersList[userName]
            print("User name is: ", userName)
            for book in user.userExistingBooks:
                print("ISBNnumber is: ", book.ISBNnumber)
                print("Checkout checkoutDate is: ", book.checkoutDate)
            print("...\n")

    def printAllUsers(self, usersList):
        for user in usersList.values():
            print("User name is: ", user.name)
            for book in user.userExistingBooks:
                print("ISBNnumber is: ", book.ISBNnumber)
                print("Checkout checkoutDate is: ", book.checkoutDate)
            print("...\n")
