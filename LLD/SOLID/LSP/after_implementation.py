from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def getNumberOfWheels(self):
        pass

class EngineVehicle(Vehicle,ABC):
   @abstractmethod
   def hasEngine(self):
        pass
    
class MotorCycle(EngineVehicle):
    def getNumberOfWheels(self):
        return 2
    
    def hasEngine(self):
        return True

class Car(EngineVehicle):
    def getNumberOfWheels(self):
        return 4
    
    def hasEngine(self):
        return True

class Bicycle(Vehicle):
    def getNumberOfWheels(self):
        return 2
    
if __name__ == "__main__":
    motorcycle = MotorCycle()
    car = Car()
    bicycle = Bicycle()
    print(str(motorcycle.hasEngine()))
    print(str(car.hasEngine()))
    print(str(bicycle.hasEngine())) #