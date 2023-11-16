class InvoiceDao:
    def __init__(self,invoice):
        self.invoice = invoice
    
    def saveToDB(self):
        pass

# Modified
class InvoiceDao:
    def __init__(self,invoice):
        self.invoice = invoice
    
    def saveToDB(self):
        pass

    def saveToFile(filename):
        pass

if __name__ == "__main__":
    invoiceDao = InvoiceDao()
    invoiceDao.saveToFile()