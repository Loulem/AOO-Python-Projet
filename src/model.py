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
        self.uuid = uuid.uuid4()

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "email": self.email,
            "uuid": str(self.uuid)
        }

class Room():
    def __init__(self,name : str ,type : str):
        self.name = name
        self.type = type
        self._reservations : list[Reservation] = []

    def is_available(self,timestamp) -> bool:
        """Return true if the room is available for the timestamp"""
        pass

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            
        }



class Reservation():
    def __init__(self, room : str, timeSlot : timedelta):
        self.room = room
        self.timeSlot = timeSlot
    
    def to_dictionnary(self) -> dict:
        return {
            "name": self.room,
            "timeSlot": self.timeSlot.__str__,
        }

    

class Controller():
    def __init__(self):
        self._clients : list[Client] = []
        self._rooms : list[Room] = []
        self._reservations : list[Reservation] = []


    def load_data(self, file ) -> None:
        """Load the data from a json file """
        try:
            with open(self.db_file, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"clients": [], "rooms": [], "reservations": []}  # Structure par défaut

    def save_data(self, file ) -> None:
        """Save the data to a json file"""
        clients = []
        rooms = []
        reservations = []
        for client in self._clients:
            clients.append(client.to_dictionnary())

        for room in self._rooms:
            rooms.append(room.to_dictionnary())
            
        for reservation in self._reservations:
            reservations.append(reservation.to_dictionnary())
            
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
        self._clients.append(new_client)
    
    def add_rooms(self, name : str, type : str) -> None:
        """Add a new room to the model"""
        pass

    def get_room_available_time_slot(self, room : Room, timeSlot : timedelta) -> list:
        """Show all the available time slot for a room"""
        pass

    



