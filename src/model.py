from __future__ import annotations # if some class use type defined later 

from client import *
from reservation import *
from room import *
import json

"""class datetime.timedelta
A duration expressing the difference between two datetime or date instances to microsecond resolution."""









class Controller():
    def __init__(self):
        self._clients : dict[str,Client] = {}
        self._rooms : dict[str,Room] = {}
        self._reservations : dict[str,Reservation] = {}


    def load_data(self, file :str ) -> None:
        """Load the data from a json file """
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            # Load clients
            for client_id, client_data in data["clients"].items():
                client = Client(client_data["name"], client_data["first_name"], client_data["email"])
                client.id = client_id   # Set the UUID from the loaded data 
                self._clients[client_id] = client

            # Load rooms
            for room_name, room_data in data["rooms"].items():
                room = Room(room_data["name"], room_data["type"])
                self._rooms[room_name] = room
                # Load reservations for each room
                for reservation_data in room_data["reservations"]:
                    reservation = Reservation(reservation_data["name"], 
                                              TimeSlot(
                                                  date.fromisoformat(reservation_data["timeSlot"]["start_day"]),
                                                  time.fromisoformat(reservation_data["timeSlot"]["start_hour"]),
                                                  timedelta(hours = int(reservation_data["timeSlot"]["hours"]), minutes = int(reservation_data["timeSlot"]["minutes"]))
                                              ),
                                              reservation_data["client_id"]
                                          )
                    reservation.id = reservation_data["id"]  # Set the UUID from the loaded data
                    room._reservations.append(reservation)
                    self._reservations[reservation.id] = reservation
            # Load reservations
            
        
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

        
    
    
    def add_client(self, name : str, first_name : str ,email : str) -> None :
        """Add a new client to the model"""
        new_client = Client(name,first_name,email)
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
        


    




if __name__ == "__main__":



    
    controller = Controller()
    controller.add_client("Mael","Legoff", "mael@uha.fr")
    controller.add_client("Lou","Lemarechal" ,"lou@uha.fr")
    controller.add_client("Paul", "tin","paul@gmail.com")
    controller.add_rooms("Room1", "Conference")
    controller.add_rooms("Room2", "Meeting")
    mael_uuid = controller.get_client_uuid("Mael")
    mael_uuid = controller.get_client_uuid("Mael")
    controller.add_reservations("Room1", TimeSlot(date(2023, 10, 1), time(12,30), timedelta(hours=1,minutes=10)), controller._clients[mael_uuid].id)
    controller.save_data("./src/data/test.json")
    controller2 = Controller()
    controller2.load_data("./src/data/test.json")
    #print(controller2.data_to_dictionnary())
    #print( controller.data_to_dictionnary())





    # # Example usage
    # # Create a controller instance and add some clients
    # controller = Controller()
    # controller.add_client("Mael","Legoff", "mael@uha.fr")
    # controller.add_client("Lou","Lemarechal" ,"lou@uha.fr")
    # controller.add_client("Paul", "tin","paul@gmail.com")
    # controller.add_rooms("Room1", "Conference")
    # controller.add_rooms("Room2", "Meeting")
    # mael_uuid = controller.get_client_uuid("Mael")
    # controller.add_reservations("Room1", TimeSlot(date(2023, 10, 1), time(12,30), timedelta(hours=1,minutes=10)), controller._clients[mael_uuid].id)
    

    # print(controller.data_to_dictionnary())
    # controller.save_data("./src/data/test.json")
    # controller.load_data("./src/data/test.json")



