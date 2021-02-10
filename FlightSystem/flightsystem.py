class AirPlane:
    passengers = {}
    capacity = 0

    def __init__(self, capacity):
        self.capacity = capacity

    def set_plane_capacity(self, capacity):
        self.capacity = capacity

    def get_plane_capacity(self):
        return self.capacity

    def is_seat_available(self):
        if self.capacity - self.passengers == 0:
            return False
        else:
            return True


class BookingInformation:
    # customer = Customer()
    arrival_location = " "
    departure_location = " "
    departure_date = " "

    def __init__(self, departure_location, arrival_location, departure_date):
        self.arrival_location = arrival_location
        self.departure_location = departure_location
        self.departure_date = departure_date


class Customer:
    name = ""

    bookingInformation = BookingInformation(" ", " ", " ")

    has_pending_request = False

    def __init__(self):
        pass

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def book_a_seat(self):
        self.has_pending_request = True
        return self.bookingInformation

    def show_booking_information(self):
        return bookingInformation


class Admin:
    def assignSeat(self):
        Customer.show_booking_information(Customer())

        if AirPlane.is_seat_available():
            AirPlane.passengers.append(Customer.name)
        else:
            return 'No more seats available. Wait for the next flight.'
