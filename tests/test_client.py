from model import Client, Room, Reservation, Controller



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
        "uuid": str(client.id),
    }



def test_Room_to_dictionnary():
    room = Room("Room1", "Conference")
    room_dict = room.to_dictionnary()
    assert room_dict == {
        "name": "Room1",
        "type": "Conference",
        "reservations": [],
    }




def test_is_saved_uuid_a_string():
    controller = Controller()
    controller.add_client("Mael", "mael@uha.fr")
    assert type( list( list( controller.data_to_dictionnary().values() )[0].keys() ) [0]) == str  # Check if the uuid is a string
