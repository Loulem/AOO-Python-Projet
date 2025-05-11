from time_Interval import *
import uuid




class Reservation():
    def __init__(self, room : str, time_interval : TimeInterval, client_id : uuid.UUID) -> None:
        self.id = str(uuid.uuid4())
        self.room = room
        self.time_interval = time_interval
        self.client_id = client_id 
        
    def overlap_with(self, time_interval_start: datetime, time_interval_end: datetime) -> bool:
        """Check if the reservation conflicts with the given time interval"""
        reservation_start = self.time_interval.start_time
        reservation_end = self.time_interval.end_time
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

