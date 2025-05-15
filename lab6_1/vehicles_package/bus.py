class Bus:
    def __init__(self, fuel_consumption_per_100km, fuel_price, passenger_capacity):
        self.fuel_consumption_per_100km = fuel_consumption_per_100km
        self.fuel_price = fuel_price
        self.passenger_capacity = passenger_capacity

    def calculate_fuel_consumption(self, distance, passengers):
        # Увеличиваем расход топлива на 5% за каждые 10 пассажиров
        adjusted_consumption = self.fuel_consumption_per_100km * (1 + (passengers / self.passenger_capacity) * 0.05)
        return (distance / 100) * adjusted_consumption

    def calculate_trip_cost(self, distance, passengers):
        fuel_consumed = self.calculate_fuel_consumption(distance, passengers)
        return fuel_consumed * self.fuel_price

    def calculate_trip_time(self, distance, average_speed):
        return distance / average_speed