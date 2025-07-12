from datetime import datetime

from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.repository.book_repository.book_memo_repo import DuplicateIDError, BookIDNotFoundError, BookMemoRepo, \
    EmptyInputError, InputError
from src.repository.client_repository.client_memo_repo import DuplicateClientIDError, ClientIDNotFoundError
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService
from src.services.undo_service import UndoService
from src.validators.errors import StringError


class UI:
    def __init__(self, undo_service:UndoService, book_service: BookService, client_service: ClientService, rental_service: RentalService):
        self._book_service = book_service
        self._client_service = client_service
        self._rental_service = rental_service
        self._undo_service = undo_service

    def display(self, repo):
        for element in repo:
            print(element.__str__())

    def print_ui(self):

        # self._book_service.generate_books()
        # self._client_service.generate_clients()
        # self._rental_service.generate_rentals()

        while True:
            print("""
            1.Manage books/ clients
            2.Rent/ return book
            3.Search
            4.Create statistics
            5.Undo
            6.Redo
            """)
            option = input("Enter your choice: ")
            if option == "1":
                print("""
                1.Add book
                2.Remove book
                3.Update book
                4.List books
                5.Add client
                6.Remove client
                7.Update client
                8.List clients
                """)
                option = input("Enter your choice: ")

                if option == "1":
                    try:
                        book_id = int(input("Enter book id: "))
                        title = input("Enter book title: ")
                        author = input("Enter book author: ")
                        try:

                            self._book_service.add_book(Book(book_id, title, author))
                            print("Book successfully added")
                        except DuplicateIDError as e:
                            print(e)
                    except ValueError:
                        print("Book id should be an integer")
                    except EmptyInputError as e:
                        print(e)
                    except InputError as e:
                        print(e)
                    except StringError:
                        print("Book title or author not valid")

                elif option == "2":
                    try:
                        book_id = int(input("Enter book id you want to remove: "))
                        try:
                            self._book_service.remove_book(book_id)
                            print("Book successfully removed")
                        except BookIDNotFoundError as e:
                            print(e)
                    except ValueError:
                        print("Book id should be an integer")


                elif option == "3":
                    try:
                        book_id = int(input("Enter book id you want to update: "))
                        new_title = input("Enter new book title: ")
                        new_author = input("Enter new book author: ")
                        try:
                            self._book_service.update_book(book_id, new_title, new_author)
                            print("Book successfully updated")
                        except BookIDNotFoundError as e:
                            print(e)
                    except ValueError:
                        print("Book id should be an integer")
                    except EmptyInputError as e:
                        print(e)
                    except InputError as e:
                        print(e)


                elif option == "4":
                    self.display(self._book_service.get_books())


                elif option == "5":
                    try:
                        client_id = int(input("Enter client id: "))
                        client_name = input("Enter client name: ")
                        try:

                            self._client_service.add_client(Client(client_id, client_name))
                            print("Client successfully added")
                        except DuplicateClientIDError as e:
                            print(e)

                    except ValueError:
                        print("Client id should be an integer")
                    except EmptyInputError as e:
                        print(e)
                    except InputError as e:
                        print(e)
                    except StringError:
                        print("Client name not valid")

                elif option == "6":
                    client_id = int(input("Enter client id you want to remove: "))
                    try:
                        self._client_service.remove_client(client_id)
                        print("Client successfully removed")
                    except ClientIDNotFoundError as e:
                        print(e)

                elif option == "7":
                    try:
                        client_id = int(input("Enter client id you want to update: "))
                        new_client_name = input("Enter new client name: ")
                        try:
                            self._client_service.update_client(client_id, new_client_name)
                            print("Client successfully updated")
                        except ClientIDNotFoundError as e:
                            print(e)
                    except ValueError:
                        print("Client id should be an integer")
                    except EmptyInputError as e:
                        print(e)
                    except InputError as e:
                        print(e)


                elif option == "8":
                    self.display(self._client_service.get_clients())
                else:
                    print("Please choose a valid option")

            elif option == "2":

                print("""
                1.Rent book
                2.Return book
                """)
                #self.display(self._rental_service.rentals())
                option = input("Enter your choice: ")
                if option == "1":

                    book_title = input("Enter book title: ")
                    book_id = self._book_service.get_book_id(book_title)
                    rental_id= self._rental_service.rental_by_book_id(book_id)
                    if rental_id != -1 and self._rental_service.get_rentals(rental_id).returned_date=="-":
                        print("Book is already rented")
                    else:

                        rental_id = self._rental_service.last_rental() + 1
                        client_id = int(input("Enter client id: "))
                        rented_date = datetime.today()
                        returned_date = "-"
                        self._rental_service.add_rental(Rental(rental_id, book_id, client_id, rented_date, returned_date))
                        print("Book rented successfully")
                        # self.display(self._rental_service.rentals())

                elif option == "2":
                    book_title = input("Enter book title you rented: ")
                    book_id = self._book_service.get_book_id(book_title)
                    rental_id = self._rental_service.book_rented(book_id)
                    returned_date = datetime.today()

                    self._rental_service.update_rental(rental_id, returned_date)
                    print("Book returned successfully")
                    # self.display(self._rental_service.rentals())
                else:
                    print("Please choose a valid option")

            elif option == "3":
                print("""
                search book by <id> <x>
                search book by <title> <x>
                search book by <author> <x>
                search client by <id> <x>
                search client by <name> <x>
                """)

                option = input("Enter your command: ")
                answer = option.lower()
                processed_answer = answer.split(" ")
                for i in range(len(processed_answer)):
                    processed_answer[i] = processed_answer[i].strip()
                if len(processed_answer) < 5:
                    print("Command error! Please try again one of the commands.")
                else:
                    if processed_answer[1] == "book":
                        if processed_answer[3] == "id":
                            if len(processed_answer) == 5:
                                try:
                                    processed_answer[4] = int(processed_answer[4])
                                    print(self._book_service.search_id(int(processed_answer[4])))
                                except ValueError:
                                    print("Book id should be an integer")
                            else:
                                print("Invalid command. Parameters don't match")

                        elif processed_answer[3] == "title":
                            try:
                                processed_answer[4] = processed_answer[4].lower()
                                self.display(self._book_service.search_title(processed_answer[4]))
                            except EmptyInputError as e:
                                print(e)

                        elif processed_answer[3] == "author":
                            try:
                                self.display(self._book_service.search_author(processed_answer[4]))
                            except EmptyInputError as e:
                                print(e)


                    elif processed_answer[1] == "client":
                        if processed_answer[3] == "id":
                            if len(processed_answer) == 5:
                                try:
                                    processed_answer[4] = int(processed_answer[4])
                                    print(self._client_service.search_id(int(processed_answer[4])))
                                except ValueError:
                                    print("Client id should be an integer")
                            else:
                                print("Invalid command. Parameters don't match")
                        elif processed_answer[3] == "name":
                            try:

                                self.display(self._client_service.search_name(processed_answer[4]))
                            except EmptyInputError as e:
                                print(e)

            elif option == "4":
                print("""
                1. Most rented books
                2. Most active clients
                3. Most rented author
                """)
                option = input("Enter your choice: ")
                if option=="1":
                    list_of_books=self._rental_service.frequency_rentals()
                    for elem in list_of_books:
                        print(elem[0].title, elem[1])

                elif option=="2":
                    list_of_clients=self._rental_service.rental_days_clients()
                    for elem in list_of_clients:
                        print(elem[0].name.strip(), elem[1], "days")
                elif option=="3":
                    list_of_authors=self._rental_service.most_rented_author()
                    for elem in list_of_authors:
                        print(elem[0].strip(), elem[1], 'times')
            elif option=="5":
                try:
                    self._undo_service.undo()
                    print("Operation undone successfully!")
                except IndexError as ie:
                    print(ie)
            elif option=="6":
                try:
                    self._undo_service.redo()
                    print("Operation redone successfully!")
                except IndexError as ie:
                    print(ie)
            else:
                print("Please choose a valid option")