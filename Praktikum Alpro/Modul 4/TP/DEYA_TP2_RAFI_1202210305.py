
class Car:
    #Constructor
    def __init__(self, name, factory, type, stock):
        self.name = name
        self.factory = factory
        self.type = type
        self.stock = stock
        self.fuel = 100
    
    #methods for print car info
    def print_info(self):
        print(f'Car Name    : {self.name}')
        print(f'Car Factory : {self.factory}')
        print(f'Car Type    : {self.type}')
        print(f'Car Fuel    : {self.fuel}')
        print(f'Stock       : {self.stock}')
    
    #methods if car is running
    def car_is_on(self):
        print('\nCar is running')
        print(f'Car fuel: {self.fuel - 10}')

if __name__ == '__main__':
    car = Car ('Speed','Lambo','Sports','in stock!')
    car.print_info()
    car.car_is_on()

       