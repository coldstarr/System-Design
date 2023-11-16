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
    def __init__(self):
        self.keyboard:WiredKeyboard = WiredKeyboard()
        self.mouse:WiredMouse = WiredMouse()
        
