from reservationApp.model.client.client import *
from reservationApp.model.reservation.reservation import *
from reservationApp.model.room.room import *
import json


class Model():
    def __init__(self, rooms_manager : RoomsManager, reservations_manager : ReservationsManager, clients_manager : ClientManager):
        self.rooms_manager = rooms_manager
        self.reservations_manager = reservations_manager
        self.clients_manager = clients_manager
    
    def load_data(self, file :str ) -> None: # to model
        """Load the data from a json file """
        #TODO:try to load data with alternative constructors in clients rooms and reservations
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            self.rooms_manager.add_rooms_from_json(data["rooms"], self.reservations_manager)
            self.clients_manager.add_clients_from_json(data["clients"])
            
    def data_to_dictionnary(self) -> dict [str,dict[str,dict]]: # to model
        """Return the data in a dictionnary format"""
        return  {
            "clients" : self.clients_manager.to_dictionnary(),
            "rooms" : self.rooms_manager.to_dictionnary(),
        }

    def save_data(self, file ) -> None: # to model
        """Save the data to a json file"""
        data = self.data_to_dictionnary()  # Convert all data to a dictionary
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)  # Write the data to the file in JSON format
