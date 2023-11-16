from abc import ABC, abstractmethod

class InvoiceDao(ABC):
    @abstractmethod
    def save(invoice):
        pass

class DatabaseInvoiceDao(InvoiceDao):
    def save(invoice):
        # save to DB
        pass

class FileInvoiceDao(InvoiceDao):
    def save(invoice):
        # save to file
        pass 