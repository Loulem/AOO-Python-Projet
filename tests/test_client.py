from client import *



def test_Client_str():
    client = Client("Mael", "Legoff", "mael@uha.fr")
    assert str(client) == f"{{name : Mael, first name : Legoff, email : mael@uha.fr, id : {client.id}}}"


def test_Client_to_dictionnary():
    client = Client("Mael","Legoff", "mael@uha.fr")
    client_dict = client.to_dictionnary()
    assert client_dict == {
        "name": "Mael",
        "first_name": "Legoff",
        "email": "mael@uha.fr",
        "uuid": str(client.id),
    }




