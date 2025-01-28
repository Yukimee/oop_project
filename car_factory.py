from car import Car


class CarFactory:
    @staticmethod
    def create_car(car_id, make, model, year, mileage):
        return Car(car_id, make, model, year, mileage)


# Example usage
car2 = CarFactory.create_car(102, "Honda", "Civic", 2019, 30000)
print(car2.get_car_details())
