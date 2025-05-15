from __future__ import annotations
from reservationApp.model.time_Interval import *
import uuid

class ReservationsManager():
    def __init__(self)-> None:
        self.reservations : dict[str,Reservation] = {} # contient les objets réservations attribuer à la salle
        
    def add_reservations_from_json(self, reservations_data : list[dict[str,str]])-> dict[str,Reservation]:
        """Add reservations from json data"""
        room_reservations : dict[str, Reservation] = {}
        for reservation_data in reservations_data:
            reservation = Reservation.from_json(reservation_data)
            self.reservations[reservation.id] = reservation
            room_reservations[reservation.id] = reservation
        return room_reservations
    
    def add_reservations(self, new_reservation : Reservation):
        self.reservations[new_reservation.id] = new_reservation


class Reservation():
    def __init__(self, room : str, time_interval : TimeInterval, client_id : str) -> None:
        self.id = str(uuid.uuid4())
        self.room = room
        self.time_interval = time_interval
        self.client_id = client_id 
    
    @classmethod
    def from_json(cls, json_data: dict) -> Reservation:
        """Create a reservation from a json data"""
        room = json_data["name"]
        client_id = json_data["client_id"]
        time_interval = TimeInterval.from_json(json_data["timeInterval"])
        reservation = cls(room, time_interval, client_id)
        reservation.id = json_data["id"]
        return reservation
    
    def overlap_with(self, time_interval_start: datetime, time_interval_end: datetime) -> bool:
        """Check if the reservation conflicts with the given time interval"""
        reservation_start = self.time_interval.start_datetime
        reservation_end = self.time_interval.end_datetime
        if (time_interval_start  >= reservation_end):
            return False
        if (time_interval_end <= reservation_start):
            return False
    
        return True
    

    def to_dictionnary(self) -> dict:
        """Return the reservation in a dictionnary format"""
        return {
            "id": self.id,
            "name": self.room,
            "client_id": self.client_id,
            "timeInterval": self.time_interval.to_dictionnary(),
        }
    def __str__(self) -> str:
        return f"{{id : {self.id}, room : {self.room}, client_id : {self.client_id}, time_interval : {self.time_interval}}}"

