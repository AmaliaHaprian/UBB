import tkinter as tk
from datetime import datetime, date, timedelta
from random import randint
from tkinter import Toplevel, Label, Entry, Button, messagebox, Image



# Import your components from the existing project
from src.domain.book import Book
from src.domain.client import Client
from src.domain.rental import Rental
from src.repository.book_repository.book_memo_repo import BookMemoRepo, DuplicateIDError, BookIDNotFoundError, \
    EmptyInputError
from src.repository.client_repository.client_memo_repo import ClientMemoRepo, DuplicateClientIDError, \
    ClientIDNotFoundError
from src.repository.rental_repository.rental_memo_repo import RentalMemoRepo
from src.services.book_service import BookService
from src.services.client_service import ClientService
from src.services.rental_service import RentalService
from PIL import ImageTk, Image

class LibraryManagerApp:
    def __init__(self, book_service:BookService, client_service:ClientService, rental_service:RentalService):

        self.book_service = book_service
        self.client_service = client_service
        self.rental_service = rental_service

    def create_main_ui(self):

        root = tk.Tk()
        root.geometry("600x600")
        root.title("Library Manager")

        background_image= tk.PhotoImage(file='bg_tkinter.png')
        background_label=Label(root, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(root, text="Welcome to Library Manager", font="Arial, 16", padx=10, pady=10)
        label.grid(row=0, column=1, columnspan=4)

        label2 = tk.Label(root, text="Choose an option", font="Arial, 12", padx=5, pady=5)
        label2.grid(row=1, column=1, columnspan=4)


        manage_button = tk.Button(root, text="Manage books/clients",bd=3, font="Arial, 9",command=lambda: self.click_manage(root), padx=8, pady=8)
        manage_button.grid(row=2, column=1)

        rent_return_button = tk.Button(root, text="Rent/return a book",bd=3,font="Arial, 9", command=lambda:self.click_rent_return(root),padx=8, pady=8)
        rent_return_button.grid(row=2, column=2)

        search_button = tk.Button(root, text="Search books/clients",bd=3,font="Arial, 9", command=lambda:self.click_search(root),padx=8, pady=8)
        search_button.grid(row=2, column=3)

        root.mainloop()

    def custom_messagebox(self, title, message):
        custom_box = Toplevel()
        custom_box.title(title)
        custom_box.geometry("200x100")

        label = Label(custom_box, text=message, fg="red")
        label.grid(row=0, column=0)

        close_button = Button(custom_box, text="Close", command=custom_box.destroy)
        close_button.grid(row=1, column=0)

    # --- Manage Books/Clients ---
    def click_manage(self, root):
        button_add = tk.Button(root, text="Add book", command=lambda:self.create_add_window(root))
        button_add.grid(row=3, column=1)

        button_remove = tk.Button(root, text="Remove book", command=lambda:self.create_remove_window(root))
        button_remove.grid(row=4, column=1)

        button_update = tk.Button(root, text="Update book", command=lambda:self.create_update_window(root))
        button_update.grid(row=5, column=1)

        button_list = tk.Button(root, text="List books", command=lambda:self.list_books(root))
        button_list.grid(row=6, column=1)

        button_add_client = tk.Button(root, text="Add client", command=lambda: self.create_add_window_client(root))
        button_add_client.grid(row=7, column=1)

        button_remove_client = tk.Button(root, text="Remove client", command=lambda: self.create_remove_window_client(root))
        button_remove_client.grid(row=8, column=1)

        button_update_client = tk.Button(root, text="Update client", command=lambda: self.create_update_window_client(root))
        button_update_client.grid(row=9, column=1)

        button_list_clients = tk.Button(root, text="List clients", command=lambda: self.list_clients(root))
        button_list_clients.grid(row=10, column=1)

    # --- Add Book ---
    def create_add_window(self,root):
        add_window = Toplevel(root)
        add_window.geometry("300x300")
        add_window.title("Add Book")

        id_label = Label(add_window, text="Enter book id", bg="pink", bd=2)
        id_label.grid(row=0, column=0)
        id_entry = Entry(add_window)
        id_entry.grid(row=0, column=1)

        title_label = Label(add_window, text="Enter book title", bd=2)
        title_label.grid(row=1, column=0)
        title_entry = Entry(add_window)
        title_entry.grid(row=1, column=1)

        author_label = Label(add_window, text="Enter book author", bg="pink", bd=2)
        author_label.grid(row=2, column=0)
        author_entry = Entry(add_window)
        author_entry.grid(row=2, column=1)

        add_button = Button(add_window, text="Add Book", command=lambda: self.add_book(id_entry.get(), title_entry.get(), author_entry.get()),padx=5, pady=5)
        add_button.grid(row=3, column=0, columnspan=2)

        #close_button = Button(add_window, text="Close", command=add_window.destroy)
        #close_button.grid(row=4, column=0)

    def add_book(self, book_id, book_title, book_author):
        book = Book(book_id, book_title, book_author)
        try:

            self.book_service.add_book(book)
            self.custom_messagebox("Success", "Book added successfully!")
        except DuplicateIDError as e:
            self.custom_messagebox("Error", e)
        except EmptyInputError as e:
            self.custom_messagebox("Error", e)


    # ---Remove Book ---
    def create_remove_window(self, root):
        remove_window = Toplevel(root)
        remove_window.geometry("300x300")
        id_label = Label(remove_window, text="Enter book id", bg="pink", bd=2)
        id_label.grid(row=0, column=0)
        id_entry = Entry(remove_window)
        id_entry.grid(row=0, column=1)
        remove_button = Button(remove_window, text="remove book", command=lambda: self.remove_book(id_entry.get()))
        remove_button.grid(row=1, column=0, columnspan=2)

        #close_button = Button(remove_window, text="Close", command=remove_window.destroy)
        #close_button.grid(row=4, column=0)

    def remove_book(self, book_id):
        try:
            self.book_service.remove_book(book_id)
            self.custom_messagebox(
                "Succes",
                "Book removed succesfully")
        except BookIDNotFoundError as e:
            self.custom_messagebox("Error", e)

    # ---Update Book ---
    def create_update_window(self,root):
        update_window = Toplevel(root)
        update_window.geometry("300x300")
        id_label = Label(update_window, text="Enter book id", bg="pink", bd=2)
        id_label.grid(row=0, column=0)
        id_entry = Entry(update_window)
        id_entry.grid(row=0, column=1)
        title_label = Label(update_window, text="Enter new book title", bd=2)
        title_label.grid(row=1, column=0)
        title_entry = Entry(update_window)
        title_entry.grid(row=1, column=1)
        author_label = Label(update_window, text="Enter book author", bg="pink", bd=2)
        author_label.grid(row=2, column=0)
        author_entry = Entry(update_window)
        author_entry.grid(row=2, column=1)

        update_button = Button(update_window, text="update book",
                            command=lambda: self.update_book(id_entry.get(), title_entry.get(), author_entry.get()))
        update_button.grid(row=3, column=0, columnspan=2)

        #close_button = Button(update_window, text="Close", command=update_window.destroy)
        #close_button.grid(row=4, column=0)

    def update_book(self, book_id, book_title, book_author):
        try:
            self.book_service.update_book(book_id, book_title, book_author)
            self.custom_messagebox(
                "Succes",
                "Book updated succesfully")
        except BookIDNotFoundError as e:
            self.custom_messagebox("Error", e)

    # --- Rent/Return a Book ---

    def click_rent_return(self,root):
        rent_button = tk.Button(root, text="Rent book", command=lambda:self.create_rent_window(root))
        rent_button.grid(row=3, column=2)

        return_button = tk.Button(root, text="Return book", command=lambda:self.create_return_window(root))
        return_button.grid(row=4, column=2)

    def create_rent_window(self,root):
        rent_window = Toplevel(root)
        rent_window.geometry("300x300")
        title_label = Label(rent_window, text="Enter book title", bg="pink", bd=2)
        title_label.grid(row=0, column=0)
        title_entry = Entry(rent_window)
        title_entry.grid(row=0, column=1)
        client_label = Label(rent_window, text="Enter client id", bd=2)
        client_label.grid(row=1, column=0)
        client_entry = Entry(rent_window)
        client_entry.grid(row=1, column=1)

        rent_button = Button(rent_window, text="Rent book", padx=3, pady=3,
                             command=lambda: self.rent_book(title_entry.get(), client_entry.get()))
        rent_button.grid(row=2, column=0, columnspan=2)

    def rent_book(self,book_title, client_id):
        book_id = self.book_service.get_book_id(book_title)
        rental_id = self.rental_service.rental_by_book_id(book_id)
        if rental_id != -1 and self.rental_service.get_rentals(rental_id).returned_date == "-":
            self.custom_messagebox(
                "Error",
                "Book is already rented")
        else:
            rental_id = self.rental_service.last_rental() + 1
            rented_date = datetime.today()
            returned_date = "-"
            self.rental_service.add_rental(Rental(rental_id, book_id, client_id, rented_date, returned_date))
            self.custom_messagebox(
                "Succes",
                "Book rented succesfully")

    def create_return_window(self,root):
        return_window = Toplevel(root)
        return_window.geometry("300x300")
        title_label = Label(return_window, text="Enter book you rented", bg="pink", bd=2)
        title_label.grid(row=0, column=0)
        title_entry = Entry(return_window)
        title_entry.grid(row=0, column=1)

        rent_button = Button(return_window, text="Return book", padx=3, pady=3,
                             command=lambda: self.return_book(title_entry.get()))
        rent_button.grid(row=2, column=0, columnspan=2)

    def return_book(self,book_title):
        book_id = self.book_service.get_book_id(book_title)
        rental_id = self.rental_service.book_rented(book_id)
        returned_date = datetime.today()

        self.rental_service.update_rental(rental_id, returned_date)
        self.custom_messagebox(
            "Succes",
            "Book returned succesfully")

    # ---List books ---
    def list_books(self,root):
        list_window = Toplevel(root)
        list_window.geometry("300x300")
        books = self.book_service.get_books()
        i = 6
        for book in books:
            label = Label(list_window, text=book)
            label.grid(row=i, column=0)
            i = i + 1
        #close_button = Button(list_window, text="Close", command=list_window.destroy)
        #close_button.grid(row=1, column=0)

    # --- Add client ---
    def create_add_window_client(self,root):
        add_window = Toplevel(root)
        add_window.geometry("300x300")
        add_window.title("Add Client")

        id_label = Label(add_window, text="Enter client id", bg="pink", bd=2)
        id_label.grid(row=0, column=0)
        id_entry = Entry(add_window)
        id_entry.grid(row=0, column=1)

        name_label = Label(add_window, text="Enter client name")
        name_label.grid(row=1, column=0)
        name_entry = Entry(add_window)
        name_entry.grid(row=1, column=1)


        add_button = Button(
            add_window,
            text="Add client",
            command=lambda: self.add_client(id_entry.get(), name_entry.get()),
        )
        add_button.grid(row=2, column=0, columnspan=2)

        #close_button = Button(add_window, text="Close", command=add_window.destroy)
        #close_button.grid(row=3, column=0)

    def add_client(self, client_id, client_name):
        client=Client(client_id, client_name)
        try:
            self.client_service.add_client(client)
            self.custom_messagebox("Success", "Client added successfully!")
        except DuplicateClientIDError as e:
            self.custom_messagebox("Error", str(e))
        except EmptyInputError as e:
            self.custom_messagebox("Error", str(e))

    # ---Remove client ---
    def create_remove_window_client(self, root):
        remove_window = Toplevel(root)
        remove_window.geometry("300x300")
        id_label = Label(remove_window, text="Enter client id", bg="pink", bd=2,)
        id_label.grid(row=0, column=0)
        id_entry = Entry(remove_window)
        id_entry.grid(row=0, column=1)
        remove_button = Button(remove_window, text="Remove client", command=lambda: self.remove_client(id_entry.get()))
        remove_button.grid(row=1, column=0, columnspan=2)

        #close_button = Button(remove_window, text="Close", command=remove_window.destroy)
        #close_button.grid(row=4, column=0)

    def remove_client(self, client_id):
        try:
            self.client_service.remove_client(client_id)
            self.custom_messagebox(
                "Succes",
                "Client removed succesfully")
        except ClientIDNotFoundError as e:
            self.custom_messagebox("Error", e)

    # ---Update Book ---
    def create_update_window_client(self,root):
        update_window = Toplevel(root)
        update_window.geometry("300x300")
        id_label = Label(update_window, text="Enter client id", bg="pink", bd=2)
        id_label.grid(row=0, column=0)
        id_entry = Entry(update_window)
        id_entry.grid(row=0, column=1)
        name_label = Label(update_window, text="Enter new client name", bd=2)
        name_label.grid(row=1, column=0)
        name_entry = Entry(update_window)
        name_entry.grid(row=1, column=1)


        add_button = Button(update_window, text="Update client",
                            command=lambda: self.update_client(id_entry.get(), name_entry.get()))
        add_button.grid(row=3, column=0, columnspan=2)

        #close_button = Button(update_window, text="Close", command=update_window.destroy)
        #close_button.grid(row=4, column=0)

    def update_client(self, client_id, client_name):
        try:
            self.client_service.update_client(client_id, client_name)
            self.custom_messagebox(
                "Succes",
                "Client updated succesfully")
        except ClientIDNotFoundError as e:
            self.custom_messagebox("Error", e)

    # ---List clients ---
    def list_clients(self,root):
        list_window = Toplevel(root)
        list_window.geometry("300x300")
        clients = self.client_service.get_clients()
        i = 6
        for client in clients:
            label = Label(list_window, text=client)
            label.grid(row=i, column=0)
            i = i + 1

    # --- Search Books and Clients ---
    def click_search(self,root):
        search_window = Toplevel(root)
        search_window.geometry("300x300")
        label1 = Label(search_window, text="""
                    search book by <id> <x>
                    search book by <title> <x>
                    search book by <author> <x>
                    search client by <id> <x>
                    search client by <name> <x>
                                         """, bd=5, relief="flat")
        label1.grid(row=0, column=0)
        entry_label = Label(search_window, text="What do you want to search for?", bg="green")
        entry_label.grid(row=1, column=0)
        entry_entry = Entry(search_window)
        entry_entry.grid(row=2, column=0)

        search_button = Button(search_window, text="search", command=lambda: self.search(search_window, entry_entry.get()))
        search_button.grid(row=3, column=0, columnspan=2)

    def search(self, search_window, search_term):
        answer = search_term.lower()
        processed_answer = answer.split(" ")

        for i in range(len(processed_answer)):
            processed_answer[i] = processed_answer[i].strip()

        if processed_answer[1] == "book":
            if processed_answer[3] == "id":
                if len(processed_answer) == 5:
                    try:
                        processed_answer[4] = int(processed_answer[4])
                        book = self.book_service.search_id(int(processed_answer[4]))
                        label = Label(search_window, text=book)
                        label.grid(row=6, column=0)
                    except ValueError:
                        self.custom_messagebox("Error", "Book id should be an integer")
                # else:
                #   print("Invalid command. Parameters don't match")

            elif processed_answer[3] == "title":
                try:
                    processed_answer[4] = processed_answer[4].lower()
                    filtered = self.book_service.search_title(processed_answer[4])
                    i = 6
                    for elem in filtered:
                        label = Label(search_window, text=elem)
                        label.grid(row=i, column=0)
                        i = i + 1

                except EmptyInputError as e:
                    self.custom_messagebox("Error", e)

            elif processed_answer[3] == "author":
                try:
                    filtered = self.book_service.search_author(processed_answer[4])
                    i = 6
                    for elem in filtered:
                        label = Label(search_window, text=elem)
                        label.grid(row=i, column=0)
                        i = i + 1
                except EmptyInputError as e:
                    self.custom_messagebox("Error", e)


        elif processed_answer[1] == "client":
            if processed_answer[3] == "id":
                if len(processed_answer) == 5:
                    try:
                        processed_answer[4] = int(processed_answer[4])
                        client = self.client_service.search_id(int(processed_answer[4]))
                        label = Label(search_window, text=client)
                        label.grid(row=6, column=0)
                    except ValueError:
                        self.custom_messagebox("Error", "Client id should be an integer")
                # else:
                #   print("Invalid command. Parameters don't match")
            elif processed_answer[3] == "name":
                try:

                    filtered = self.client_service.search_name(processed_answer[4])
                    i = 6
                    for elem in filtered:
                        label = Label(search_window, text=elem)
                        label.grid(row=i, column=0)
                        i = i + 1
                except EmptyInputError as e:
                    self.custom_messagebox("Error", e)

        #close_button = Button(search_window, text="Close", command=search_window.destroy)
        #close_button.grid(row=15, column=0)
