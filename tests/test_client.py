from reservationApp.model.client import *
from reservationApp.controller import *
import pytest

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

def test_Client_email_error():
    with pytest.raises(ClientError):
        client = Client("Mael", "Legoff", "Mael@uhafr")
    with pytest.raises(ClientError):
        client = Client("Mael", "Legoff", "Mael@uha.r")
    with pytest.raises(ClientError):
        client = Client("Mael", "Legoff", "Maeluha.fr")