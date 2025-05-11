from model import *
import pytest
def test_is_saved_uuid_a_string():
    controller = Controller()
    controller.add_client("Mael", "Legoff","mael@uha.fr")
    assert type( list( list( controller.data_to_dictionnary().values() )[0].keys() ) [0]) == str  # Check if the uuid is a string


def test_if_saved_are_correctly_loaded():
    

    controller = Controller()
    controller.add_client("Mael","Legoff", "mael@uha.fr")
    controller.add_client("Lou","Lemarechal" ,"lou@uha.fr")
    controller.add_client("Paul", "tin","paul@gmail.com")
    controller.add_room("Room1", "Conference")
    controller.add_room("Room2", "Meeting")
    mael_uuid = controller.get_client_uuid("Mael")
    mael_uuid = controller.get_client_uuid("Mael")
    tomorow = date.today() + timedelta(days=1)
    controller.add_reservation("Room1", TimeInterval(tomorow, time(12,30), timedelta(hours=1,minutes=10)), controller._clients[mael_uuid].id)
    controller.save_data("./src/data/test.json")
    controller2 = Controller()
    controller2.load_data("./src/data/test.json")
    assert controller2.data_to_dictionnary() == controller.data_to_dictionnary()





def test_if_controller_Reservations_is_same_as_room_Reservation():
    controller = Controller()
    controller.add_client("Mael", "Legoff", "mael@uha.fr")
    controller.add_room("Room1", "Conference")
    tomorow = date.today() + timedelta(days=1)
    controller.add_reservation("Room1", TimeInterval(tomorow, time(12, 30), timedelta(hours=1, minutes=10)), list(controller._clients.values())[0].id)
    assert list(controller._rooms["Room1"]._reservations)[0] == list(controller._reservations.values())[0]

def test_add_client_error():
    controller = Controller()
    controller.add_client("Mael", "Legoff", "Mael@uha.fr")
    with pytest.raises(Reservation_app_error):
        controller.add_client("Mael", "Legoff", "et@uha.fr")



def test_add_room_error():
    controller = Controller()
    controller.add_room("Room1", "Conference")
    with pytest.raises(Reservation_app_error):
        controller.add_room("Room1", "Conference")

def test_add_reservation_error():
    controller = Controller()
    controller.add_client("Mael", "Legoff", "mael@uha.fr")
    controller.add_room("Room1", "Conference")
    mael_uuid = controller.get_client_uuid("Mael")
    controller.add_reservation("Room1", TimeInterval(date(2026, 9, 6), time(12, 30), timedelta(hours=1, minutes=10)), mael_uuid)
    with pytest.raises(Reservation_app_error):
        # test if the reservation is in the past
        controller.add_reservation("Room1", TimeInterval(date(2020, 10, 1), time(12, 30), timedelta(hours=1, minutes=10)), mael_uuid)
    with pytest.raises(Reservation_app_error):
        # test if the reservation is not available
        controller.add_reservation("Room1", TimeInterval(date(2026, 9, 6), time(12, 30), timedelta(hours=1, minutes=10)), mael_uuid)
    with pytest.raises(Reservation_app_error):
        # test if the room does not exist
        controller.add_reservation("Room2", TimeInterval(date(2026, 9, 6), time(12, 30), timedelta(hours=1, minutes=10)), mael_uuid)
    with pytest.raises(Reservation_app_error):
        # test if the client does not exist
        controller.add_reservation("Room1", TimeInterval(date(2026, 9, 6), time(12, 30), timedelta(hours=1, minutes=10)), "not_a_client")