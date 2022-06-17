
class car:
    #constructor
    def __init__(self, name,factory,type,stock):
        self.name = name
        self.factory = factory
        self.type = type
        self.fuel = 100
        self.stock = stock
    
    #methods fo print car info
    def print_info(self):
        print(f"Car name: {self.name}")
        print(f"Car factory: {self.factory}")
        print(f"Car type: {self.type}")
        print(f"Car fuel: {self.fuel}")
        print(f"Car {self.stock}")
    
    #methods for car is running
    def run(self):
        print("\n\nCar is running")
        print(f"Car fuel: {self.fuel - 10}")

if __name__ == "__main__":
    car = car("Civic","Honda","Sedan","in Stock!")
    car.print_info()
    car.run()
