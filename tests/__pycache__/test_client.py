from model import Client


def test_Client_str():
    client = Client("Mael", "mael@uha.fr")
    # Directly compare the string representation
    assert str(client) == f"{{name : Mael; email : mael@uha.fr, id : {client.id}}}"


def test_Client_to_dictionnary():
    client = Client("Mael", "mael@uha.fr")
    client_dict = client.to_dictionnary()
    assert client_dict == {
        "name": "Mael",
        "email": "mael@uha.fr",
        "uuid": str(client.id),  # Fix key to match the `to_dictionnary` method
    }
    assert type(client_dict["uuid"]) == str
    assert type(client_dict["name"]) == str
    assert type(client_dict["email"]) == str
    assert client_dict["name"] == "Mael"
    assert client_dict["email"] == "mael@uha.fr"
    assert client_dict["uuid"] == str(client.id)


