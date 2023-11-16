from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def getNumberOfWheels(self):
        pass

    @abstractmethod
    def hasEngine(self):
        pass

class MotorCycle(Vehicle):
    def getNumberOfWheels(self):
        return 2
    
    def hasEngine(self):
        return True

class Car(Vehicle):
    def getNumberOfWheels(self):
        return 4
    
    def hasEngine(self):
        return True

class Bicycle(Vehicle):
    def getNumberOfWheels(self):
        return 2
    
    def hasEngine(self):
        raise("No engine")
    
if __name__ == "__main__":
    motorcycle = MotorCycle()
    car = Car()
    bicycle = Bicycle()
    print(str(motorcycle.hasEngine()))
    print(str(car.hasEngine()))
    print(str(bicycle.hasEngine())) #