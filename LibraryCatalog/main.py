from Book.BookService import BookService
from User.UserService import UserService
from InformationsResults.BookInformations import BookInformations
from InformationsResults.UserInformations import UserInformations

if __name__ == '__main__':
   bookService  = BookService()
   userService = UserService()
   bookService.setUserService(userService)

   bookInformations = BookInformations()
   userInformations = UserInformations()

   bookInformations.printAllBooks(bookService.getBooksDictionory())
   userInformations.printAllUsers(userService.getUsersDictionary())
   bookService.userCheckoutBook("12340007", "Vardan", "2021-04-10")
   bookService.userCheckoutBook("12340008", "Vardan", "2021-04-10")
   bookService.subscribeBook("12340008", "Vardan")
   bookService.userReturnBook("12340008", "Gera")
   bookService.userReturnBook("12340005", "Ban")
   userInformations.printUserByName(userService.getUsersDictionary(), "Vardan")
   bookService.getSubscribersOfTheBook("12340007")
   bookService.getSubscribersOfTheBook("12340008")
   bookService.getUsersWhoCheckedOutBook("12340000")








