class Book:
    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return list(set(contract.author for contract in self.contracts()))


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class")
        contract = Contract(self, book, date, royalties)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author

    @property
    def book(self):
        return self._book

    @property
    def date(self):
        return self._date

    @property
    def royalties(self):
        return self._royalties

    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of the Author class")
        self._author = author

    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise Exception("book must be an instance of the Book class")
        self._book = book

    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        self._date = date

    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, (int, float)):
            raise Exception("royalties must be a number")
        self._royalties = royalties

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]


# Example usage:
# author1 = Author("John Smith")
# book1 = Book("My Great Book")
# contract1 = author1.sign_contract(book1, "2024-05-31", 15)
# print(book1.contracts())  # Should return a list of contracts for the book
# print(book1.authors())  # Should return a list of authors of the book
# print(author1.contracts())  # Should return a list of contracts for the author
# print(author1.books())  # Should return a list of books by the author
# print(author1.total_royalties())  # Should return the total royalties for the author
# print(Contract.contracts_by_date("2024-05-31"))  # Should return all contracts on the specified date
