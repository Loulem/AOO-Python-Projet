import tkinter as tk
import uuid
from abc import ABC, abstractmethod

class Model:
    def __init__(self):
        self.uuid = []

    def append(self, item):
        self.uuid.append(item)

    def clear(self):
        self.uuid = []

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def start(self):
        self.view.setup(self)
        self.view.start_main_loop()

    def handle_click_generate_uuid(self):
        # generate a uuid and add it to the list
        newid = uuid.uuid4()
        self.model.append(newid)
        self.view.append_to_list(newid)

    def handle_click_clear_list(self):
        # clear the uuid list in the model and the view
        self.model.clear()
        self.view.clear_list()

class View(ABC):
    @abstractmethod
    def setup(self, controller):
        pass

    @abstractmethod
    def append_to_list(self, item):
        pass

    @abstractmethod
    def clear_list(self):
        pass
    
    @abstractmethod
    def start_main_loop(self):
        pass

class TkView(View):
    def setup(self, controller):

        def change_frame_add_new_client():
            # destroy the current frame and create a new one
            self.frame.pack_forget()
            frame_add_new_client.pack(fill=tk.BOTH, expand=1)
        
        def change_frame_add_a_new_room():
            # destroy the current frame and create a new one
            self.frame.pack_forget()
            frame_add_new_room.pack(fill=tk.BOTH, expand=1)

        def change_frame_display_reservable_room():
            # destroy the current frame and create a new one
            self.frame.pack_forget()
            frame_display_reservable_room.pack(fill=tk.BOTH, expand=1)
        
        def change_frame_display_reservation_of_a_client():
            # destroy the current frame and create a new one
            self.frame.pack_forget()
            frame_display_client_reservation.pack(fill=tk.BOTH, expand=1)

        def change_frame_identify_if_a_room_is_free_in_a_time_slot():
            # destroy the current frame and create a new one
            self.frame.pack_forget()
            frame_identify_if_room_is_free_in_a_time_slot.pack(fill=tk.BOTH, expand=1)

        def change_frame_display_room_free_in_a_time_slot():
            # destroy the current frame and create a new one
            self.frame.pack_forget()
            frame_display_rooms_free_in_a_time_slot.pack(fill=tk.BOTH, expand=1)

        def change_frame_room_reservation():
            # destroy the current frame and create a new one
            self.frame.pack_forget()
            frame_room_reservation.pack(fill=tk.BOTH, expand=1)
        
        
        # setup tkinter
        self.root = tk.Tk()
        self.root.geometry("1080x720")
        self.root.minsize(480,360)
        self.root.title("MeetingPro")
        self.root.iconbitmap("src/MeetingPro.ico")
    
        # create the gui
        self.frame = tk.Frame(self.root, bg="red")
        self.frame.pack(fill=tk.BOTH, expand=1)
        self.label = tk.Label(self.frame, text="Result:", bg="yellow")
        self.label.pack()
        self.add_new_client = tk.Button(self.frame, text="Ajouter un nouveau client", command=change_frame_add_new_client)
        self.add_new_client.pack()
        self.add_a_new_room = tk.Button(self.frame, text="Ajouter une nouvelle salle", command=change_frame_add_a_new_room)
        self.add_a_new_room.pack()
        self.display_reservable_room = tk.Button(self.frame, text="Afficher les salles réservables", command=change_frame_display_reservable_room)
        self.display_reservable_room.pack()
        self.display_resevation_of_a_client = tk.Button(self.frame, text="Afficher les réservations pour un client", command=change_frame_display_reservation_of_a_client)
        self.display_resevation_of_a_client.pack()
        self.identify_if_a_room_is_free_in_a_time_slot = tk.Button(self.frame, text="Identifier si une salle est disponible sur un créneau", command=change_frame_identify_if_a_room_is_free_in_a_time_slot)
        self.identify_if_a_room_is_free_in_a_time_slot.pack()
        self.display_room_free_in_a_time_slot = tk.Button(self.frame, text="Afficher les salles disponibles pour un créneau", command=change_frame_display_room_free_in_a_time_slot)
        self.display_room_free_in_a_time_slot.pack()
        self.reservation_room = tk.Button(self.frame, text="Réserver une salle", command=change_frame_room_reservation)
        self.reservation_room.pack()


        # create the "Ajouter un nouveau client" Frame
        frame_add_new_client = tk.Frame(self.root, bg="orange")

        # create the "Ajouter une nouvelle salle" Frame
        frame_add_new_room = tk.Frame(self.root, bg="purple")

        # create the "Afficher les salles réservables" Frame
        frame_display_reservable_room = tk.Frame(self.root, bg="blue")

        # create the "Afficher les réservations pour un client" Frame
        frame_display_client_reservation = tk.Frame(self.root, bg="pink")

        # create the "Identifier si une salle est disponible sur un créneau" Frame
        frame_identify_if_room_is_free_in_a_time_slot = tk.Frame(self.root, bg="cyan")

        # create the "Afficher les salles disponibles pour un créneau" Frame
        frame_display_rooms_free_in_a_time_slot = tk.Frame(self.root, bg="grey")

         # create the "Réserver une salle" Frame
        frame_room_reservation = tk.Frame(self.root, bg="green")

    

        '''
        self.list = tk.Listbox(self.frame, bg="blue", fg="white")
        self.list.pack(fill=tk.BOTH, expand=1)
        self.generate_uuid_button = tk.Button(self.frame, text="Generate UUID", command=controller.handle_click_generate_uuid)
        self.generate_uuid_button.pack()
        self.clear_button = tk.Button(self.frame, text="Clear list", command=controller.handle_click_clear_list)
        self.clear_button.pack()
        '''
    def append_to_list(self, item):
        self.list.insert(tk.END, item)

    def clear_list(self):
        self.list.delete(0, tk.END)
    
    def start_main_loop(self):
        # start the loop
        self.root.mainloop()

# create the MVC & start the application
c = Controller(Model(), TkView())
c.start()