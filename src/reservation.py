from datetime import date , timedelta , datetime, time
import uuid

class TimeSlot():
    def __init__(self, start_day : datetime, start_hour : time , duration : timedelta) -> None:
        self.start_day = start_day
        self.start_hour = start_hour
        self.duration = duration
        
        
    def __str__(self) -> str:
        return f"{{start_time : {self.start_time}; end_time : {self.end_time}}}"
    
    def to_dictionnary(self) -> dict:
        return {
            "start_day": self.start_day.isoformat(),
            "start_hour": self.start_hour.isoformat(),
            "hours": str(self.duration).split(":")[0],
            "minutes": str(self.duration).split(":")[1],
        }
    



class Reservation():
    def __init__(self, room : str, timeSlot : TimeSlot, client_id : uuid.UUID) -> None:
        self.id = str(uuid.uuid4())
        self.room = room
        self.timeSlot = timeSlot
        self.client_id = client_id # uuid of the client who made the reservation
        
    
    def to_dictionnary(self) -> dict:
        return {
            "id": self.id,
            "name": self.room,
            "client_id": self.client_id,
            "timeSlot": self.timeSlot.to_dictionnary(),
        }
    

