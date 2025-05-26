from tkinter import *


root = Tk()
root.title("MeetingPro")
root.geometry("1080x720")
root.minsize(480, 360)
root.iconbitmap("src/MeetingPro.ico")


# change menu
def main_menu():
    hide_all()
    main_frame.pack(fill="both", expand=1)
    add_button = Button(main_frame, text="Ajouter", command=add_menu)
    show_button = Button(main_frame, text="Afficher", command=show_menu)
    book_button = Button(main_frame, text="Réserver", command=reserve_menu)
    add_button.pack()
    show_button.pack()
    book_button.pack()

def add_menu():
    hide_all()
    add_frame.pack(fill="both", expand=1)
    add_new_client_button = Button(add_frame, text="Ajouter un client", command=new_client_menu)
    add_new_client_button.pack()
    add_new_room_button = Button(add_frame, text="Ajouter une salle", command=new_room_menu)
    add_new_room_button.pack()

def new_client_menu():
    hide_all()
    new_client_frame.pack(fill="both", expand=1)
    new_client_label = Label(new_client_frame, text="Ajouter un client")
    new_client_label.pack()
    new_client_name_entry = Entry(new_client_frame)
    new_client_name_entry.insert(0, "Prénom")
    new_client_name_entry.pack()
    new_client_surname_entry = Entry(new_client_frame)
    new_client_surname_entry.insert(0, "Nom de famille")
    new_client_surname_entry.pack()
    new_client_email_entry = Entry(new_client_frame)
    new_client_email_entry.insert(0, "Email")
    new_client_email_entry.pack()
    validation_button = Button(new_client_frame, text="valider", command=main_menu)
    validation_button.pack()
    cancel_button = Button(new_client_frame, text="Annuler", command=add_menu)
    cancel_button.pack()

def new_room_menu():
    hide_all()
    new_room_frame.pack(fill="both", expand=1)
    new_room_label = Label(new_room_frame, text="Ajouter une nouvelle salle")
    new_room_label.pack()

    new_room_name_entry = Entry(new_room_frame, text="Nom de la salle")
    new_room_name_entry.pack()

    capacity = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    capacity_list = StringVar()
    capacity_list.set(capacity[0])  # Set default value
    new_room_capacity = OptionMenu(new_room_frame, capacity_list, *capacity)
    new_room_capacity.pack()

    type_of_room = ["Salle de réunion", "Salle de conférence", "Bureau"]
    type_of_room_list = StringVar()
    type_of_room_list.set(type_of_room[0])  # Set default value
    new_room_type = OptionMenu(new_room_frame, type_of_room_list, *type_of_room)
    new_room_type.pack()

    validation_button = Button(new_room_frame, text="valider", command=main_menu)
    validation_button.pack()
    cancel_button = Button(new_room_frame, text="Annuler", command=add_menu)
    cancel_button.pack()

def show_menu():
    hide_all()
    show_frame.pack(fill="both", expand=1)
    show_list_of_rooms_button = Button(show_frame, text="Afficher la liste des salles", command=show_list_of_rooms)
    show_list_of_rooms_button.pack()
    show_list_of_clients_button = Button(show_frame, text="Afficher la liste des clients")
    show_list_of_clients_button.pack()
    show_rooms_for_time_slot_button = Button(show_frame, text="Afficher les salles disponibles pour un créneau",command=room_available_for_time_slot_menu)
    show_rooms_for_time_slot_button.pack()
    show_book_of_clients_button = Button(show_frame, text="Afficher les reservation d'un clients", command=reservation_menu)
    show_book_of_clients_button.pack()

def reservation_menu():
    hide_all()
    reservation_frame.pack(fill="both", expand=1)
    reservation_label = Label(reservation_frame, text="Réservation du client")
    reservation_label.pack()
    client_label = Label(reservation_frame, text="Client:")
    client_label.pack()
    client =["Client 1", "Client 2", "Client 3", "Client 4", "Client 5"]
    client_list= StringVar()
    client_list.set(client[0])  # Set default value
    client_option_menu = OptionMenu(reservation_frame, client_list, *client)
    client_option_menu.pack()
    validation_button = Button(reservation_frame, text="valider", command=main_menu)
    validation_button.pack()
    cancel_button = Button(reservation_frame, text="Annuler", command=show_menu)
    cancel_button.pack()

def room_available_for_time_slot_menu():
    hide_all()
    room_available_for_time_slot_frame.pack(fill="both", expand=1)
    room_available_for_time_slot_label = Label(room_available_for_time_slot_frame, text="Salles disponibles pour le créneau")
    room_available_for_time_slot_label.pack()
    begin_label = Label(room_available_for_time_slot_frame, text="Début:")
    begin_label.pack()
    date_of_beginning_entry = Entry(room_available_for_time_slot_frame)
    date_of_beginning_entry.insert(0, "Date de début")
    date_of_beginning_entry.pack()
    end_label = Label(room_available_for_time_slot_frame, text="Fin:")
    end_label.pack()
    date_of_ending_entry = Entry(room_available_for_time_slot_frame)
    date_of_ending_entry.insert(0, "Date de fin")
    date_of_ending_entry.pack()
    validation_button = Button(room_available_for_time_slot_frame, text="valider", command=main_menu)
    validation_button.pack()
    cancel_button = Button(room_available_for_time_slot_frame, text="Annuler", command=show_menu)
    cancel_button.pack()
  

