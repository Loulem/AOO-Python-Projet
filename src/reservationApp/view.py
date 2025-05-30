
from tkinter import *
import re
from tkinter import ttk
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from reservationApp.controller.controller import Controller  # imported only for type checking

class View():
    def __init__(self,controller : "Controller"):    
        self.controller = controller
        self.root = Tk()
        self.root.title("MeetingPro")
        self.root.geometry("1080x720")
        self.root.minsize(480, 360)
        self.root.iconbitmap("src/MeetingPro.ico")
        # create a menu bar
        self.my_menu = Menu(self.root)
        self.root.config(menu=self.my_menu)
        self.file_menu = Menu(self.my_menu)
        self.my_menu.add_checkbutton(label="accueil", command=self.main_menu)
        self.my_menu.add_checkbutton(label="ajouter", command=self.add_menu)
        self.my_menu.add_checkbutton(label="réserver", command=self.reserve_menu)
        self.my_menu.add_checkbutton(label="afficher", command=self.show_menu)

        # create menu
        self.main_frame = Frame(self.root, bg="white")
        self.add_frame = Frame(self.root, bg="white")
        self.show_frame = Frame(self.root, bg="white")
        self.reserve_frame = Frame(self.root, bg="white")
        self.new_client_frame = Frame(self.root, bg="white")
        self.new_room_frame = Frame(self.root, bg="white")
        self.show_list_of_rooms_frame = Frame(self.root, bg="white")
        self.reservation_frame = Frame(self.root, bg="white")
        self.room_available_for_time_slot_frame = Frame(self.root, bg="white")
        self.choose_room_frame = Frame(self.root, bg="white")
        self.validation_of_reservation_frame = Frame(self.root, bg="white")
        self.main_menu()


    
    def main(self):
        """Main function to start the application."""
        self.root.mainloop()

