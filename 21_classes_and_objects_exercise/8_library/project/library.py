class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def get_book(self, author, book_name, days_to_return, user):
        if user not in self.user_records:
            return None
        if author not in self.books_available:
            return None

        available_book = next((book for book in self.books_available.get(author,[]) if book == book_name), None)

        if available_book:
            self.books_available[author].remove(available_book)
            user.books.append(book_name)

            if user.username in self.rented_books:
                self.rented_books[user.username][book_name] = days_to_return
            else:
                self.rented_books[user.username] = {book_name:days_to_return}
            return f'{book_name} successfully rented for the next {days_to_return} days!'

        for books in self.rented_books.values():
            for rented_book, days_left in books.items():
                if rented_book == book_name:
                    return f'The book "{rented_book}" is already rented and will be available in {days_left} days!'
        else:
            return None

