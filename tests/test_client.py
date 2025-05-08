from model import Client, Room, Reservation



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


    def test_Room_to_dictionnary():
        room = Room("Room1", "Conference", "1234-uuid")
        room_dict = room.to_dictionnary()
        assert room_dict == {
            "name": "Room1",
            "type": "Conference",
            "reservations": [],
        }


