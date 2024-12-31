# Write a Flight class with methods to book seats, display available seats, 
#and cancel bookings. Use properties to enforce business rules (e.g., seat limits).


class Flight:
    def __init__(self, flight_number, total_seats):
        self.flight_number = flight_number
        self.total_seats = total_seats
        self.booked_seats = 0

    @property
    def available_seats(self):
        return self.total_seats - self.booked_seats

    def book_seat(self, number_of_seats):
        if number_of_seats <= 0:
            return "Invalid number of seats to book."
        if self.available_seats >= number_of_seats:
            self.booked_seats += number_of_seats
            return f"Successfully booked {number_of_seats} seat(s)."
        else:
            return f"Cannot book {number_of_seats} seat(s). Only {self.available_seats} seat(s) available."

    def cancel_booking(self, number_of_seats):
        if number_of_seats <= 0:
            return "Invalid number of seats to cancel."
        if number_of_seats <= self.booked_seats:
            self.booked_seats -= number_of_seats
            return f"Successfully canceled {number_of_seats} seat(s)."
        else:
            return f"Cannot cancel {number_of_seats} seat(s). Only {self.booked_seats} seat(s) booked."

    def display_available_seats(self):
        return f"Available seats: {self.available_seats}"

# Example usage:
if __name__ == "__main__":
    flight = Flight("AA123", 100)

    print(flight.display_available_seats())  

    print(flight.book_seat(5))  
    print(flight.display_available_seats()) 

    print(flight.book_seat(10))  
    print(flight.display_available_seats())  

    print(flight.cancel_booking(3))  
    print(flight.display_available_seats())  

    print(flight.cancel_booking(15)) 
    print(flight.display_available_seats())  