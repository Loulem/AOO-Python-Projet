from __future__ import annotations
from tkinter import *
import re
from tkinter import ttk     
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from reservationApp.controller.controller import Controller  # imported only for type checking
    from reservationApp.model.model import Client, Room, TimeInterval
    from reservationApp.model.client.client import Client
from reservationApp.model.time_Interval import TimeInterval
from datetime import datetime, timedelta

class View():
    def __init__(self,controller :"Controller"):    
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
        self.client_reservation_frame = Frame(self.root, bg="white")
        self.main_menu()


    
    def main(self):
        """Main function to start the application."""
        self.root.mainloop()

# change menu
    def main_menu(self):
        self.hide_all()
        self.main_frame.pack(fill="both", expand=1)
        center_frame = Frame(self.main_frame, bg="white")
        center_frame.pack(expand=True)
        add_button = Button(center_frame,fg="white",bg="blue4", text="Ajouter", command=self.add_menu,height=1, width=20,font=(15))
        show_button = Button(center_frame,fg="white",bg="blue4", text="Afficher", command=self.show_menu,height=1, width=20,font=(15))
        book_button = Button(center_frame,fg="white",bg="blue4", text="Réserver", command=self.reserve_menu,height=1, width=20,font=(15))
        add_button.pack(padx=20, pady=20)
        show_button.pack(padx=20, pady=20)
        book_button.pack(padx=20, pady=20)

    def add_menu(self):
        self.hide_all()
        self.add_frame.pack(fill="both", expand=1)
        center_frame = Frame(self.add_frame, bg="white")
        center_frame.pack(expand=True)
        add_new_client_button = Button(center_frame,fg="white",bg="blue4", text="Ajouter un client", command=self.new_client_menu,height=1, width=20,font=(15))
        add_new_client_button.pack(padx=20, pady=20)
        add_new_room_button = Button(center_frame,fg="white",bg="blue4", text="Ajouter une salle", command=self.new_room_menu,height=1, width=20,font=(15))
        add_new_room_button.pack(padx=20, pady=20)

    def new_client_menu(self):
        self.hide_all()
        self.new_client_frame.pack(fill="both", expand=1)
        fields_frame = Frame(self.new_client_frame, bg="white")
        fields_frame.pack(anchor="w", padx=20, pady=40, fill="x")
        buttons_frame = Frame(self.new_client_frame, bg="white")
        buttons_frame.pack(side="bottom", fill="x", pady=20, padx=20)
        new_client_label = Label(fields_frame, text="Ajouter un client",bg="white",font=(15))
        new_client_label.pack()
        new_client_name_entry = Entry(fields_frame,bg="powderblue",font=(15))
        new_client_name_entry.insert(0, "Prénom")
        new_client_name_entry.pack()
        new_client_surname_entry = Entry(fields_frame,bg="powderblue",font=(15))
        new_client_surname_entry.insert(0, "Nom de famille")
        new_client_surname_entry.pack()
        new_client_email_entry = Entry(fields_frame,bg="powderblue",font=(15))
        new_client_email_entry.insert(0, "example@mail.fr")
        new_client_email_entry.pack()
        validation_button = Button(buttons_frame,fg="white",bg="blue4", text="valider", command= lambda : self.controller.add_client(new_client_name_entry.get(),new_client_surname_entry.get(),new_client_email_entry.get()),height=1, width=20,font=(15))
        validation_button.pack(side="right", anchor="se")
        cancel_button = Button(buttons_frame,fg="white",bg="blue4", text="Annuler", command=self.add_menu,height=1, width=20,font=(15))
        cancel_button.pack(side="left", anchor="sw")

    def show_error_message(self, message: str):
        """Display an error message in a popup window."""
        error_window = Toplevel(self.root)
        error_window.title("Erreur")
        error_label = Label(error_window, text=message, fg="red")
        error_label.pack(pady=20) 
        close_button = Button(error_window,fg="white",bg="blue4", text="Fermer", command=error_window.destroy)
        close_button.pack(pady=10)
        error_window.geometry("300x150")

    def show_success_message(self, message: str):
        """Display a success message in a popup window."""
        success_window = Toplevel(self.root)
        success_window.title("Succès")
        success_label = Label(success_window, text=message, fg="green")
        success_label.pack(pady=20)
        close_button = Button(success_window, text="Fermer", command=success_window.destroy,fg="white",bg="blue4")
        close_button.pack(pady=10)
        success_window.geometry("700x100")

    def new_room_menu(self):
        self.hide_all()
        self.new_room_frame.pack(fill="both", expand=1)
        new_room_label = Label(self.new_room_frame, text="Ajouter une nouvelle salle",bg="white")
        new_room_label.pack()
        var = StringVar()
        new_room_name_entry = Entry(self.new_room_frame, text="Nom de la salle",bg="powderblue") # TODO remove use of text parameter
        new_room_name_entry.pack()

        capacity = [str(i) for i in range(1,14)]
        capacity_list = StringVar()
        capacity_list.set(capacity[0])  # Set default value
        new_room_capacity = OptionMenu(self.new_room_frame, capacity_list, *capacity)
        new_room_capacity.pack()

        type_of_room = ["Standard", "Conference", "Informatique"]
        type_of_room_list = StringVar()
        type_of_room_list.set(type_of_room[0])  # Set default value
        new_room_type = OptionMenu(self.new_room_frame, type_of_room_list, *type_of_room)
        new_room_type.pack()

        validation_button = Button(self.new_room_frame, text="valider", command=lambda:self.controller.add_room(new_room_name_entry.get(), type_of_room_list.get(), capacity_list.get()),fg="white",bg="blue4")
        validation_button.pack()
        cancel_button = Button(self.new_room_frame, text="Annuler", command=self.add_menu,fg="white",bg="blue4")
        cancel_button.pack()


    def show_menu(self):
        self.hide_all()
        self.show_frame.pack(fill="both", expand=1)
        show_list_of_rooms_button = Button(self.show_frame, text="Afficher la liste des salles", command=self.show_list_of_rooms,fg="white",bg="blue4")
        show_list_of_rooms_button.pack()
        show_list_of_clients_button = Button(self.show_frame, text="Afficher la liste des clients",fg="white",bg="blue4")
        show_list_of_clients_button.pack()
        show_rooms_for_time_slot_button = Button(self.show_frame, text="Afficher les salles disponibles pour un créneau",command=self.room_available_for_time_slot_menu,fg="white",bg="blue4")
        show_rooms_for_time_slot_button.pack()
        show_book_of_clients_button = Button(self.show_frame, text="Afficher les reservation d'un clients", command=self.reservation_menu,fg="white",bg="blue4")
        show_book_of_clients_button.pack()

    def reservation_menu(self):# TODO change the name of this function to show_reservation_menu
        """Display the reservation menu where the user can choose a client to reserve a room."""
        self.hide_all()
        self.reservation_frame.pack(fill="both", expand=1)
        reservation_label = Label(self.reservation_frame, text="Réservation du client",bg="white")
        reservation_label.pack()
        client_list= StringVar()
        client_label = Label(self.reservation_frame, text="Client:",bg="white")
        client_label.pack()
        client_dict = self.controller.get_clients_dict()  
        # TODO if the list is empty there is an error, add something to handle this case
        
        client_keys = list(client_dict.keys())
        client_list = StringVar()

        if not client_keys:
            client_keys = ["Aucun client disponible"]
            client_list.set(client_keys[0])
        else:
            client_list.set(client_keys[0])

        client_option_menu = OptionMenu(self.reservation_frame, client_list, *client_keys)
        client_option_menu.pack()

        validation_button = Button(self.reservation_frame, text="valider", command=lambda :self.client_reservation_menu(client_list.get()),fg="white",bg="blue4")
        validation_button.pack()
        cancel_button = Button(self.reservation_frame, text="Annuler", command=self.show_menu,fg="white",bg="blue4")
        cancel_button.pack()

    def client_reservation_menu(self,client_list_var : str):
        self.hide_all()
        self.client_reservation_frame.pack(fill="both", expand=1)
        reservation_of_client_label = Label(self.client_reservation_frame, text="Réservation du client",bg="white")
        reservation_of_client_label.pack()
        client_label = Label(self.client_reservation_frame, text="Client:",bg="white")
        client_label.pack()
        reservation_label= Label(self.client_reservation_frame, text="Réservation:",bg="white")
        reservation_label.pack()
        show_client_label = Label(self.client_reservation_frame, text=f"Client: {client_list_var}",bg="white")
        show_client_label.pack()
        back_button = Button(self.client_reservation_frame, text="Retour", command=self.reservation_menu,fg="white",bg="blue4")
        back_button.pack()
        
        # Get the list of rooms and display them in the listboxcolumns = ("Nom", "Type", "Capacité")
        columns = ("Salle", "Type", "Capacité", "Début", "Fin", "Durée")
        tree = ttk.Treeview(self.client_reservation_frame, columns=columns, show="headings", height=10)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center")
        try:
            reservations = self.controller.get_rooms_list()
            if not reservations:
                tree.insert("", "end", values=("Aucune reservation"))
            else:
                for reservation in reservations:
                    tree.insert("", "end", values=(reservation.name, reservation.type, reservation.capacity,reservation.Time_interval, reservation.start_datetime, reservation.duration))
        except Exception as e:
            self.show_error_message(f"Erreur lors de la récupération des salles : {e}")
        tree.pack(fill="both", expand=1, padx=20, pady=10)


    def room_available_for_time_slot_menu(self):
        self.hide_all()
        self.room_available_for_time_slot_frame.pack(fill="both", expand=1)
        room_available_for_time_slot_label = Label(self.room_available_for_time_slot_frame, text="Salles disponibles pour le créneau",bg="white")
        room_available_for_time_slot_label.pack()
        begin_label = Label(self.room_available_for_time_slot_frame, text="Début:",bg="white")
        begin_label.pack()
        date_of_beginning_entry = Entry(self.room_available_for_time_slot_frame,bg="powderblue")
        date_of_beginning_entry.insert(0, "Date de début")
        date_of_beginning_entry.pack()
        end_label = Label(self.room_available_for_time_slot_frame, text="Fin:",bg="white")
        end_label.pack()
        date_of_ending_entry = Entry(self.room_available_for_time_slot_frame,bg="powderblue")
        date_of_ending_entry.insert(0, "Date de fin")
        date_of_ending_entry.pack()
        validation_button = Button(self.room_available_for_time_slot_frame, text="valider", command=self.main_menu,fg="white",bg="blue4")
        validation_button.pack()
        cancel_button = Button(self.room_available_for_time_slot_frame, text="Annuler", command=self.show_menu,fg="white",bg="blue4")
        cancel_button.pack()

    def show_list_of_rooms(self):
        self.hide_all()
        self.show_frame.pack(fill="both", expand=1)

        # Titre
        show_list_of_rooms_label = Label(self.show_frame, text="Liste des salles")
        show_list_of_rooms_label.pack()

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


    def reserve_menu(self):
        self.hide_all()
        self.reserve_frame.pack(fill="both", expand=1)
        reserve_label = Label(self.reserve_frame, text="Réserver une salle",bg="white")
        reserve_label.pack()
        begin_label = Label(self.reserve_frame, text="Début:",bg="white")
        begin_label.pack()
        date_of_beginning_entry = Entry(self.reserve_frame,bg="powderblue")
        date_of_beginning_entry.insert(0, "01/01/2024 12:00")  # Example date format
        date_of_beginning_entry.pack()
        end_label = Label(self.reserve_frame, text="Fin:",bg="white")
        end_label.pack()
        date_of_ending_entry = Entry(self.reserve_frame,bg="powderblue")
        date_of_ending_entry.insert(0, "01/01/2024 13:00")
        date_of_ending_entry.pack()
        client_label = Label(self.reserve_frame, text="Client:",bg="white")
        client_label.pack()
        client_dict = self.controller.get_clients_dict()  
        client = list(client_dict.keys())  # Create a list of client names
        
        # TODO if the list is empty there is an error, add something to handle this case
        client_list= StringVar()
        
        if client == []:
            client_list.set("Aucun client disponible")  # Set default value if no clients are available
        else : 
            client_list.set(client[0])  # Set default value
            client_option_menu = OptionMenu(self.reserve_frame, client_list, *client)
            client_option_menu.pack()
        type_of_room_label = Label(self.reserve_frame, text="Type:",bg="white")
        type_of_room_label.pack()
        validation_button = Button(self.reserve_frame, text="Valider", command=lambda: self.choose_room_menu(client_dict[client_list.get()], date_of_beginning_entry.get(), date_of_ending_entry.get()),fg="white",bg="blue4")
        validation_button.pack()
        cancel_button = Button(self.reserve_frame, text="Annuler", command=lambda: self.main_menu(),fg="white",bg="blue4")
        cancel_button.pack()
        
    def choose_room_menu(self,client : "Client", date_of_beginning_variable : str, date_of_ending_variable : str):
        """Display the choose room menu with the available rooms for the given time slot."""
        regex = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4} ([01][0-9]|2[0-3]):[0-5][0-9]\b'
        if not re.fullmatch(regex, date_of_beginning_variable) or not re.fullmatch(regex, date_of_ending_variable): # check if the date is in the following format : jj/mm/yyyy hh:mm
            self.show_error_message("Format de date invalide. Utilisez le format JJ/MM/AAAA HH:MM.")
            return
        start_date = date_of_beginning_variable.split(' ')[0]
        end_date = date_of_ending_variable.split(' ')[0]
        
        start_day, start_month, start_year = map(int, start_date.split('/'))
        start_hour, start_minute = map(int, date_of_beginning_variable.split(' ')[1].split(':'))
        end_day, end_month, end_year = map(int, end_date.split('/'))
        end_hour, end_minute = map(int, date_of_ending_variable.split(' ')[1].split(':'))
        rooms_available = self.controller.get_rooms_available(start_year, start_month, start_day, start_hour, start_minute, end_year, end_month, end_day, end_hour, end_minute)
        time_interval = TimeInterval(datetime(start_year, start_month, start_day, start_hour, start_minute), datetime(end_year, end_month, end_day, end_hour, end_minute))
        if time_interval.start_datetime < datetime.today():
            self.show_error_message("La date de début de la réservation est déjà passée.")
            return
        
        if (rooms_available == None ):
            
            return
        standard_rooms, conference_rooms, computer_rooms = rooms_available
        
        if not standard_rooms and not conference_rooms and not computer_rooms:
            # If no rooms are available, show an error message
            self.show_error_message("Aucune salle disponible pour ce créneau.")
            return


        self.hide_all()
        self.choose_room_frame.pack(fill="both", expand=1)
        choose_room_label = Label(self.choose_room_frame, text="Reserver une salle",bg="white")
        choose_room_label.pack()
        client_label = Label(self.choose_room_frame, text=f"Client : name {client.name}, first name :{client.first_name}, email :{client.email}",bg="white")
        client_label.pack()
        begin_label = Label(self.choose_room_frame, text=f"Début:{time_interval.start_datetime}",bg="white")
        begin_label.pack()
        end_label = Label(self.choose_room_frame, text=f"Fin:{time_interval.end_datetime}",bg="white")
        end_label.pack()
        duration_label = Label(self.choose_room_frame, text=f"Durée:{time_interval.duration}",bg="white")
        duration_label.pack()
        room_available_labbel = Label(self.choose_room_frame, text="Salles disponibles:",bg="white")
        room_available_labbel.pack()
        
        
        type_label = Label(self.choose_room_frame, text="Type de salle:",bg="white")
        type_label.pack()
        standard_checkbutton = IntVar()
        type_of_room_standard_checkbutton = Checkbutton(self.choose_room_frame, text="Standard", variable=standard_checkbutton)
        type_of_room_standard_checkbutton.pack()
        conference_checkbutton = IntVar()
        type_of_room_conference_checkbutton = Checkbutton(self.choose_room_frame, text="Conférence", variable=conference_checkbutton)
        type_of_room_conference_checkbutton.pack()
        computer_checkbutton = IntVar()
        type_of_room_computer_science_checkbutton = Checkbutton(self.choose_room_frame, text="Informatique", variable=computer_checkbutton)
        type_of_room_computer_science_checkbutton.pack()

        room_list_var = StringVar()
        room_list = []
        room_option_menu = OptionMenu(self.choose_room_frame, room_list_var, "")
        room_option_menu.pack()

        def update_room_list(*arg):
            room_list.clear()
            if standard_checkbutton.get():
                room_list.extend(standard_rooms)
            if conference_checkbutton.get():
                room_list.extend(conference_rooms)
            if computer_checkbutton.get():
                room_list.extend(computer_rooms)
            room_option_menu['menu'].delete(0, 'end')
            for room in room_list:
                room_option_menu['menu'].add_command(label=room, command=lambda value=room: room_list_var.set(value))
            if room_list:
                room_list_var.set(room_list[0])
            else:
                room_list_var.set("")

        type_of_room_standard_checkbutton.config(command=update_room_list)
        type_of_room_conference_checkbutton.config(command=update_room_list)
        type_of_room_computer_science_checkbutton.config(command=update_room_list)
        update_room_list()

        validation_button = Button(self.choose_room_frame, text="Valider", command=lambda: self.validation_of_reservation_menu(client, time_interval, room_list_var),fg="white",bg="blue4")
        validation_button.pack()
        cancel_button = Button(self.choose_room_frame, text="Annuler", command=self.reserve_menu,fg="white",bg="blue4")
        cancel_button.pack()

    def validation_of_reservation_menu(self,client_list_var : "Client", time_interval : TimeInterval, room_list_var : StringVar):
        self.hide_all()
        

        self.validation_of_reservation_frame.pack(fill="both", expand=1)
        validation_of_reservation_label = Label(self.validation_of_reservation_frame, text="Réservation Validée!",bg="white")
        validation_of_reservation_label.pack()
        first_name = client_list_var.first_name
        last_name = client_list_var.name
        room_name = room_list_var.get().split(" ")[2]
        room_name = room_name.replace(",", "")
        room_type = room_list_var.get().split(" ")[5]
        room_type = room_type.replace(",", "")
        room_capacity = room_list_var.get().split(" ")[8] 
        try :
            self.controller.add_reservation(room_name, time_interval, client_list_var.email)
        except Exception as e:
            self.show_error_message(f"Erreur lors de la réservation : {str(e)}")
            return
        room_capacity = room_capacity.replace("}", "")
        client_label = Label(self.validation_of_reservation_frame, text=f"Client: {first_name}{last_name}",bg="white")
        client_label.pack()
        begining_label = Label(self.validation_of_reservation_frame, text=f"Début: {time_interval.start_datetime}",bg="white")
        begining_label.pack()
        ending_label = Label(self.validation_of_reservation_frame, text=f"Fin: {time_interval.end_datetime}",bg="white")
        ending_label.pack()
        duration_label = Label(self.validation_of_reservation_frame, text=f"Durée: { time_interval.duration }",bg="white")
        duration_label.pack()
        room_label = Label(self.validation_of_reservation_frame, text=f"Salle: {room_name}",bg="white")
        room_label.pack()
        type_of_room_label = Label(self.validation_of_reservation_frame, text=f"Type de salle: {room_type}",bg="white")
        type_of_room_label.pack()
        capacity_label = Label(self.validation_of_reservation_frame, text=f"Capacité: {room_capacity}",bg="white")
        capacity_label.pack()
        reservation_details_label = Label(self.validation_of_reservation_frame, text="Détails de la réservation",bg="white")
        reservation_details_label.pack()
        main_menu_button = Button(self.validation_of_reservation_frame, text="menu principal", command=self.main_menu,fg="white",bg="blue4")
        main_menu_button.pack()
        #self.controller.save()

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
        for widget in self.client_reservation_frame.winfo_children():
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
        self.client_reservation_frame.pack_forget()
