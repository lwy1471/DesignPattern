from abc import ABC, abstractmethod

# command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
        
        
# command concrete class

class NoCommand(Command):
    def execute(self):
        pass

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

class Aircon_turnOnOff(Command):
    def __init__(self, aircon):
        self.aircon = aircon
    
    def execute(self):
        self.aircon.on_and_off()
        
class Aircon_currentTemp(Command):
    def __init__(self, aircon):
        self.aircon = aircon
    def execute(self):
        self.aircon.currentTemper()
        
class Tv_turnOnOff(Command):
    def __init__(self, tv):
        self.tv = tv
        
    def execute(self):
        self.tv.on_and_off()

class Tv_channelChange(Command):
    def __init__(self, tv):
        self.tv = tv
    def execute(self):
        self.tv.change_channel()
        
# Recieve class

class Light():
    def on(self):
        print('Light is on')
    def off(self):
        print('Light is off')

class Aircon():
    def __init__(self):
        self.power = False
        
    def on_and_off(self):
        if self.power == False:
            print('Air Conditioner is On')
            self.power = True
        else:
            print('Air Conditioner is Off')
            self.power = False
            
    def currentTemper(self):
        print('Current Temperature is 18c')
        
class Tv():
    def __init__(self):
        self.power = False
        
    def on_and_off(self):
        if self.power == False:
            print('Tv is On')
            self.power = True
        else:
            print('Tv is Off')
            self.power = False
    
    def change_channel(self):
        print('Tv Channel is changed')

# Invoker class
class RemoteControl():
    
    def __init__(self):
        self.onSlot = []
        self.offSlot = []
        
        for i in range(7):
            self.onSlot.insert(i, NoCommand())
            self.offSlot.insert(i, NoCommand())

    def setCommand(self, slotNum, onCommand, offCommand):
        self.onSlot.insert(slotNum, onCommand)
        self.offSlot.insert(slotNum, offCommand)
    
    def onButtonPressed(self, slotNum):
        self.onSlot[slotNum].execute()
    def offButtonPressed(self, slotNum):
        self.offSlot[slotNum].execute()
        
if __name__ == '__main__':
    remote = RemoteControl()
    
    remote.setCommand(0, LightOnCommand(Light()), LightOffCommand(Light()))
    aircon = Aircon()
    remote.setCommand(1, Aircon_turnOnOff(aircon), Aircon_currentTemp(aircon))
    tv = Tv()
    remote.setCommand(2, Tv_turnOnOff(tv), Tv_channelChange(tv))
    
    remote.onButtonPressed(0)
    remote.offButtonPressed(0)
    
    remote.onButtonPressed(1)
    remote.onButtonPressed(1)
    remote.onButtonPressed(1)
    remote.offButtonPressed(1)
    
    remote.onButtonPressed(2)
    remote.onButtonPressed(2)
    remote.onButtonPressed(2)
    remote.offButtonPressed(2)
    
