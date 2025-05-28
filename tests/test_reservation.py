from reservationApp.model.reservation.reservation import *
from reservationApp.model.room.room import Room



def test_reservation_str():
    room = Room("Room1", "Conference",12)
    tomorow = datetime.today()
    start_datetime = tomorow
    end_datetime = tomorow+ timedelta(hours=1)
    time_interval = TimeInterval(start_datetime, end_datetime)
    client_id = str(uuid.uuid4())
    reservation = Reservation(room.name, time_interval, client_id)
    print(reservation)
    assert str(reservation) == f"{{id : {reservation.id}, room : {"Room1"}, client_id : {client_id}, time_interval : {{start_time : {str(start_datetime)}; end_time : {str(end_datetime)}}}}}"

def test_reservation_overlap():
    room = Room("Room1", "Conference",12)
    tomorow = datetime.today()
    start_datetime = tomorow
    end_datetime = tomorow + timedelta(hours=1)
    time_interval = TimeInterval(start_datetime, end_datetime)
    client_id = str(uuid.uuid4())
    reservation = Reservation(room.name, time_interval, client_id)

    # Test for a conflicting timeInterval
    conflicting_start = tomorow - timedelta(hours=3)
    conflicting_end = tomorow + timedelta(hours=4)
    assert reservation.overlap_with(conflicting_start, conflicting_end) == True

    # Test for a non-conflicting timeInterval
    non_conflicting_start = tomorow - timedelta(hours=2)
    non_conflicting_end = tomorow - timedelta(hours=1)
    assert reservation.overlap_with(non_conflicting_start, non_conflicting_end) == False

def test_reservation_to_dictionnary():
    room = Room("Room1", "Conference",12)
    start_datetime = datetime(2026, 10, 1,12,29)
    end_datetime = datetime(2026, 10, 1,15,29)
    time_interval = TimeInterval(start_datetime, end_datetime)
    client_id = str(uuid.uuid4())
    reservation = Reservation(room.name, time_interval, client_id)

    reservation_dict = reservation.to_dictionnary()
    assert reservation_dict == {
        "id": reservation.id,
        "name": "Room1",
        "client_id": client_id,
        "timeInterval": time_interval.to_dictionnary(),
    }