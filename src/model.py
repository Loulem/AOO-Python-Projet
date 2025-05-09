from __future__ import annotations # if some class use type defined later 
import uuid 
from datetime import date , timedelta 
import json

"""class datetime.timedelta
A duration expressing the difference between two datetime or date instances to microsecond resolution."""


class Client():
    def __init__(self,name : str, email : str) -> None:
        self.name = name
        self._email = email # ajouter un property pour afficher une erreur si l’email n’est pas de la forme ____@___.__
        self.id = str(uuid.uuid4())


    def __str__(self):
        return f"{{name : {self.name}; email : {self._email}, id : {self.id}}}"
        

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "email": self._email,
            "uuid": self.id
        }

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
    




class Controller():
    def __init__(self):
        self._clients : dict[uuid.UUID,Client] = {}
        self._rooms : dict[str,Room] = {}
        self._reservations : dict[uuid.UUID,Reservation] = {}


    def load_data(self, file ) -> None:
        """Load the data from a json file """
        pass

    def data_to_dictionnary(self) -> dict [str,dict[str,dict]]:
        """Return the data in a dictionnary format"""
        rooms: dict[str,Room] = {} # a dictionnary with the name of the room as key and the uuid of the client as value
        clients: dict[str,dict] = {} # a dictionnary with the name of the client as key and the uuid of the client as value
        reservations: dict[str,dict] = {} # a dictionnary with the name of the reservation as key and the uuid of the client as value
        for client in self._clients.values():
            clients[client.id.__str__()] = client.to_dictionnary()
        for room in self._rooms.values():
            rooms[room.name] = room.to_dictionnary()
        # for reservation in self._reservations.values():
        #     reservations[str(reservation.id)] = reservation.to_dictionnary()
 
        return  {
            "clients" : clients,
            "rooms" : rooms,
            #"reservation" : reservations,
        }

    def save_data(self, file ) -> None:
        """Save the data to a json file"""
        data = self.data_to_dictionnary()  # Convert all data to a dictionary
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)  # Write the data to the file in JSON format

        
    
    
    def add_client(self, name : str, email : str) -> None :
        """Add a new client to the model"""
        new_client = Client(name,email)
        self._clients[new_client.id] = new_client
    

    def get_clients_infos(self,name : str)->str:
        clients_infos = []
        for client in self._clients.values():
            if client.name == name:
                clients_infos.append(client.to_dictionnary())
        if len(clients_infos) == 0:
            raise ValueError(f"No client named {name}")
        return clients_infos
        
    
    def get_client_uuid(self, name : str) -> str:
        """Get the uuid of a client by his name"""
        for client in self._clients.values():
            if client.name == name:
                return client.id
        raise ValueError(f"No client named {name}")
    
    def add_rooms(self, name : str, type : str) -> None:
        """Add a new room to the model"""
        new_room = Room(name,type)
        self._rooms[name] = new_room
        pass

    def get_room_available_time_slot(self, room : Room, timeSlot : timedelta) -> list:
        """Show all the available time slot for a room"""
        pass

    def get_rooms_available(self)->list[Room]:
        """Give a list of all the available room for a timestamp"""
        pass


    def add_reservations(self, room : str, timeSlot : TimeSlot, client_id : str) -> Reservation:
        """Create a new reservation for a room"""
        new_reservation = self._rooms[room].create_reservations(timeSlot,client_id)
        self._reservations[new_reservation.id] = new_reservation
        


    
class TimeSlot():
    def __init__(self, start_time : date, end_time : date) -> None:
        self.start_time = start_time
        self.end_time = end_time
        
    def __str__(self) -> str:
        return f"{{start_time : {self.start_time}; end_time : {self.end_time}}}"
    
    def to_dictionnary(self) -> dict:
        return {
            "start_time": str(self.start_time),
            "end_time": str(self.end_time)
        }
    



if __name__ == "__main__":

    # Example usage
    # Create a controller instance and add some clients
    controller = Controller()
    controller.add_client("Mael", "mael@uha.fr")
    controller.add_client("Lou", "lou@uha.fr")
    controller.add_client("Paul", "paul@gmail.com")
    controller.add_rooms("Room1", "Conference")
    controller.add_rooms("Room2", "Meeting")
    mael_uuid = controller.get_client_uuid("Mael")
    controller.add_reservations("Room1", TimeSlot(date(2023, 10, 1), date(2023, 10, 2)), controller._clients[mael_uuid].id)
    
    print(controller.data_to_dictionnary())
    controller.save_data("test.json")
