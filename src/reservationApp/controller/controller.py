from __future__ import annotations # if some class use type defined later 
from reservationApp.model.model import *
from reservationApp.view import View

class Reservation_app_error(Exception):
    """Base class for all exceptions raised by the reservation app"""
    pass


class Controller():
    def __init__(self):
        self.rooms_manager = RoomsManager()
        self.reservations_manager = ReservationsManager()
        self.clients_manager = ClientManager()
        self.model = Model(self.rooms_manager,self.reservations_manager,self.clients_manager)
        self.view = None

    def start_view(self):
        """Start the view"""
        self.view = View(self)
        self.view.main()

    def add_client(self, name : str, first_name : str ,email : str) -> None :
        """Add a new client to the model"""
        try:
            self.clients_manager.add_client( name , first_name ,email )
            self.view.main_menu
        except ClientError as e:
            self.view.show_error_message(str(e))    
        else:
            self.view.show_success_message(f"Client {name} {first_name} with email {email} added successfully.")

    def add_room(self, name : str, type : str,capacity) -> None:
        """Add a new room to the model"""
        try:
            self.rooms_manager.add_room(name, type,capacity)
            self.view.main_menu
        except RoomError as e:
            self.view.show_error_message(str(e))    
        else:
            self.view.show_success_message(f"Room {name} of type {type} with capacity {capacity} added successfully.")


    def get_room_available_time_interval(self, room : Room, time_interval : timedelta) -> list:
        """Show all the available time interval for a room"""
        pass

    def get_rooms_available(self,start_year,start_month,start_day,start_hour,minute,end_year,end_month,end_day,end_hour,end_minute)->tuple [list[Room]]:
        """Give a list of all the available room for a time interval"""
        try :
            time_interval = TimeInterval(datetime(start_year, start_month, start_day, start_hour, minute),datetime(end_year, end_month, end_day, end_hour, end_minute))
        except Exception as e:
            return self.view.show_error_message(f"Error creating time interval: {str(e)}")
        self.rooms_manager.get_available_rooms(time_interval)
        standards_rooms = [room for room in self.rooms_manager.rooms.values() if room.type == "Standard"]
        conferences_rooms = [room for room in self.rooms_manager.rooms.values() if room.type == "Conference"]
        informatiques_rooms = [room for room in self.rooms_manager.rooms.values() if room.type == "Informatique"]
        return  standards_rooms, conferences_rooms, informatiques_rooms

    
    def add_reservation(self, room : str, time_interval : TimeInterval, client_email : str) -> None:
        """Create a new reservation for a room"""
        if not self.rooms_manager.is_a_room(room):
            raise Reservation_app_error(f"Room {room} does not exist")
        
        if client_email not in self.clients_manager.clients:
            raise Reservation_app_error(f"Client {client_email} does not exist")
        
        if not self.rooms_manager.rooms[room].is_available(time_interval):
            raise Reservation_app_error(f"Room {room} is not available for the time interval {time_interval}")
        
        if time_interval.start_datetime < datetime.today():
            raise Reservation_app_error(f"The start of the reservation has already passed")
        
        new_reservation = self.rooms_manager.rooms[room].create_reservations(time_interval,client_email)
        self.reservations_manager.add_reservations(new_reservation)
        

    




if __name__ == "__main__":

    controller = Controller()
    controller.start_view()

    """
    controller = Controller()
    controller.add_client("Mael","Legoff", "mael@uha.fr")
    controller.add_client("Lou","Lemarechal" ,"lou@uha.fr")
    controller.add_client("Paul", "tin","paul@gmail.com")
    controller.add_room("Room1", "Conference")
    controller.add_room("Room2", "Meeting")
    controller.add_reservation("Room1", TimeInterval(datetime(2026, 10, 1,12,20), datetime(2026, 10, 1,12,20)), "mael@uha.fr")
    
    controller.model.save_data("./data/test.json")
    controller2 = Controller()
    controller2.model.load_data("./data/test.json")
    print(controller2.model.clients_manager.clients_email[0])
    t1 = datetime.today()
    mael_name = controller.clients_manager.clients_name
    controller.clients_manager.clients["mael@uha.fr"].name = "hello"
    print(controller.clients_manager.clients_name)
    print(mael_name)
    t2 = t1 + timedelta(minutes=1)
    print(t1 < t2)
    print(t2)"""