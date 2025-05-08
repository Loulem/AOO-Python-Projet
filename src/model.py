from __future__ import annotations # if some class use type defined later 
import uuid 
from datetime import date , timedelta 
import json

"""class datetime.timedelta
A duration expressing the difference between two datetime or date instances to microsecond resolution."""


class Client():
    def __init__(self,name : str, email : str) -> None:
        self.name = name
        self._email = email # ajouter un property pour afficher une erreur si l’email n’est pas de la forme ____@___.__
        self.id = uuid.uuid4()


    def __str__(self):
        return f"{{name : {self.name}; email : {self._email}, id : {self.id}}}"
        

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "email": self._email,
            "uuid": str(self.id)
        }

class Room():
    def __init__(self,name : str ,type : str, client_uuid : str):
        self.name = name
        self.type = type
        self._reservations : list[int] = [] # contient les identifiants des réservations attribuer à la salle
        self.client_id = client_uuid
        
    def is_available(self,timestamp:timedelta) -> bool:
        """Return true if the room is available for the timestamp"""
        pass

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "reservations": self._reservations,
            
        }



class Reservation():
    def __init__(self, id : int ,room : str, timeSlot : timedelta):
        self.id = id
        self.room = room
        self.timeSlot = timeSlot
    
    def to_dictionnary(self) -> dict:
        return {
            "id": self.id,
            "name": self.room,
            "timeSlot": self.timeSlot.__str__,
            
        }
    



class Controller():
    def __init__(self):
        self._clients : dict[uuid.UUID,Client] = {}
        self._rooms : dict[str,Room] = {}
        self._reservations : dict[uuid.UUID,Reservation] = {}


    def load_data(self, file ) -> None:
        """Load the data from a json file """
        try:
            with open(self.db_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"clients": [], "rooms": [], "reservations": []}  # Structure par défaut

    def save_data(self, file ) -> None:
        """Save the data to a json file"""
        clients: dict[dict] = {}
        rooms: dict = {}
        reservations: dict = {}
        for client in self._clients:
            clients[client.id] = client.to_dictionnary()

        for room in self._rooms:
            rooms[room.name] = room.to_dictionnary()
            
        for reservation in self._reservations:
            reservations[reservation.id] = reservation.to_dictionnary()
            
        data = {
            "clients" : clients,
            "rooms" : rooms,
            "reservation" : reservations,
        }
        
    def get_rooms_available(self)->list[Room]:
        """Give a list of all the available room for a timestamp"""
        pass
    
    def add_client(self, name : str, email : str) -> None :
        """Add a new client to the model"""
        new_client = Client(name,email)
        self._clients[new_client.id] = new_client
    
    def add_rooms(self, name : str, type : str) -> None:
        """Add a new room to the model"""
        pass

    def get_room_available_time_slot(self, room : Room, timeSlot : timedelta) -> list:
        """Show all the available time slot for a room"""
        pass

    def get_client_infos(self,name : str)->str:
        clients_infos = []
        for client in self._clients.values():
            if client.name == name:
                clients_infos.append(client.__str__())
        return clients_infos


    

    



if __name__ == "__main__":

    client = Client("Mael", "mael@uha.fr")
    print(client.__str__())
    print(type(client.id))
    print(client.to_dictionnary())
    controller = Controller()
    controller.add_client("Mael", "mael@uha.fr")
    print(controller.get_client_infos("Mael"))