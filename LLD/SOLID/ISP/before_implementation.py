from abc import ABC, abstractmethod

class RestaurantEmployee(ABC):
    @abstractmethod
    def washDishes():
        pass

    @abstractmethod
    def serveCustomers():
        pass

    @abstractmethod
    def cookFood():
        pass

class waiter(RestaurantEmployee):
    def washDishes():
        # not my job
        pass

    def serveCustomers():
        # yes and here is my implementation
        print("Serving the customer")
    
    def cookFood():
        # not my job
        pass