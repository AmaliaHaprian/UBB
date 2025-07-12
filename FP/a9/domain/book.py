class Book(object):
    def __init__(self, book_id, title, author):
        self.__book_id = book_id
        self._title = title
        self._author = author

    @property
    def book_id(self):
        return self.__book_id
    @property
    def title(self):
        return self._title
    @property
    def author(self):
        return self._author

    @title.setter
    def title(self, title):
        self._title = title
    @author.setter
    def author(self, author):
        self._author = author

    def __str__(self):
        return f"Book id={self.book_id} is {self._title} by {self._author}"

    def __repr__(self):
        return str(self)