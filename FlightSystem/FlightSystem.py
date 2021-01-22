class AirPlane():

    passengers = {}
    def __init__(self, capacity):
        self.capacity = capacity

    def set_plane_capacity(self, capacity):
        self.capacity = capacity

    def get_place_capacity():
        return self.capacity

    def is_seat_available():
        if self.capacity - passengers == 0:
            return "No more seats available" 


class Customer():

    has_pending_request = False
    name = " "

    def __init__(self, name):
        self.name = name

    def book_a_seat():
        get_booking_information()
        has_pending_request = True


    def fill_booking_information(self, location, name):
        self.location = location
        self.name = name

    def get_booking_information():
        information = [
            "name" : self.name,
            "location" : self.location
        ]


class Admin():

    def assignSeat():

        Customer.get_booking_information()

        if not AirPlane.is_seat_available():
            passengers.append(Customer.name)
        else:
            return AirPlane.is_seat_available()

    
        
        