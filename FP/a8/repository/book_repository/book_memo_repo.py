from src.domain.book import Book

class RepositoryError(Exception):
    pass
class DuplicateIDError(RepositoryError):
    pass
class BookIDNotFoundError(RepositoryError):
    pass
class InputError(Exception):
    pass
class EmptyInputError(InputError):
    pass
class BookMemoRepo():
    def __init__(self):
        self._data={}

    def add(self, book: Book):
        """
        The function add a new book to the repository. If there already is a book with such id, it raises an error
        :param book: the book entity
        :return: None
        """
        if int(book.book_id) in self._data:
            raise DuplicateIDError("Duplicate book id error")

        if len(book.title)==0 or len(book.author)==0:
            raise EmptyInputError('Fields cannot be empty')
        if len(book.title)<3:
            raise InputError('Field title should be at least 3 characters long')
        if len(book.author)<3:
            raise InputError('Field author should be at least 3 characters long')
        self._data[book.book_id] = book

    def remove(self, book_id):
        """
        The function removes a book from the repository. If there is no such book, it raises an error.
        :param book_id: the id of the book to remove
        :return: the modifies list of books
        """
        if book_id not in self._data:
            raise BookIDNotFoundError("Book id not found")
        return self._data.pop(book_id)

    def update(self, book_id: str, new_title, new_author):
        """
        The function updates a book in the repository. If there is no such book, it raises an error.
        :param book_id: the id of the book to update
        :param new_title: the new title of the book
        :param new_author: the new author of the book
        :return: None
        """
        if book_id not in self._data:
            raise BookIDNotFoundError("Book id not found")
        if len(new_title)==0 or len(new_author)==0:
            raise EmptyInputError('Fields cannot be empty')
        if len(new_title)<3 or len(new_author)<3:
            raise InputError('Field title and author should be at least 3 characters long')
        self._data[book_id].title = new_title
        self._data[book_id].author = new_author

    def get_all(self):
        return list(self._data.values())

    def search_by_id(self, search_book_id):
        for book_id in self._data:
            if search_book_id==book_id:
                return self._data[book_id]

    def search_by_title(self, search_book_title):
        if len(search_book_title)==0:
            raise EmptyInputError('Field cannot be empty')
        filtered=[]
        for book_id in self._data:
            if search_book_title.lower() in self._data[book_id].title.lower():
                filtered.append(self._data[book_id])
        return filtered

    def search_by_author(self, search_book_author):
        if len(search_book_author)==0:
            raise EmptyInputError('Field cannot be empty')
        filtered=[]
        for book_id in self._data:
            if search_book_author.lower() in self._data[book_id].author.lower():
                filtered.append(self._data[book_id])
        return filtered

    def get_id_from_title(self, search_book_title):
        for book_id in self._data:
            if search_book_title.lower() in self._data[book_id].title.lower():
                return book_id
        return 10000

    def __iter__(self):
        return BookRepositoryIterator(list(self._data.values()))

    #def __getitem__(self, key):
     #   if key not in self._data:
     #       return None
      #  return self._data[key]

class BookRepositoryIterator():
    def __init__(self, data):
        self.__data=data
        self.__pos=-1
    def __next__(self):
         self.__pos +=1
         if len(self.__data)==self.__pos:
             raise StopIteration()
         return self.__data[self.__pos]


