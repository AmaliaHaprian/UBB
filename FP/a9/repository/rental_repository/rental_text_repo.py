from datetime import datetime, date

from src.domain.rental import Rental
from src.repository.rental_repository.rental_memo_repo import RentalMemoRepo


class RentalTextRepo(RentalMemoRepo):
    def __init__(self, file_name='rentals.txt'):
        super().__init__()
        self.file_name=file_name
        self._load()

    def _load(self):
        fin=open(self.file_name,"rt")
        line = fin.readline()
        while len(line)>0:
            current_line=line.split(",")
            rental_id=current_line[0]
            book_id=current_line[1]
            client_id=current_line[2]

            rented_date=datetime.strptime(current_line[3],'%Y-%m-%d')
            returned_date=current_line[4].strip()
            if returned_date!="-":
                returned_date=datetime.strptime(returned_date,'%Y-%m-%d')
            if current_line[0]!="\n":
                new_rental=Rental(int(rental_id), int(book_id), int(client_id), rented_date, returned_date)
                super().add(new_rental)
            line=fin.readline()
        fin.close()

    def _save(self):
        #fout=open(self._file_name, "wt")
        #for student in self.get_all():
        #    fout.write(student.to_str() + "\n")

        fout=open(self.file_name,"wt")
        for rental in self.get_all():
            if rental.returned_date=="-":
                fout.write(str(rental.rental_id) + "," + str(rental.book_id) + "," + str(rental.client_id) + "," + rental.rented_date.strftime("%Y-%m-%d") + "," + rental.returned_date + "\n")
            else:
                fout.write(str(rental.rental_id)+ "," +str(rental.book_id) + "," + str(rental.client_id) + "," + rental.rented_date.strftime("%Y-%m-%d")+ "," + rental.returned_date.strftime("%Y-%m-%d")+"\n")
        fout.close()

        #TODO test rent book for text repository
    def add(self, rental):
        super().add(rental)
        self._save()
    def remove(self, rental):
        rental=super().remove(rental)
        self._save()
        return rental
    def update(self, rental_id, returned_date):
        rental=super().update(rental_id, returned_date)
        self._save()
        return rental
    def get_all(self):
        return super().get_all()
    def get_last_rental(self):
        return super().get_last_rental()
    def get_rental_by_book_id(self, search_book_id):
        return super().get_rental_by_book_id(search_book_id)
    #def __iter__(self):
      #  self._load()
      #  return super().__iter__()
   # def __getitem__(self, key):
      #  self._load()
      #  return super().__getitem__(key)