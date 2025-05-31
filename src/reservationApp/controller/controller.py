from __future__ import annotations # if some class use type defined later 
from reservationApp.model.model import *
from reservationApp.model.view.view import View

class Reservation_app_error(Exception):
    """Base class for all exceptions raised by the reservation app"""
    pass


class Controller():
    def __init__(self):
        self.rooms_manager = RoomsManager()
        self.reservations_manager = ReservationsManager()
        self.clients_manager = ClientManager()
        self.model = Model(self.rooms_manager,self.reservations_manager,self.clients_manager)
        self.view :View
    
    def save(self) -> None:
        """Save the model data to a file"""
        self.model.save_data("./data/data.json")
    
    def run(self):
        """Run the app"""
        self.model.load_data("./data/data.json")
        self.view = View(self)
        self.view.main()
        self.model.save_data("./data/data.json")

    def add_client(self, name : str, first_name : str ,email : str) -> None :
        """Add a new client to the model"""
        try:
            self.clients_manager.add_client( name , first_name ,email )
            self.view.main_menu()
        except ClientError as e:
            self.view.show_error_message(str(e))    
        else:
            self.view.show_success_message(f"Client {name} {first_name} with email {email} added successfully.")
    
    def get_clients_dict(self) -> dict[str,Client]:
        """Get the list of clients"""
        return self.clients_manager.clients
    
    def get_clients_list(self) -> list[Client]:
        """Get the list of clients"""
        return self.clients_manager.clients_list
    
    def get_rooms_list(self) -> list[Room]:
        """Get the list of rooms"""
        return self.rooms_manager.rooms_list
    def add_room(self, name : str, type : str,capacity) -> None:
        """Add a new room to the model"""

        try:
            self.rooms_manager.add_room(name, type,capacity)
            self.view.main_menu()
        except RoomError as e:
            self.view.show_error_message(str(e))    
        else:
            self.view.show_success_message(f"Room {name} of type {type} with capacity {capacity} added successfully.")

    def get_reservations_of_client(self, client_email : str) -> list[Reservation]:
        client_reservations = []
        for reservation in self.reservations_manager.reservations.values():
            if reservation.client_id == client_email:
                client_reservations.append(reservation)
        return client_reservations

    def get_rooms_infos(self, room_name : str) -> Room:
        """Get the infos of a room"""
        return self.rooms_manager.rooms[room_name]

    def get_rooms_available_per_type(self,start_year,start_month,start_day,start_hour,minute,end_year,end_month,end_day,end_hour,end_minute)-> tuple[list[Room],list[Room],list[Room]] | None:
        """Give a list of all the available room for a time interval for each type"""
        availables_rooms = self.get_rooms_available(start_year,start_month,start_day,start_hour,minute,end_year,end_month,end_day,end_hour,end_minute)
        if availables_rooms == None:
            return
        standards_rooms = [room for room in availables_rooms if room.type == "Standard"]
        conferences_rooms = [room for room in availables_rooms if room.type == "Conference"]
        informatiques_rooms = [room for room in availables_rooms if room.type == "Informatique"]
        return  standards_rooms, conferences_rooms, informatiques_rooms
    def get_rooms_available(self,start_year,start_month,start_day,start_hour,minute,end_year,end_month,end_day,end_hour,end_minute)-> list[Room] | None:
        """Give a list of all the available room for a time interval"""
        try :
            time_interval = TimeInterval(datetime(start_year, start_month, start_day, start_hour, minute),datetime(end_year, end_month, end_day, end_hour, end_minute))
        except ValueError as e:
            self.view.show_error_message(f"Error creating time interval: {str(e)}")
            return None
        return  self.rooms_manager.get_available_rooms(time_interval)
    
    def add_reservation(self, room : str, time_interval : TimeInterval, client_email : str) -> None:
        """Create a new reservation for a room"""
        if not self.rooms_manager.is_a_room(room):
            raise Reservation_app_error(f"Room {room} does not exist")
        
        if client_email not in self.clients_manager.clients:
            raise Reservation_app_error(f"Client {client_email} does not exist")
        
        if not self.rooms_manager.rooms[room].is_available(time_interval):
            raise Reservation_app_error(f"Room {room} is not available for the time interval {time_interval}")
        
        if time_interval.start_datetime < datetime.today():
            raise Reservation_app_error(f"The start of the reservation has already passed")
        
        new_reservation = self.rooms_manager.rooms[room].create_reservations(time_interval,client_email)
        self.reservations_manager.add_reservations(new_reservation)
        

