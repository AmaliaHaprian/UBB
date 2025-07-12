import pickle

from src.repository.rental_repository.rental_memo_repo import RentalMemoRepo


class RentalBinaryRepo(RentalMemoRepo):
    def __init__(self, file_name="rentals.pickle"):
        super().__init__()
        self._file_name = file_name
        self._load()
    def _load(self):
        try:
            fin=open(self._file_name, "rb")
            text=pickle.load(fin)
        except EOFError:
            return
        for rentals in text:
            if rentals not in text:
                super().add(rentals)

    def _save(self):
        with open(self._file_name, "wb") as fout:
            pickle.dump(self, fout)

    def add(self, rental):
        super().add(rental)
        self._save()
    def remove(self, rental):
        super().remove(rental)
        self._save()
    def update(self, rental_id, returned_date):
        super().update(rental_id, returned_date)
        self._save()
    def get_all(self):
        return super().get_all()
    def get_last_rental(self):
        return super().get_last_rental()
    def get_rental_by_book_id(self, search_book_id):
        return super().get_rental_by_book_id(search_book_id)