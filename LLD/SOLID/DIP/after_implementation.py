from abc import ABC, abstractmethod 

class Mouse(ABC):
    pass

class WiredMouse(Mouse):
    pass

class BluetoothMouse(Mouse):
    pass

class Keyboard(ABC):
    pass

class WiredKeyboard(Keyboard):
    pass

class BluetoothKeyboard(Keyboard):
    pass

class MacBook:
    def __init__(self,keyboard, mouse):
        self.keyboard:Keyboard = keyboard
        self.mouse:Mouse = mouse

if __name__ == "__main__":
    laptop = MacBook(WiredKeyboard(),WiredMouse())
        
