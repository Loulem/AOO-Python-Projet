import uuid

import re


class ClientError(Exception):
    """Base class for all exceptions raised by the client"""

    pass


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


