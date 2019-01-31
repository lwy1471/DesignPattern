from abc import ABCMeta, abstractmethod
 
# Computer ABS Class
class Computer():
    __metaclass__ = ABCMeta
    
    def __init__(self, cpu, ram, hdd):
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
    
    def getDescription(self):
        msg = ["CPU: ","RAM: ", "HDD: "]
        materials = (self.cpu, self.ram, self.hdd)
        return "CPU: {0}, RAM: {1}, SSD: {2}".format(self.cpu, self.ram, self.hdd)
    
    @abstractmethod
    def cost(self):
        pass

# Computer's Decorator ABS classes
class ComputerDecorator(Computer):
    __metaclass__ = ABCMeta
    
    def __init__(self, computer):
        self.computer = computer

    def getDescription(self):
        return self.computer.getDescription()
    
    @abstractmethod
    def cost(self):
        pass
        
# Computer's concrete classes
class BasicDesktop(Computer):
    
    def __init__(self, cpu, ram, hdd, monitor, ifDevices):
        super().__init__(cpu, ram, hdd)
        self.monitor = monitor
        self.ifDevices = ifDevices
    
    def cost(self):
        return 120
    
    def getDescription(self):
        origin = super().getDescription()
        append = "Monitor: {}, Interface: {}".format(self.monitor, self.ifDevices)
        return origin+" "+append
        
class Laptop(Computer):
    def cost(self):
        return 200
        

# Computer's Decorator concrete classes
class GPU(ComputerDecorator):
    def cost(self):
        return self.computer.cost() + 40

class SSD(ComputerDecorator):
    def cost(self):
        return self.computer.cost() + 20

class ExtraRam(ComputerDecorator):
    def cost(self):
        return self.computer.cost() + 10

if __name__ == "__main__":

    desktop = BasicDesktop('I7-6770k', '8GB', '1TB', 'DELL 24 Inch', 'Keyboard, Mouse')
    print("Basic Desktop spec.")
    print(desktop.getDescription())
    print("Cost : {}".format(desktop.cost()))
    
    desktop = GPU(desktop)
    print("GPU Desktop spec.")
    print(desktop.getDescription())
    print("Cost : {}".format(desktop.cost()))    
    
    desktop = SSD(desktop)
    print("GPU + SSD Desktop spec.")
    print(desktop.getDescription())
    print("Cost : {}".format(desktop.cost()))   

    desktop = ExtraRam(desktop)
    print("GPU + SSD + RAM Desktop spec.")
    print(desktop.getDescription())
    print("Cost : {}".format(desktop.cost()))   
    