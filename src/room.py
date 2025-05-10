from reservation import *


class Room():
    def __init__(self,name : str ,type : str):
        self.name = name
        self.type = type
        self._reservations : list[Reservation] = [] # contient les objets réservations attribuer à la salle
        
        
    def create_reservations(self, timeSlot : TimeSlot, client_id : str ) -> Reservation:
        """Add a reservation to the room"""
        new_reservation = Reservation( self.name, timeSlot, client_id)
        self._reservations.append(new_reservation)
        return new_reservation
        

    def is_available(self,timestamp:timedelta) -> bool:
        """Return true if the room is available for the timestamp"""
        pass

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "reservations": [reservation.to_dictionnary() for reservation in self._reservations] 
            
            
        }


