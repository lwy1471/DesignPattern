from abc import ABC, abstractmethod

# command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
        
        
# command concrete class
class LightOnCommand(Command):
    
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.on()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light
    
    def execute(self):
        self.light.off()

# Recieve class

class Light():
    def on(self):
        print('Light is on')
    def off(self):
        print('Light is off')

        
# Invoker class
class RemoteControl():
    
    def __init__(self):
        self.slot = []
    
    def setCommand(self, slotNum, command):
        self.slot.insert(slotNum, command)
    
    def buttonPressed(self, slotNum):
        self.slot[slotNum].execute()
        
if __name__ == '__main__':
    remote = RemoteControl()
    remote.setCommand(0, LightOnCommand(Light()))
    remote.setCommand(1, LightOffCommand(Light()))
    
    remote.buttonPressed(0)
    remote.buttonPressed(1)
    print('change button 0->1, 1->0')
     
    remote.setCommand(0, LightOffCommand(Light()))
    remote.setCommand(1, LightOnCommand(Light()))
    remote.buttonPressed(0)
    remote.buttonPressed(1)