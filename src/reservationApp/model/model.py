from __future__ import annotations # if some class use type defined later 
from reservationApp.model.client import *
from reservationApp.model.reservation import *
from reservationApp.model.room.room import *
import json

class Reservation_app_error(Exception):
    """Base class for all exceptions raised by the reservation app"""
    pass


class Controller():
    def __init__(self):
        self.rooms_manager = RoomsManager()
        self.reservations_manager = ReservationsManager()
        self.clients_manager = ClientManager()


    def load_data(self, file :str ) -> None: # to model
        """Load the data from a json file """
        #TODO:try to load data with alternative constructors in clients rooms and reservations
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.rooms_manager.add_rooms_from_json(data["rooms"], self.reservations_manager)
            self.clients_manager.add_clients_from_json(data["clients"])
            
    def data_to_dictionnary(self) -> dict [str,dict[str,dict]]: # to model
        """Return the data in a dictionnary format"""
        return  {
            "clients" : self.clients_manager.to_dictionnary(),
            "rooms" : self.rooms_manager.to_dictionnary(),
        }

    def save_data(self, file ) -> None: # to model
        """Save the data to a json file"""
        data = self.data_to_dictionnary()  # Convert all data to a dictionary
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)  # Write the data to the file in JSON format

        
    
    
    def add_client(self, name : str, first_name : str ,email : str) -> None :
        """Add a new client to the model"""
        if name in self.clients_name:
            raise Reservation_app_error(f"Client {name} already exists")
        if email in self.clients_manager.clients:
            raise Reservation_app_error(f"Client {email} already exists")
        new_client = Client(name,first_name,email)
        self.clients_manager.clients[new_client._email] = new_client

    @property
    def clients_name(self) -> list[str]:
        """Get a list of clients name"""
        return [client.name for client in self.clients_manager.clients.values()]
    


    def get_clients_infos(self,email : str) -> str:
        return self.clients_manager.clients[email].to_dictionnary()
    
    
    def get_client_uuid(self, name : str) -> str:
        """Get the uuid of a client by his name"""
        for client in self.clients_manager.clients.values():
            if client.name == name:
                return client.id
        raise Reservation_app_error(f"No client named {name}")
    


    
    def add_room(self, name : str, type : str) -> None:
        """Add a new room to the model"""
        if self.rooms_manager.is_a_room(name):
            raise Reservation_app_error(f"Room {name} already exists")
        new_room = Room(name,type)
        self.rooms_manager.add_room(new_room)


    def get_room_available_time_interval(self, room : Room, time_interval : timedelta) -> list:
        """Show all the available time interval for a room"""
        pass

    def get_rooms_available(self)->list[Room]:
        """Give a list of all the available room for a time interval"""
        pass

    @property
    def rooms_name(self) -> list[str]:
        """Get a list of rooms name"""
        return [room.name for room in self._rooms.values()]

    def add_reservation(self, room : str, time_interval : TimeInterval, client_email : str) -> Reservation:
        """Create a new reservation for a room"""
        if not self.rooms_manager.is_a_room(room):
            raise Reservation_app_error(f"Room {room} does not exist")
        
        if client_email not in self.clients_manager.clients:
            raise Reservation_app_error(f"Client {client_email} does not exist")
        
        if not self.rooms_manager.rooms[room].is_available(time_interval):
            raise Reservation_app_error(f"Room {room} is not available for the time interval {time_interval}")
        
        if time_interval.start_time < datetime.today():
            raise Reservation_app_error(f"The start of the reservation has already passed")
        
        new_reservation = self.rooms_manager.rooms[room].create_reservations(time_interval,client_email)
        self.reservations_manager.add_reservations(new_reservation)
        


    




if __name__ == "__main__":



    
    controller = Controller()
    controller.add_client("Mael","Legoff", "mael@uha.fr")
    controller.add_client("Lou","Lemarechal" ,"lou@uha.fr")
    controller.add_client("Paul", "tin","paul@gmail.com")
    controller.add_room("Room1", "Conference")
    controller.add_room("Room2", "Meeting")
    mael_uuid = controller.get_client_uuid("Mael")
    mael_uuid = controller.get_client_uuid("Mael")
    controller.add_reservation("Room1", TimeInterval(date(2026, 10, 1), time(12,30), timedelta(hours=1,minutes=10)), "mael@uha.fr")
    
    controller.save_data("./data/test.json")
    controller2 = Controller()
    controller2.load_data("./data/test.json")
    print(controller2.data_to_dictionnary())
 

