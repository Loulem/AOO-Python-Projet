from __future__ import annotations
from datetime import datetime, timedelta, date, time

class TimeInterval():
    def __init__(self, start_day : datetime, start_hour : time , duration : timedelta) -> None:
        #TODO : change the class to store start_day_time and start_end_time
        """Initialize the time interval with a start day, start hour and duration"""
        self.start_day = start_day
        self.start_hour = start_hour
        self.duration = duration

    
    @classmethod
    def from_json(cls, json_data:dict) -> TimeInterval:
        """Create a time interval from a json data"""
        start_day = date.fromisoformat(json_data["start_day"])
        start_hour = time.fromisoformat(json_data["start_hour"])
        duration = timedelta(hours = int(json_data["hours"]), minutes = int(json_data["minutes"]))
        return cls(start_day,start_hour,duration)                                          
        
    def __str__(self) -> str:
        return f"{{start_time : {self.start_time}; end_time : {self.end_time}}}"
    
    def to_dictionnary(self) -> dict:
        """Return the time interval in a dictionnary format"""
        return {
            "start_day": self.start_day.isoformat(),
            "start_hour": self.start_hour.isoformat(),
            "hours": str(self.duration).split(":")[0],
            "minutes": str(self.duration).split(":")[1],
        }

    @property
    def start_time(self) -> datetime:
        """Return the start time of the time interval"""
        return datetime.combine(self.start_day, self.start_hour)
    
    @property
    def end_time(self) -> datetime:
        """Return the end time of the time interval"""
        return self.start_time + self.duration
