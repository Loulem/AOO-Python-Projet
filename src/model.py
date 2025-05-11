from __future__ import annotations # if some class use type defined later 

from client import *
from reservation import *
from room import *
import json
class Reservation_app_error(Exception):
    """Base class for all exceptions raised by the reservation app"""
    pass


class Controller():
    def __init__(self):
        self._clients : dict[str,Client] = {}
        self._rooms : dict[str,Room] = {}
        self._reservations : dict[str,Reservation] = {}

    def load_data(self, file :str ) -> None:
        """Load the data from a json file """
        #TODO:try to load data with alternative constructors in clients rooms and reservations
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Load clients
            for client_id, client_data in data["clients"].items():
                client = Client(client_data["name"], client_data["first_name"], client_data["email"])
                client.id = client_id   # Set the UUID from the loaded data 
                self._clients[client_id] = client

            # Load rooms
            for room_name, room_data in data["rooms"].items():
                room = Room(room_data["name"], room_data["type"])
                self._rooms[room_name] = room
                # Load reservations for each room
                for reservation_data in room_data["reservations"]:
                    reservation = Reservation(reservation_data["name"], 
                                              TimeInterval(
                                                  date.fromisoformat(reservation_data["timeInterval"]["start_day"]),
                                                  time.fromisoformat(reservation_data["timeInterval"]["start_hour"]),
                                                  timedelta(hours = int(reservation_data["timeInterval"]["hours"]), minutes = int(reservation_data["timeInterval"]["minutes"]))
                                              ),
                                              reservation_data["client_id"]
                                          )
                    reservation.id = reservation_data["id"]  # Set the UUID from the loaded data
                    room._reservations.append(reservation) # add the reservation to the room
                    self._reservations[reservation.id] = reservation # add the reservation to the controller
            

    def data_to_dictionnary(self) -> dict [str,dict[str,dict]]:
        """Return the data in a dictionnary format"""
        clients = {client_id: client_data.to_dictionnary() for client_id, client_data in self._clients.items()}
        rooms = {room_name: room_data.to_dictionnary() for room_name, room_data in self._rooms.items()}
        return  {
            "clients" : clients,
            "rooms" : rooms,
        }

    def save_data(self, file ) -> None:
        """Save the data to a json file"""
        data = self.data_to_dictionnary()  # Convert all data to a dictionary
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)  # Write the data to the file in JSON format

        
    
    
    def add_client(self, name : str, first_name : str ,email : str) -> None :
        """Add a new client to the model"""
        if name in self.clients_name:
            raise Reservation_app_error(f"Client {name} already exists")
        new_client = Client(name,first_name,email)
        self._clients[new_client.id] = new_client

    @property
    def clients_name(self) -> list[str]:
        """Get a list of clients name"""
        return [client.name for client in self._clients.values()]
    


    def get_clients_infos(self,name : str)->str:
        clients_infos = []
        for client in self._clients.values():
            if client.name == name:
                clients_infos.append(client.to_dictionnary())
        if len(clients_infos) == 0:
            raise Reservation_app_error(f"No client named {name}")
        return clients_infos
        
    
    def get_client_uuid(self, name : str) -> str:
        """Get the uuid of a client by his name"""
        for client in self._clients.values():
            if client.name == name:
                return client.id
        raise Reservation_app_error(f"No client named {name}")
    


    
    def add_room(self, name : str, type : str) -> None:
        """Add a new room to the model"""
        if name in self.rooms_name:
            raise Reservation_app_error(f"Room {name} already exists")
        new_room = Room(name,type)
        self._rooms[name] = new_room
        pass

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

    def add_reservation(self, room : str, time_interval : TimeInterval, client_id : str) -> Reservation:
        """Create a new reservation for a room"""
        if room not in self._rooms:
            raise Reservation_app_error(f"Room {room} does not exist")
        if client_id not in self._clients:
            raise Reservation_app_error(f"Client {client_id} does not exist")
        if not self._rooms[room].is_available(time_interval):
            raise Reservation_app_error(f"Room {room} is not available for the time interval {time_interval}")
        if time_interval.start_time < datetime.today():
            raise Reservation_app_error(f"The start of the reservation is in the past")
        new_reservation = self._rooms[room].create_reservations(time_interval,client_id)
        self._reservations[new_reservation.id] = new_reservation
        


    




if __name__ == "__main__":



    
    controller = Controller()
    controller.add_client("Mael","Legoff", "mael@uha.fr")
    controller.add_client("Lou","Lemarechal" ,"lou@uha.fr")
    controller.add_client("Paul", "tin","paul@gmail.com")
    controller.add_room("Room1", "Conference")
    controller.add_room("Room2", "Meeting")
    mael_uuid = controller.get_client_uuid("Mael")
    mael_uuid = controller.get_client_uuid("Mael")
    controller.add_reservation("Room1", TimeInterval(date(2023, 10, 1), time(12,30), timedelta(hours=1,minutes=10)), controller._clients[mael_uuid].id)
    controller.save_data("./src/data/test.json")
    controller2 = Controller()
    controller2.load_data("./src/data/test.json")






