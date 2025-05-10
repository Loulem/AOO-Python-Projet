from model import *



def test_Client_str():
    client = Client("Mael", "Legoff", "mael@uha.fr")
    # Directly compare the string representation
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
    controller.add_client("Mael", "Legoff","mael@uha.fr")
    assert type( list( list( controller.data_to_dictionnary().values() )[0].keys() ) [0]) == str  # Check if the uuid is a string


def test_if_saved_are_correctly_loaded():
    

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
    assert controller2.data_to_dictionnary() == controller.data_to_dictionnary()