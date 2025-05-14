from __future__ import annotations
from reservationApp.model.reservation import *

class RoomsManager():
    def __init__(self):
        self.rooms : dict[str,Room] = {}

    
    def add_rooms_from_json(self, rooms_data : dict[str,dict[str,str]], reservations_manager : ReservationsManager) :
        """Create a room manager from a json data"""
        for room_name, room_data in rooms_data.items():
            room = Room.from_json(room_data, reservations_manager)
            self.rooms[room_name] = room

    def add_room(self, room : Room):
        self.rooms[room.name] = room

    def is_a_room(self,name : str)-> None:
        return name in self.rooms.keys() 

    def to_dictionnary(self):
        return {room_name: room_data.to_dictionnary() for room_name, room_data in self.rooms.items()} 
            
    

class Room():
    def __init__(self,name : str ,type : str):
        self.name = name
        self.type = type
        self._reservations : dict[str,Reservation] = {} # contient les objets réservations attribuer à la salle
        #TODO : ajouter un attribut pour le nombre de places de la salle
        
    @classmethod
    def from_json(cls, json_data:dict, reservations_manager : ReservationsManager)-> Room:
        """Create a room from a json data"""
        name = json_data["name"]
        type = json_data["type"]
        room = cls(name, type)
        room._reservations = reservations_manager.add_reservations_from_json(json_data["reservations"])
        return room

    def create_reservations(self, time_interval : TimeInterval, client_id : str ) -> Reservation:
        """Add a reservation to the room"""
        new_reservation = Reservation( self.name, time_interval, client_id)
        self._reservations[new_reservation.id] = new_reservation
        return new_reservation
        

    def is_available(self,time_interval:TimeInterval) -> bool:
        """Return true if the room is available during the time interval"""
        for reservation in self._reservations.values():
           if reservation.overlap_with(time_interval.start_time, time_interval.end_time):
                return False
        return True

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "reservations": [reservation.to_dictionnary() for reservation in self._reservations.values()] 
            
            
        }
    def __str__(self) -> str:
        return f"{{name : {self.name}, type : {self.type}}}"



