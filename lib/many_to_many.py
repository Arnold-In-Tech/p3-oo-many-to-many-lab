
class Author:

    all = []

    def __init__(self, name):
        self.name = name
        Author.add_author_to_all(self)

    # ======================== 
    @classmethod
    def add_author_to_all(cls, author):
        cls.all.append(author)


    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    

    def books(self):
        # return a list of related books using the Contract class as an intermediary.
        return [contract.book for contract in self.contracts()]


    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date,royalties)


    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])



class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.add_book_to_all(self)

    # ======================== 
    @classmethod
    def add_book_to_all(cls, book):
        cls.all.append(book)


    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]


    def authors(self):
        return [contract.author for contract in self.contracts()]



class Contract:

    all = []

    def __init__(self, author, book, date, royalties):

        if isinstance(author, Author):
            self.author = author
        else:
            raise TypeError("author must be an instance of Author class")

        if isinstance(book, Book):
            self.book = book
        else:
            raise TypeError("book must be an instance of Book class")

        if type(date) == str:
            self.date = date
        else:
            raise TypeError("date must be of type string")

        if type(royalties) == int:
            self.royalties = royalties
        else:
            raise TypeError("royalties must be of type integer")

        Contract.add_contract_to_all(self)

        
    @classmethod
    def add_contract_to_all(cls, contract):
        cls.all.append(contract)


    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date ]


# =========================================================================

    # # ======================== 
    # @property
    # def author(self):
    #     return self._author
    
    # @author.setter
    # def author(self, value):
    #     if isinstance(value, Author):
    #         self._author = value
    #     else:
    #         raise TypeError("author must be an instance of Author class")


    # # ======================== 
    # @property
    # def book(self):
    #     return self._book
    
    # @book.setter
    # def book(self, value):
    #     if isinstance(value, Book):
    #         self._book = value
    #     else:
    #         raise TypeError("book must be an instance of Book class")


    # # ======================== 
    # @property
    # def date(self):
    #     return self._date

    # @date.setter
    # def date(self, value):
    #     if type(value) == str:
    #         self._date = value
    #     else:
    #         raise TypeError("date must be of type string")


    # # ======================== 
    # @property
    # def royalties(self):
    #     return self._royalties

    # @royalties.setter
    # def royalties(self, value):
    #     if type(value) == int:
    #         self._royalties = value
    #     else:
    #         raise TypeError("royalties must be of type integer")

    # ======================== 
    