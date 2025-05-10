import uuid

class Client():
    def __init__(self,name : str, first_name : str, email : str) -> None:
        self.name = name
        self.first_name = first_name
        self._email = email # ajouter un property pour afficher une erreur si l’email n’est pas de la forme ____@___.__
        self.id = str(uuid.uuid4())


    def __str__(self):
        return f"{{name : {self.name}, first name : {self.first_name}, email : {self._email}, id : {self.id}}}"
        

    def to_dictionnary(self) -> dict:
        return {
            "name": self.name,
            "first_name": self.first_name,
            "email": self._email,
            "uuid": self.id
        }
