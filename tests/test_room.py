from reservationApp.model.room.room import *

def test_Room_str():
    room = Room("Room1", "Conference")
    assert str(room) == f"{{name : Room1, type : Conference}}"
    # Test if the string representation of the room is correct

def test_Room_to_dictionnary():
    room = Room("Room1", "Conference")
    room_dict = room.to_dictionnary()
    assert room_dict == {
        "name": "Room1",
        "type": "Conference",
        "reservations": [],
    }
    # Test if the dictionary representation of the room is correct


def test_Room_create_reservations():
    room = Room("Room1", "Conference")
    start_datetime = datetime(2026, 10, 1,12,29)
    end_datetime = datetime(2026, 10, 1,15,29)
    time_interval = TimeInterval(start_datetime, end_datetime)
    client_id = str(uuid.uuid4())
    reservation = room.create_reservations(time_interval, client_id)
    
    assert len(room._reservations) == 1
    assert list(room._reservations.values())[0] == reservation


    


