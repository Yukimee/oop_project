class Car:
    def __init__(self, car_id, make, model, year, mileage, available=True):
        self.__car_id = car_id
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage
        self.__available = available

    def get_car_details(self):
        return f"{self.__make} {self.__model} ({self.__year}), Mileage: {self.__mileage}, Available: {self.__available}"

    def update_availability(self, status):
        self.__available = status


# Example usage
car1 = Car(101, "Toyota", "Alphard", 2024, 5000)
print(car1.get_car_details())
car1.update_availability(False)
print(car1.get_car_details())

car_inventory = {}


def add_car(car):
    car_inventory[car.get_car_details()] = car
    return "Car added successfully!"


def delete_car(car_make):
    for key in list(car_inventory.keys()):
        if car_make in key:
            del car_inventory[key]
            return "Car deleted successfully!"
    return "Car not found."


# Example usage
add_car(car1)
print(delete_car("Toyota"))

