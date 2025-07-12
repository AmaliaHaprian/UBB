import pickle

from src.domain.book import Book
from src.repository.book_repository.book_memo_repo import BookMemoRepo


class BookBinaryRepo(BookMemoRepo):
    def __init__(self, file_path):
        super().__init__()
        self._file_path = file_path
        self._load()
    def _load(self):

        try:
            fin=open(self._file_path, "rb")
            text=pickle.load(fin)
            for book in text:
                if book not in text:
                    super().add(book)
        except EOFError:
            return
        except FileNotFoundError:
            print("file not found")
        except OSError as e:
            print(e)


    def _save(self):
        with open(self._file_path, "wb") as fout:
            pickle.dump(self._data, fout)

    def add(self, book: Book):
        super().add(book)
        self._save()

    def remove(self, book: Book):
        super().remove(book)
        self._save()
    def update(self, book_id, new_title, new_author):
        super().update(book_id, new_title, new_author)
        self._save()
    def get_all(self):
        return super().get_all()
    def search_by_id(self, book_id):
        return super().search_by_id(book_id)
    def search_by_title(self, book_title):
        return super().search_by_title(book_title)
    def search_by_author(self, book_author):
        return super().search_by_author(book_author)
    def get_id_from_title(self, book_title):
        return super().get_id_from_title(book_title)
    #def __iter__(self):
       # self._load()
       # return super().__iter__()
    #def __getitem__(self, key):
     #   self._load()
      #  return super().__getitem__(key)