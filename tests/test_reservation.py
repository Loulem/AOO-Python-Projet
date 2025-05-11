from reservation import *
from room import Room



def test_reservation_str():
    room = Room("Room1", "Conference")
    start_day = datetime(2025, 10, 1)
    start_hour = time(12, 30)
    duration = timedelta(hours=1, minutes=10)
    time_interval = TimeInterval(start_day, start_hour, duration)
    client_id = str(uuid.uuid4())
    reservation = Reservation(room.name, time_interval, client_id)
    print(reservation)
    assert str(reservation) == f"{{id : {reservation.id}, room : {"Room1"}, client_id : {client_id}, time_interval : {{start_time : 2025-10-01 12:30:00; end_time : 2025-10-01 13:40:00}}}}"

def test_reservation_overlap():
    room = Room("Room1", "Conference")
    start_day = datetime(2025, 10, 1)
    start_hour = time(12, 30)
    duration = timedelta(hours=1, minutes=10)
    time_interval = TimeInterval(start_day, start_hour, duration)
    client_id = str(uuid.uuid4())
    reservation = Reservation(room.name, time_interval, client_id)

    # Test for a conflicting timeInterval
    conflicting_start = datetime.combine(start_day, time(12, 0))
    conflicting_end = datetime.combine(start_day, time(13, 0))
    assert reservation.overlap_with(conflicting_start, conflicting_end) == True

    # Test for a non-conflicting timeInterval
    non_conflicting_start = datetime.combine(start_day, time(14, 0))
    non_conflicting_end = datetime.combine(start_day, time(15, 0))
    assert reservation.overlap_with(non_conflicting_start, non_conflicting_end) == False

def test_reservation_to_dictionnary():
    room = Room("Room1", "Conference")
    start_day = datetime(2025, 10, 1)
    start_hour = time(12, 30)
    duration = timedelta(hours=1, minutes=10)
    time_interval = TimeInterval(start_day, start_hour, duration)
    client_id = str(uuid.uuid4())
    reservation = Reservation(room.name, time_interval, client_id)

    reservation_dict = reservation.to_dictionnary()
    assert reservation_dict == {
        "id": reservation.id,
        "name": "Room1",
        "client_id": client_id,
        "timeInterval": time_interval.to_dictionnary(),
    }