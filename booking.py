class Booking:
    def __init__(self, booking_id, user_id, car_id, rental_days, daily_rate):
        self.__booking_id = booking_id
        self.__user_id = user_id
        self.__car_id = car_id
        self.__rental_days = rental_days
        self.__daily_rate = daily_rate
        self.__total_cost = self.calculate_total_cost()

    def calculate_total_cost(self):
        return self.__rental_days * self.__daily_rate

    def get_booking_details(self):
        return f"Booking ID: {self.__booking_id}, Car ID: {self.__car_id}, Total Cost: ${self.__total_cost}"


# Example usage
booking1 = Booking(1001, 1, 123, 7, 50)
print(booking1.get_booking_details())
