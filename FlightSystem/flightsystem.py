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


# class Customer:
#     name = ""
#
#     has_pending_request = False
#     name = " "
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def book_a_seat(self):
#         self.get_booking_information()
#         has_pending_request = True
#
#     def fill_booking_information(self, location):
#         location = location
#
#     def get_booking_information(self):
#         information = {
#             "name": self.name,
#             "location": self.location
#         }


# class BookingInformation:
#     customer = Customer(Customer.get_name())
#     arrival_location = " "
#     departure_location = " "
#     Customer.__init__()


# class Admin:
#     def assignSeat(self):
#         Customer.get_booking_information(Customer())
#
#         if not AirPlane.is_seat_available():
#             AirPlane.passengers.append(Customer.name)
#         else:
#             return AirPlane.is_seat_available()
