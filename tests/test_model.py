from model import *
import pytest
def test_is_saved_uuid_a_string():
    controller = Model()
    controller.add_client("Mael", "Legoff","mael@uha.fr")
    assert type( list( list( controller.data_to_dictionnary().values() )[0].keys() ) [0]) == str  # Check if the uuid is a string


def test_if_saved_are_correctly_loaded():
    

    controller = Model()
    controller.add_client("Mael","Legoff", "mael@uha.fr")
    controller.add_client("Lou","Lemarechal" ,"lou@uha.fr")
    controller.add_client("Paul", "tin","paul@gmail.com")
    controller.add_room("Room1", "Conference")
    controller.add_room("Room2", "Meeting")
    mael_uuid = controller.get_client_uuid("Mael")
    mael_uuid = controller.get_client_uuid("Mael")
    controller.add_reservation("Room1", TimeInterval(date(2023, 10, 1), time(12,30), timedelta(hours=1,minutes=10)), controller._clients[mael_uuid].id)
    controller.save_data("./src/data/test.json")
    controller2 = Model()
    controller2.load_data("./src/data/test.json")
    assert controller2.data_to_dictionnary() == controller.data_to_dictionnary()





def test_if_controller_Reservations_is_same_as_room_Reservation():
    controller = Model()
    controller.add_client("Mael", "Legoff", "mael@uha.fr")
    controller.add_room("Room1", "Conference")
    controller.add_reservation("Room1", TimeInterval(date(2023, 10, 1), time(12, 30), timedelta(hours=1, minutes=10)), list(controller._clients.values())[0].id)
    assert list(controller._rooms["Room1"]._reservations)[0] == list(controller._reservations.values())[0]

def test_add_client_error():
    controller = Model()
    controller.add_client("Mael", "Legoff", "Mael@uha.fr")
    with pytest.raises(Reservation_app_error):
        controller.add_client("Mael", "Legoff", "et@uha.fr")