# change menu
    def main_menu(self):
        self.hide_all()
        self.main_frame.pack(fill="both", expand=1)
        add_button = Button(self.main_frame, text="Ajouter", command=self.add_menu)
        show_button = Button(self.main_frame, text="Afficher", command=self.show_menu)
        book_button = Button(self.main_frame, text="Réserver", command=self.reserve_menu)
        add_button.pack()
        show_button.pack()
        book_button.pack()

    def add_menu(self):
        self.hide_all()
        self.add_frame.pack(fill="both", expand=1)
        add_new_client_button = Button(self.add_frame, text="Ajouter un client", command=self.new_client_menu)
        add_new_client_button.pack()
        add_new_room_button = Button(self.add_frame, text="Ajouter une salle", command=self.new_room_menu)
        add_new_room_button.pack()

    def new_client_menu(self):
        self.hide_all()
        self.new_client_frame.pack(fill="both", expand=1)
        new_client_label = Label(self.new_client_frame, text="Ajouter un client")
        new_client_label.pack()
        new_client_name_entry = Entry(self.new_client_frame)
        new_client_name_entry.insert(0, "Prénom")
        new_client_name_entry.pack()
        new_client_surname_entry = Entry(self.new_client_frame)
        new_client_surname_entry.insert(0, "Nom de famille")
        new_client_surname_entry.pack()
        new_client_email_entry = Entry(self.new_client_frame)
        new_client_email_entry.insert(0, "Email")
        new_client_email_entry.pack()
        validation_button = Button(self.new_client_frame, text="valider", command= lambda : self.controller.add_client(new_client_name_entry.get(),new_client_surname_entry.get(),new_client_email_entry.get()))
        validation_button.pack()
        cancel_button = Button(self.new_client_frame, text="Annuler", command=self.add_menu)
        cancel_button.pack()

    def show_error_message(self, message: str):
        """Display an error message in a popup window."""
        error_window = Toplevel(self.root)
        error_window.title("Erreur")
        error_label = Label(error_window, text=message, fg="red")
        error_label.pack(pady=20) 
        close_button = Button(error_window, text="Fermer", command=error_window.destroy)
        close_button.pack(pady=10)
        error_window.geometry("300x150")

    def show_success_message(self, message: str):
        """Display a success message in a popup window."""
        success_window = Toplevel(self.root)
        success_window.title("Succès")
        success_label = Label(success_window, text=message, fg="green")
        success_label.pack(pady=20)
        close_button = Button(success_window, text="Fermer", command=success_window.destroy)
        close_button.pack(pady=10)
        success_window.geometry("700x100")
        self.main_menu()  

    def new_room_menu(self):
        self.hide_all()
        self.new_room_frame.pack(fill="both", expand=1)
        new_room_label = Label(self.new_room_frame, text="Ajouter une nouvelle salle")
        new_room_label.pack()
        var = StringVar()
        new_room_name_entry = Entry(self.new_room_frame, text="Nom de la salle") # TODO remove use of text parameter
        new_room_name_entry.pack()

        capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        capacity_list = StringVar()
        capacity_list.set(str(capacity[0]))  # Set default value
        new_room_capacity = OptionMenu(self.new_room_frame, capacity_list,*capacity)
        new_room_capacity.pack()

        type_of_room = ["Salle de réunion", "Salle de conférence", "Bureau"]
        type_of_room_list = StringVar()
        type_of_room_list.set(type_of_room[0])  # Set default value
        new_room_type = OptionMenu(self.new_room_frame, type_of_room_list, *type_of_room)
        new_room_type.pack()

        validation_button = Button(self.new_room_frame, text="valider", command=lambda:self.controller.add_room(new_room_name_entry.get(), type_of_room_list.get(), capacity_list.get()))
        validation_button.pack()
        cancel_button = Button(self.new_room_frame, text="Annuler", command=self.add_menu)
        cancel_button.pack()


    def show_menu(self):
        self.hide_all()
        self.show_frame.pack(fill="both", expand=1)
        show_list_of_rooms_button = Button(self.show_frame, text="Afficher la liste des salles", command=self.show_list_of_rooms)
        show_list_of_rooms_button.pack()
        show_list_of_clients_button = Button(self.show_frame, text="Afficher la liste des clients")
        show_list_of_clients_button.pack()
        show_rooms_for_time_slot_button = Button(self.show_frame, text="Afficher les salles disponibles pour un créneau",command=self.room_available_for_time_slot_menu)
        show_rooms_for_time_slot_button.pack()
        show_book_of_clients_button = Button(self.show_frame, text="Afficher les reservation d'un clients", command=self.reservation_menu)
        show_book_of_clients_button.pack()

    def reservation_menu(self): # TODO change the name of this function to show_reservation_menu
        """Display the reservation menu where the user can choose a client to reserve a room."""
        self.hide_all()
        self.reservation_frame.pack(fill="both", expand=1)
        reservation_label = Label(self.reservation_frame, text="Réservation du client")
        reservation_label.pack()
        client_label = Label(self.reservation_frame, text="Client:")
        client_label.pack()
        client = self.controller.get_clients_list()  # TODO if the list is empty there is an error, add something to handle this case
        client_list = StringVar()
        client_list.set(client[0])  # Set default value
        client_option_menu = OptionMenu(self.reservation_frame, client_list, *client)
        client_option_menu.pack()
        validation_button = Button(self.reservation_frame, text="valider", command=self.main_menu)
        validation_button.pack()
        cancel_button = Button(self.reservation_frame, text="Annuler", command=self.show_menu)
        cancel_button.pack()

    def room_available_for_time_slot_menu(self):
        self.hide_all()
        self.room_available_for_time_slot_frame.pack(fill="both", expand=1)
        room_available_for_time_slot_label = Label(self.room_available_for_time_slot_frame, text="Salles disponibles pour le créneau")
        room_available_for_time_slot_label.pack()
        begin_label = Label(self.room_available_for_time_slot_frame, text="Début:")
        begin_label.pack()
        date_of_beginning_entry = Entry(self.room_available_for_time_slot_frame)
        date_of_beginning_entry.insert(0, "Date de début")
        date_of_beginning_entry.pack()
        end_label = Label(self.room_available_for_time_slot_frame, text="Fin:")
        end_label.pack()
        date_of_ending_entry = Entry(self.room_available_for_time_slot_frame)
        date_of_ending_entry.insert(0, "Date de fin")
        date_of_ending_entry.pack()
        validation_button = Button(self.room_available_for_time_slot_frame, text="valider", command=self.main_menu)
        validation_button.pack()
        cancel_button = Button(self.room_available_for_time_slot_frame, text="Annuler", command=self.show_menu)
        cancel_button.pack()
    
    def show_list_of_rooms(self):
        self.hide_all()
        self.show_frame.pack(fill="both", expand=1)
        
        """# Titre
        show_list_of_rooms_label = Label(self.show_frame, text="Liste des salles")
        show_list_of_rooms_label.pack()
        listbox = Listbox(self.show_frame)
        listbox.pack(fill="both", expand=1)
        # add a scrollbar
        scrollbar = Scrollbar(self.show_frame)
        scrollbar.pack(side="right", fill="y")
        listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)"""
        # Get the list of rooms and display them in the listboxcolumns = ("Nom", "Type", "Capacité")
        columns = ("Nom", "Type", "Capacité")
        tree = ttk.Treeview(self.show_frame, columns=columns, show="headings", height=10)

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")

        try:
            rooms = self.controller.get_rooms_list()
            if not rooms:
                tree.insert("", "end", values=("Aucune salle disponible", "", ""))
            else:
                for room in rooms:
                    tree.insert("", "end", values=(room.name, room.type, room.capacity))
        except Exception as e:
            self.show_error_message(f"Erreur lors de la récupération des salles : {e}")

        tree.pack(fill="both", expand=1, padx=20, pady=10)
        """
        try:
            rooms = self.controller.get_rooms_list()
            if not rooms:
                listbox.insert(END, "Aucune salle disponible.")
                return
            
            for room in rooms:
                room_info = f"{room.name} | Type: {room.type} | Capacité: {room.capacity}"
                listbox.insert(END, room_info)
        except Exception as e:
            self.show_error_message(f"Erreur lors de la récupération des salles : {e}")"""



    def reserve_menu(self):
        self.hide_all()
        self.reserve_frame.pack(fill="both", expand=1)
        reserve_label = Label(self.reserve_frame, text="Réserver une salle")
        reserve_label.pack()
        begin_label = Label(self.reserve_frame, text="Début:")
        begin_label.pack()
        date_of_beginning_entry = Entry(self.reserve_frame)
        date_of_beginning_entry.insert(0, "Date de début")
        date_of_beginning_entry.pack()
        end_label = Label(self.reserve_frame, text="Fin:")
        end_label.pack()
        date_of_ending_entry = Entry(self.reserve_frame)
        date_of_ending_entry.insert(0, "Date de fin")
        date_of_ending_entry.pack()
        client_label = Label(self.reserve_frame, text="Client:")
        client_label.pack()
        client = self.controller.get_clients_list() # a modifier pour recuperer la liste des clients
        # TODO if the list is empty there is an error, add something to handle this case
        client_list= StringVar()
        client_list.set(client[0])  # Set default value
        client_option_menu = OptionMenu(self.reserve_frame, client_list, *client)
        client_option_menu.pack()
        type_of_room_label = Label(self.reserve_frame, text="Type:")
        type_of_room_label.pack()
        validation_button = Button(self.reserve_frame, text="Valider", command=lambda: self.choose_room_menu(client_list, date_of_beginning_entry.get(), date_of_ending_entry.get()))
        validation_button.pack()
        cancel_button = Button(self.reserve_frame, text="Annuler", command= self.main_menu)
        cancel_button.pack()
        
    def choose_room_menu(self,client_list_var : StringVar, date_of_beginning_variable : str, date_of_ending_variable : str):
        """Display the choose room menu with the available rooms for the given time slot."""
        start_date = date_of_beginning_variable.split(' ')[0]
        end_date = date_of_ending_variable.split(' ')[0]
        regex = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4} ([01][0-9]|2[0-3]):[0-5][0-9]\b' 
        if not re.fullmatch(regex, date_of_beginning_variable) or not re.fullmatch(regex, date_of_ending_variable): # check if the date is in the following format : jj/mm/yyyy hh:mm
            self.show_error_message("Format de date invalide. Utilisez le format JJ/MM/AAAA HH:MM.")
            return
        
        start_day, start_month, start_year = map(int, start_date.split('/'))
        start_hour, start_minute = map(int, date_of_beginning_variable.split(' ')[1].split(':'))
        end_day, end_month, end_year = map(int, end_date.split('/'))
        end_hour, end_minute = map(int, date_of_beginning_variable.split(' ')[1].split(':'))
        rooms_available = self.controller.get_rooms_available(start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute)
        
        if (rooms_available == None ):
            self.show_error_message("Erreur lors de la récupération des salles disponibles.")
            return
        standard_rooms, conference_rooms, informatique_rooms = rooms_available
        if not standard_rooms and not conference_rooms and not informatique_rooms:
            # If no rooms are available, show an error message
            self.show_error_message("Aucune salle disponible pour ce créneau.")
            return

        self.hide_all()
        self.choose_room_frame.pack(fill="both", expand=1)
        choose_room_label = Label(self.choose_room_frame, text="Reserver une salle")
        choose_room_label.pack()
        client_label = Label(self.choose_room_frame, text=f"Client : {client_list_var.get()}")
        client_label.pack()
        begin_label = Label(self.choose_room_frame, text=f"Début:{date_of_beginning_variable}")
        begin_label.pack()
        end_label = Label(self.choose_room_frame, text=f"Fin:{date_of_ending_variable}")
        end_label.pack()
        duration_label = Label(self.choose_room_frame, text=f"Durée:{date_of_ending_variable} - {date_of_beginning_variable}")
        duration_label.pack()
        room_available_labbel = Label(self.choose_room_frame, text="Salles disponibles:")
        room_available_labbel.pack()
        room_list = ["Salle 1", "Salle 2", "Salle 3", "Salle 4", "Salle 5"]
        room_list_var = StringVar()
        room_list_var.set(room_list[0])  # Set default value
        room_option_menu = OptionMenu(self.choose_room_frame, room_list_var, *room_list)
        room_option_menu.pack()
        type_label = Label(self.choose_room_frame, text="Type de salle:")
        type_label.pack()
        type_of_room_standart_checkbutton = Checkbutton(self.choose_room_frame, text="Standart")
        type_of_room_standart_checkbutton.pack()
        type_of_room_conference_checkbutton = Checkbutton(self.choose_room_frame, text="Conférence")
        type_of_room_conference_checkbutton.pack()
        type_of_room_computeur_science_checkbutton= Checkbutton(self.choose_room_frame, text="Informatique")
        type_of_room_computeur_science_checkbutton.pack()
        validation_button = Button(self.choose_room_frame, text="valider", command=lambda :self.validation_of_reservation_menu(client_list_var, date_of_beginning_variable, date_of_ending_variable, room_list_var))
        validation_button.pack()
        cancel_button = Button(self.choose_room_frame, text="Annuler", command=self.reserve_menu)
        cancel_button.pack()

    def validation_of_reservation_menu(self,client_list_var : StringVar, date_of_beginning_variable : StringVar, date_of_ending_variable : StringVar, room_list_var : StringVar):
        self.hide_all()
        self.validation_of_reservation_frame.pack(fill="both", expand=1)
        validation_of_reservation_label = Label(self.validation_of_reservation_frame, text="Réservation Validée!")
        validation_of_reservation_label.pack()
        client_label = Label(self.validation_of_reservation_frame, text=f"Client: {client_list_var.get()}")
        client_label.pack()
        begining_label = Label(self.validation_of_reservation_frame, text=f"Début: {date_of_beginning_variable}")
        begining_label.pack()
        ending_label = Label(self.validation_of_reservation_frame, text=f"Fin: {date_of_ending_variable}")
        ending_label.pack()
        duration_label = Label(self.validation_of_reservation_frame, text=f"Durée: {date_of_ending_variable} - {date_of_beginning_variable}")
        duration_label.pack()
        room_label = Label(self.validation_of_reservation_frame, text=f"Salle: {room_list_var.get()}")
        room_label.pack()
        type_of_room_label = Label(self.validation_of_reservation_frame, text="Type de salle: ")
        type_of_room_label.pack()
        capacity_label = Label(self.validation_of_reservation_frame, text="Capacité: ")
        capacity_label.pack()
        reservation_details_label = Label(self.validation_of_reservation_frame, text="Détails de la réservation")
        reservation_details_label.pack()
        main_menu_button = Button(self.validation_of_reservation_frame, text="menu principal", command=self.main_menu)
        main_menu_button.pack()

    # hide all frames
    def hide_all(self):
    # destroy all widgets in the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        for widget in self.add_frame.winfo_children():
            widget.destroy()
        for widget in self.show_frame.winfo_children():
            widget.destroy()
        for widget in self.reserve_frame.winfo_children():
            widget.destroy()
        for widget in self.new_client_frame.winfo_children():
            widget.destroy()
        for widget in self.new_room_frame.winfo_children():
            widget.destroy()
        for widget in self.show_list_of_rooms_frame.winfo_children():
            widget.destroy()
        for widget in self.reservation_frame.winfo_children():
            widget.destroy()
        for widget in self.room_available_for_time_slot_frame.winfo_children():
            widget.destroy()
        for widget in self.choose_room_frame.winfo_children():
            widget.destroy()
        for widget in self.validation_of_reservation_frame.winfo_children():
            widget.destroy()

        # hide all frames
        self.new_client_frame.pack_forget()
        self.new_room_frame.pack_forget()
        self.main_frame.pack_forget()
        self.add_frame.pack_forget()
        self.show_frame.pack_forget()
        self.reserve_frame.pack_forget()
        self.show_list_of_rooms_frame.pack_forget()
        self.reservation_frame.pack_forget()
        self.room_available_for_time_slot_frame.pack_forget()
        self.choose_room_frame.pack_forget()
        self.validation_of_reservation_frame.pack_forget()
