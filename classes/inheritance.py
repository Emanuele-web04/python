class Vehicle():
    def __init__(self, price, gas, color) -> None:
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100
    
    def emptyGas(self) -> bool:
        self.gas = 0
        return True
    
    def gasLeft(self):
        return self.gas

class Car(Vehicle):
    def __init__(self, price, gas, color, speed) -> None:
        # super allows you to get access to the superclass
        # super per se is just a superclass object, 
        # but with init in this case, you're passing the whole init to this child class
        super().__init__(price, gas, color)
        self.speed = speed
    
    def clacson(self):
        print("Beep beep")

class Truck(Vehicle):
    def __init__(self, price, gas, color, tires) -> None:
        super().__init__(price, gas, color)
        self.tires = tires

    def clacson(self):
        print("Honk honk") 
    


