from reservationApp.model.reservation import *


class Room():
    def __init__(self,name : str ,type : str):
        self.name = name
        self.type = type
        self._reservations : list[Reservation] = [] # contient les objets réservations attribuer à la salle
        #TODO : ajouter un attribut pour le nombre de places de la salle
        
        
    def create_reservations(self, time_interval : TimeInterval, client_id : str ) -> Reservation:
        """Add a reservation to the room"""
        new_reservation = Reservation( self.name, time_interval, client_id)
        self._reservations.append(new_reservation)
        return new_reservation
        

    def is_available(self,time_interval:TimeInterval) -> bool:
        """Return true if the room is available during the time interval"""
        for reservation in self._reservations:
           if reservation.overlap_with(time_interval.start_time, time_interval.end_time):
                return False
        return True

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "type": self.type,
            "reservations": [reservation.to_dictionnary() for reservation in self._reservations] 
            
            
        }
    def __str__(self) -> str:
        return f"{{name : {self.name}, type : {self.type}}}"