def show_list_of_rooms():
    hide_all()
    show_frame.pack(fill="both", expand=1)
    show_list_of_rooms_label = Label(show_frame, text="Liste des salles")
    show_list_of_rooms_label.pack()
    listbox = Listbox(show_frame)
    listbox.pack(fill="both", expand=1)
    # add a scrollbar
    scrollbar = Scrollbar(show_frame)
    scrollbar.pack(side="right", fill="y")
    listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=listbox.yview)
    # add some items to the listbox
    for i in range(100):
        listbox.insert(END, "Salle " + str(i))

def reserve_menu():
    hide_all()
    reserve_frame.pack(fill="both", expand=1)
    reserve_label = Label(reserve_frame, text="Réserver une salle")
    reserve_label.pack()
    begin_label = Label(reserve_frame, text="Début:")
    begin_label.pack()
    date_of_beginning_entry = Entry(reserve_frame)
    date_of_beginning_entry.insert(0, "Date de début")
    date_of_beginning_entry.pack()
    end_label = Label(reserve_frame, text="Fin:")
    end_label.pack()
    date_of_ending_entry = Entry(reserve_frame)
    date_of_ending_entry.insert(0, "Date de fin")
    date_of_ending_entry.pack()
    client_label = Label(reserve_frame, text="Client:")
    client_label.pack()
    client =["Client 1", "Client 2", "Client 3", "Client 4", "Client 5"] # a modifier pour recuperer la liste des clients
    client_list= StringVar()
    client_list.set(client[0])  # Set default value
    client_option_menu = OptionMenu(reserve_frame, client_list, *client)
    client_option_menu.pack()
    validation_button = Button(reserve_frame, text="Valider", command=lambda: choose_room_menu(client_option_menu))
    validation_button.pack()
    cancel_button = Button(reserve_frame, text="Annuler", command=choose_room_menu)
    cancel_button.pack()
    




def choose_room_menu(client_option_menu : StringVar):
    #print(client_option_menu.getvar(client_option_menu.cget("textvariable")))
    #client_selected = client_option_menu.getvar(client_option_menu.cget("textvariable"))
    hide_all()
    choose_room_frame.pack(fill="both", expand=1)
    choose_room_label = Label(choose_room_frame, text="Reserver une salle")
    choose_room_label.pack()
    client_label = Label(choose_room_frame, text=f"Client : {client_option_menu.get()}")
    client_label.pack()
    begin_label = Label(choose_room_frame, text="Début:")
    begin_label.pack()
    end_label = Label(choose_room_frame, text="Fin:")
    end_label.pack()
    duration_label = Label(choose_room_frame, text="Durée:")
    duration_label.pack()
    room_available_labbel = Label(choose_room_frame, text="Salles disponibles:")
    room_available_labbel.pack()
    room_list = ["Salle 1", "Salle 2", "Salle 3", "Salle 4", "Salle 5"]
    room_list_var = StringVar()
    room_list_var.set(room_list[0])  # Set default value
    room_option_menu = OptionMenu(choose_room_frame, room_list_var, *room_list)
    room_option_menu.pack()
    type_label = Label(choose_room_frame, text="Type de salle:")
    type_label.pack()
    validation_button = Button(choose_room_frame, text="valider", command=main_menu)
    validation_button.pack()
    cancel_button = Button(choose_room_frame, text="Annuler", command=reserve_menu)
    cancel_button.pack()


# hide all frames
def hide_all():
    # destroy all widgets in the main frame
    for widget in main_frame.winfo_children():
        widget.destroy()
    for widget in add_frame.winfo_children():
        widget.destroy()
    for widget in show_frame.winfo_children():
        widget.destroy()
    for widget in reserve_frame.winfo_children():
        widget.destroy()
    for widget in new_client_frame.winfo_children():
        widget.destroy()
    for widget in new_room_frame.winfo_children():
        widget.destroy()
    for widget in show_list_of_rooms_frame.winfo_children():
        widget.destroy()
    for widget in reservation_frame.winfo_children():
        widget.destroy()
    for widget in room_available_for_time_slot_frame.winfo_children():
        widget.destroy()
    for widget in choose_room_frame.winfo_children():
        widget.destroy()

    # hide all frames
    new_client_frame.pack_forget()
    new_room_frame.pack_forget()
    main_frame.pack_forget()
    add_frame.pack_forget()
    show_frame.pack_forget()
    reserve_frame.pack_forget()
    show_list_of_rooms_frame.pack_forget()
    reservation_frame.pack_forget()
    room_available_for_time_slot_frame.pack_forget()
    choose_room_frame.pack_forget()


# create a menu bar
my_menu = Menu(root)
root.config(menu=my_menu)
file_menu = Menu(my_menu)
my_menu.add_checkbutton(label="accueil", command=main_menu)
my_menu.add_checkbutton(label="ajouter", command=add_menu)
my_menu.add_checkbutton(label="réserver", command=reserve_menu)
my_menu.add_checkbutton(label="afficher", command=show_menu)

# create menu
main_frame = Frame(root, bg="white")
add_frame = Frame(root, bg="white")
show_frame = Frame(root, bg="white")
reserve_frame = Frame(root, bg="white")
new_client_frame = Frame(root, bg="white")
new_room_frame = Frame(root, bg="white")
show_list_of_rooms_frame = Frame(root, bg="white")
reservation_frame = Frame(root, bg="white")
room_available_for_time_slot_frame = Frame(root, bg="white")
choose_room_frame = Frame(root, bg="white")
main_menu()

root.mainloop()