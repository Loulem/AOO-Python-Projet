from controller.controller import *
import pytest
def test_is_saved_uuid_a_string():
    controller = Controller()
    controller.add_client("Mael", "Legoff","mael@uha.fr")
    assert type( list( list( controller.model.data_to_dictionnary().values() )[0].keys() ) [0]) == str  # Check if the uuid is a string


def test_if_saved_are_correctly_loaded():
    

    controller = Controller()
    controller.add_client("Mael","Legoff", "mael@uha.fr")
    controller.add_client("Lou","Lemarechal" ,"lou@uha.fr")
    controller.add_client("Paul", "tin","paul@gmail.com")
    controller.add_room("Room1", "Conference")
    controller.add_room("Room2", "Meeting")
    tomorow = datetime.today() + timedelta(days=1)
    controller.add_reservation("Room1", TimeInterval(tomorow,tomorow+ timedelta(hours=1) ), "mael@uha.fr")
    controller.model.save_data("./data/test.json")
    controller2 = Controller()
    controller2.model.load_data("./data/test.json")
    assert controller2.model.data_to_dictionnary() == controller.model.data_to_dictionnary()





def test_if_controller_Reservations_is_same_as_room_Reservation():
    controller = Controller()
    controller.add_client("Mael", "Legoff", "mael@uha.fr")
    controller.add_room("Room1", "Conference")
    tomorow = datetime.today() + timedelta(days=1)
    controller.add_reservation("Room1", TimeInterval(tomorow,tomorow+ timedelta(hours=1)), "mael@uha.fr")
    assert list(controller.rooms_manager.rooms["Room1"]._reservations.values())[0] == list(controller.reservations_manager.reservations.values())[0]

def test_add_client_error():
    controller = Controller()
    controller.add_client("Mael", "Legoff", "Mael@uha.fr")
    with pytest.raises(ClientError):
        controller.add_client("Mael", "Legoff", "Mael@uha.fr")



def test_add_room_error():
    controller = Controller()
    controller.add_room("Room1", "Conference")
    with pytest.raises(RoomError):
        controller.add_room("Room1", "Conference")


def test_add_reservation_error():
    controller = Controller()
    controller.add_client("Mael", "Legoff", "mael@uha.fr")
    controller.add_room("Room1", "Conference")
    tomorow = datetime.today() + timedelta(days=1)
    controller.add_reservation("Room1", TimeInterval(tomorow,tomorow + timedelta(hours=1)), "mael@uha.fr")
    with pytest.raises(Reservation_app_error):
        # test if the reservation is in the past
        controller.add_reservation("Room1", TimeInterval(tomorow-timedelta(days = 2),tomorow - timedelta(days=1)), "mael@uha.fr")
    with pytest.raises(Reservation_app_error):
        # test if the room is not available
        controller.add_reservation("Room1", TimeInterval(tomorow , tomorow+ timedelta(hours=5)), "mael@uha.fr")
    with pytest.raises(Reservation_app_error):
        # test if the room does not exist
        controller.add_reservation("Room2", TimeInterval(tomorow + timedelta(hours=2),tomorow+ timedelta(hours=5)), "mael@uha.fr")
    with pytest.raises(Reservation_app_error):
        # test if the client does not exist
        controller.add_reservation("Room1", TimeInterval(tomorow + timedelta(hours=2),tomorow+ timedelta(hours=5)), "not_a_client")