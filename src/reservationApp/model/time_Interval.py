from __future__ import annotations
from datetime import datetime, timedelta, date, time

class TimeInterval():
    def __init__(self, start_datetime : datetime , end_datetime : datetime) -> None:
        """Initialize the time interval with a start day, start hour and duration"""
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
    
    @classmethod
    def from_json(cls, json_data:dict) -> TimeInterval:
        """Create a time interval from a json data"""
        start_datetime = datetime.fromisoformat(json_data["start_datetime"])
        end_datetime = datetime.fromisoformat(json_data["end_datetime"])
        return cls(start_datetime, end_datetime)

    def __str__(self) -> str:
        return f"{{start_time : {self.start_datetime}; end_time : {self.end_datetime}}}"
    
    def to_dictionnary(self) -> dict:
        """Return the time interval in a dictionnary format"""
        return {
            "start_datetime": self.start_datetime.isoformat(),
            "end_datetime": self.end_datetime.isoformat(),
        }
    
    @property
    def end_datetime(self):
        return self._end_datetime
    
    @end_datetime.setter
    def end_datetime(self, end_datetime : datetime ):
        """Set the end datetime of the time interval"""
        
        if end_datetime <= self.start_datetime :

            raise ValueError("End of the time Interval is before the start")
        self._end_datetime = end_datetime

        