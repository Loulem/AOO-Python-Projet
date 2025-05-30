from __future__ import annotations
from reservationApp.model.reservation.reservation import *
class RoomError(Exception):
    pass

class RoomsManager():
    def __init__(self):
        self.rooms : dict[str,Room] = {}

    def get_available_rooms(self, time_interval: TimeInterval) -> list[Room]:
        """Return a list of available rooms for a given time interval"""
        available_rooms = []
        for room in self.rooms.values():
            if room.is_available(time_interval):
                available_rooms.append(room)
        return available_rooms
    
    def add_rooms_from_json(self, rooms_data : dict[str,dict[str,str]], reservations_manager : ReservationsManager) :
        """Create a room manager from a json data"""
        for room_name, room_data in rooms_data.items():
            room = Room.from_json(room_data, reservations_manager)
            self.rooms[room_name] = room

    def add_room(self, name : str, type : str, capacity : int):
        if self.is_a_room(name):
            raise RoomError(f"Room {name} already exists")
        new_room = Room(name,type,capacity)
        self.rooms[name] = new_room


    def is_a_room(self,name : str)-> bool:
        return name in self.rooms.keys() 

    def to_dictionnary(self):
        return {room_name: room_data.to_dictionnary() for room_name, room_data in self.rooms.items()} 
            
    @property
    def rooms_name(self) -> list[str]:
        """Get a list of rooms name"""
        return [room.name for room in self.rooms.values()]
    
    @property
    def rooms_list(self) -> list[Room]:
        """Get a list of rooms"""
        return list(self.rooms.values())


class Room():
    def __init__(self,name : str ,type : str, capacity):
        self.name = name
        self.type = type
        self._reservations : dict[str,Reservation] = {} 
        self.capacity = capacity
        
    @classmethod
    def from_json(cls, json_data:dict, reservations_manager : ReservationsManager)-> Room:
        """Create a room from a json data"""
        name = json_data["name"]
        type = json_data["type"]
        capacity = json_data["capacity"]
        room = cls(name, type,capacity)
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
           if reservation.overlap_with(time_interval.start_datetime, time_interval.end_datetime):
                return False
        return True

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "capacity": self.capacity,
            "reservations": [reservation.to_dictionnary() for reservation in self._reservations.values()] 
            
            
        }
    def __str__(self) -> str:
        return f"{{name : {self.name}, type : {self.type}, capacity : {self.capacity}}}"



