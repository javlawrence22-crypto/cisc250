# =============================================================================
# Student Name: Javrick Lawrence
# Lab Title: Lab 6 - Vehicle Class
# Date: June 13, 2026
# =============================================================================

class Vehicle:
    def __init__(self, make, model, year, max_fuel=10):
        self.make = make
        self.model = model
        self.year = year
        self.max_fuel = max_fuel
        self.current_fuel = 0
        self.is_almost_empty = True

    def fuel_level(self, gallons):
        if gallons < 0:
            print(f"Can't set negative fuel: {gallons}")
        elif gallons > self.max_fuel:
            print(f"Can't set fuel to {gallons} — tank only holds {self.max_fuel}")
        else:
            self.current_fuel = float(gallons)
            self.empty_warning_check()

    def details(self):
        return f"{self.year} {self.make} {self.model}"

    def fuel_left(self):
        return round((self.current_fuel / self.max_fuel) * 100, 1)

    def empty_warning_check(self):
        if self.fuel_left() < 10:
            self.is_almost_empty = True
        else:
            self.is_almost_empty = False


# Task 2

vehicles = []

car1 = Vehicle("Toyota", "Mark X", 2020, 12.0)
car2 = Vehicle("Honda", "Civic", 2019, 11.0)
car3 = Vehicle("Suzuki", "Jimny", 2021, 14.0)
car4 = Vehicle("Nissan", "Latio", 2018, 8.0)

vehicles.extend([car1, car2, car3, car4])

car1.fuel_level(5.3)
car2.fuel_level(2.2)
car3.fuel_level(10.1)
car4.fuel_level(0.5)

car2.fuel_level(-4.4)
car4.fuel_level(100)

# Part 2

print("\n--- Vehicle Info ---")
for v in vehicles:
    print(v.details())
    print(f"Fuel: {v.current_fuel} gal")
    print(f"Percent left: {v.fuel_left()}%")
    print(f"Almost empty: {v.is_almost_empty}")
    print("---")