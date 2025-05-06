import uuid 
from __future__ import annotations # if some class use type defined later 

class Client():
    def __init__(self,name : str, email : str) -> None:
        self.name = name
        self._email = email # ajouter un property pour afficher une erreur si l’email n’est pas de la forme ____@___.__
        self.uuid = uuid.uuid4()



class Room():
    def __init__(self,name):
        self.name = name

    def is_available(self,timestamp) -> bool:
        """Return true if the room is available for the timestamp"""
        pass


class Standard(Room):
    def __init__(self, name):
        super().__init__(name)
        self.size = 4

class Conference(Room):
    def __init__(self, name):
        super().__init__(name)
        self.size = 10

class Informatique(Room):
    def __init__(self, name):
        super().__init__(name)
        self.size = 4

    
    


class Model():
    def __init__(self):
        self._clients : dict[Client] = []
        self._rooms : dict[Room] = []

    def load_data(self, file ):
        """Load the data from a json file """
        pass

    def save_data(self,file):
        """Save the data to a json file"""
        pass

    def get_rooms_available(self)->list[Room]:
        """Give a list of all the available room for a timestamp"""


