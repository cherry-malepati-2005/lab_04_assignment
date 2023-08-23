class Flight:
    def __init__(self, flight_id, from_city, to_city, price):
        self.flight_id = flight_id
        self.from_city = from_city
        self.to_city = to_city
        self.price = price

class FlightTable:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights_by_city(self, city_code):
        city_flights = []
        for flight in self.flights:
            if flight.from_city == city_code or flight.to_city == city_code:
                city_flights.append(flight)
        return city_flights

    def search_flights_from_city(self, from_city_code):
        from_city_flights = []
        for flight in self.flights:
            if flight.from_city == from_city_code:
                from_city_flights.append(flight)
        return from_city_flights

    def search_flights_between_cities(self, from_city_code, to_city_code):
        between_cities_flights = []
        for flight in self.flights:
            if flight.from_city == from_city_code and flight.to_city == to_city_code:
                between_cities_flights.append(flight)
        return between_cities_flights

def main():
    flight_table = FlightTable()

    flight_data = [
        ("AI161E90", "BLR", "BOM", 5600),
        ("BR161F91", "BOM", "BBI", 6750),
        ("AI161F99", "BBI", "BLR", 8210),
        ("VS171E20", "JLR", "BBI", 5500),
        ("AS171G30", "HYD", "JLR", 4400),
        ("AI131F49", "HYD", "BOM", 3499)
    ]

    for data in flight_data:
        flight = Flight(*data)
        flight_table.add_flight(flight)

    cities = {
        "BLR": "Bengaluru",
        "BOM": "Mumbai",
        "BBI": "Bhubaneswar",
        "HYD": "Hyderabad",
        "JLR": "Jabalpur"
    }

    while True:
        print("\nSearch options:")
        print("1. Flights for a particular City")
        print("2. Flights From a city")
        print("3. Flights between two given cities")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city_code = input("Enter city code (e.g., BLR, BOM, BBI, HYD, JLR): ")
            if city_code in cities:
                result = flight_table.search_flights_by_city(city_code)
                city_name = cities[city_code]
                print(f"Flights involving {city_name}:")
                for flight in result:
                    print(f"{flight.flight_id} - From: {cities[flight.from_city]} To: {cities[flight.to_city]} Price: {flight.price}")
            else:
                print("Invalid city code!")

        elif choice == "2":
            from_city_code = input("Enter city code for departure (e.g., BLR, BOM, BBI, HYD, JLR): ")
            if from_city_code in cities:
                result = flight_table.search_flights_from_city(from_city_code)
                city_name = cities[from_city_code]
                print(f"Flights departing from {city_name}:")
                for flight in result:
                    print(f"{flight.flight_id} - To: {cities[flight.to_city]} Price: {flight.price}")
            else:
                print("Invalid city code!")

        elif choice == "3":
            from_city_code = input("Enter city code for departure (e.g., BLR, BOM, BBI, HYD, JLR): ")
            to_city_code = input("Enter city code for arrival (e.g., BLR, BOM, BBI, HYD, JLR): ")
            if from_city_code in cities and to_city_code in cities:
                result = flight_table.search_flights_between_cities(from_city_code, to_city_code)
                from_city_name = cities[from_city_code]
                to_city_name = cities[to_city_code]
                print(f"Flights from {from_city_name} to {to_city_name}:")
                for flight in result:
                    print(f"{flight.flight_id} Price: {flight.price}")
            else:
                print("Invalid city code(s)!")
        
        elif choice == "4":
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
