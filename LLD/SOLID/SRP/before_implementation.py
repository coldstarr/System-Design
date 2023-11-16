class Pendrive:
    def __init__(self,brand,size,price):
        self.brand = brand
        self.size = size
        self.price = price
    
    def __str__(self):
        return self.brand+" "+"Pendrive"

class Invoice:
    def __init__(self, pendrive, quantity):
        self.pendrive = pendrive
        self.quantity = quantity
    
    def calculateTotal(self):
        price = self.pendrive.price*self.quantity
        return price
    
    def printInvoice(self):
        pass

    def saveToDB(self):
        pass

if __name__ == "__main__":
    pendrive = Pendrive("Dell",32,1000)
    invoice = Invoice(pendrive,2)
    total_price = invoice.calculateTotal()
    print("Total amount: ", total_price)

    