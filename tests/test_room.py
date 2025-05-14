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
    start_day = datetime(2023, 10, 1)
    start_hour = time(12, 30)
    duration = timedelta(hours=1, minutes=10)
    time_interval = TimeInterval(start_day, start_hour, duration)
    client_id = str(uuid.uuid4())
    reservation = room.create_reservations(time_interval, client_id)
    
    assert len(room._reservations) == 1
    assert list(room._reservations.values())[0] == reservation


    


