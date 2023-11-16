from abc import ABC, abstractmethod

class WaiterInterface(ABC):
    @abstractmethod
    def serveCustomers():
        pass

    @abstractmethod
    def takeOrder():
        pass

class ChefInterface(ABC):
    @abstractmethod
    def cookFood():
        pass

    @abstractmethod
    def decideMenu():
        pass

class waiter(WaiterInterface):
    def serveCustomers():
        print("serving the customer")

    def takeOrder():
        print("taking orders")