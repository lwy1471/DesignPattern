from abc import ABCMeta, abstractmethod

#Abstract Class
class Display():
    __metaclass__ = ABCMeta
 
    def __init__(self, user, resolution, interface):
        self.resolution = resolution
        self.user = user
        self.setInputIF(interface)
            
    @abstractmethod
    def introItself(self):
        pass
           
    def displayIF(self):
        return self.InputInterface.getInterface()
        
    def setInputIF(self, interface):
        self.InputInterface = interface
        
        
class InputIF():
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def getInterface(self):
        pass

# Display concrete classes       
class Monitor(Display):
    def introItself(self):
        print("I am Monitor. My input interface is " + self.displayIF())
        

class Mobile(Display):        
    def introItself(self):
        print("I am Mobile. My input interface is " + self.displayIF())
        
class TemperatureDisplay(Display):
    def introItself(self):
        print("I am Temperature Display. " + self.displayIF())
        
        
        
# Input Interface concrete classes
class Mouse(InputIF):
    def getInterface(self):
        return "Mouse"
        
class Button(InputIF):
    def getInterface(self):
        return "Button"
        
class RemoteCtrl(InputIF):
    def getInterface(self):
        return "Remote Controller"

class Touch(InputIF):
    def getInterface(self):
        return "Touch"

class NoneInterface(InputIF):
    def getInterface(self):
        return "I have no input interface."
        
        
# Test Class

if __name__ == '__main__':
    monitor = Monitor('hadong','160x90', Mouse())
    mobile = Mobile('hadong', '9x16', Touch())
    temperatureDisplay = TemperatureDisplay('hadong', '5x5', NoneInterface())
    
    monitor.introItself()
    mobile.introItself()
    temperatureDisplay.introItself()
    
    #change interface
    monitor.setInputIF(Touch())
    monitor.introItself()
    print("Now Monitor is touch screen.")
    
    