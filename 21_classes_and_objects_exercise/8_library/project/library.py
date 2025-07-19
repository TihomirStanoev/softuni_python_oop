from project.user import User

class Library:
    def __init__(self):
        self.user_records: list[User] = []
        self.books_available: dict[str:[str]] = {} # {'Authors':['Books']}
        self.rented_books: dict[str:dict[str:int]] = {} # {'usernames':{'book1': 5, 'book2':3 }}

    def _is_rented(self, book_name: str):
        for _, __ in self.rented_books.items():
            for rented_book, days in __.items():
                if book_name == rented_book:
                    return days
        return -1

    def _is_available(self, author, book_name):
        return  book_name in self.books_available.get(author, [])


    def get_book(self, author: str, book_name: str, days_to_return: int, user: User):
        if not self._is_available(author, book_name):
            rented_days = self._is_rented(book_name)
            if rented_days >= 0:
                return f'The book "{book_name}" is already rented and will be available in {rented_days} days!'
            return ''

        if user.username not in self.rented_books:
            self.rented_books[user.username] = {}
        self.rented_books[user.username][book_name] = days_to_return
        user.books.append(book_name)
        self.books_available[author].remove(book_name)

        return f'{book_name} successfully rented for the next {days_to_return} days!'


    def return_book(self, author:str, book_name:str, user:User):
        if book_name not in user.books:
            return f'{user.username} doesn\'t have this book in his/her records!'

        self.books_available[author].append(book_name)
        del self.rented_books[user.username][book_name]
        user.books.remove(book_name)