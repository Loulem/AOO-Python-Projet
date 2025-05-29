from __future__ import annotations
import uuid
import re


class ClientError(Exception):
    """Base class for all exceptions raised by the client"""

    pass

class ClientManager():
    def __init__(self):
        self.clients : dict[str,Client] = {} 

    def add_clients_from_json(self, json_data : dict[str,dict[str,str]]) -> None:
        
        for client_email , client_data in json_data.items():
            self.clients[client_email] = Client.from_json(client_data)

    def add_client(self, name : str, first_name : str ,email : str) -> None :
        if name in self.clients_name:
            raise ClientError(f"Client {name} already exists")
        if email in self.clients:
            raise ClientError(f"There is already a client with the email : {email}")
        new_client = Client(name,first_name,email)
        self.clients[new_client._email] = new_client
        
    def get_clients_infos(self,email : str) -> dict:
        return self.clients[email].to_dictionnary()
    @property
    def clients_list(self) -> list[Client]:
        """Get a list of clients"""
        return list(self.clients.values())
    @property
    def clients_name(self) -> list[str]:
        """Get a list of clients name"""
        return [client.name for client in self.clients.values()]
    
    @property
    def clients_email(self) -> list[str]:
        """Get a list of clients email"""
        return list(self.clients.keys())

    def to_dictionnary(self):
        return {client_id: client_data.to_dictionnary() for client_id, client_data in self.clients.items()}

    def is_a_client(self,email : str) -> bool:
        """Return true if it is an already register client"""
        return email in self.clients_email

class Client():
    def __init__(self,name : str, first_name : str, email : str) -> None:
        self.name = name
        self.first_name = first_name
        self.email = email  # ajouter un property pour afficher une erreur si l’email n’est pas de la forme ____@___.__
        self.id = str(uuid.uuid4())
        self._reservertions_id : list[str] = [] #TODO: ajouter les reservations id quand on load et quand on les créer 

    @property
    def email(self) -> str:
        """Return the email of the client"""
        return self._email
    
    @email.setter
    def email(self, email : str) -> None:
        """Set the email of the client"""
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if not(re.fullmatch(regex, email)):
            raise ClientError("Email must be in the format ____@___.__")
        self._email = email

    def __str__(self):
        return f"{{name : {self.name}, first name : {self.first_name}, email : {self._email}, id : {self.id}}}"
        

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "first_name": self.first_name,
            "email": self._email,
            "uuid": self.id
        }
    @classmethod
    def from_json(cls,json_data : dict[str,str]) -> Client:
        client = cls(json_data["name"],json_data["first_name"],json_data["email"])
        client.id = json_data["uuid"]
        return client


