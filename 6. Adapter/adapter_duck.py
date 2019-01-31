from abc import ABC, abstractmethod

class Duck(ABC):
    @abstractmethod
    def quack(self):
        pass
        
    @abstractmethod
    def fly(self):
        pass

# Target        
class MallardDuck(Duck):
    def quack(self):
        print('Quack')
    def fly(self):
        print('MallardDuck is flying')
        

# Adaptee
class Turkey():
    def gobble(self):
        print('Gobble Gobble')
    def fly(self):
        print('Turkey is flying')

# Adapter
class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey
    
    def quack(self):
        self.turkey.gobble()
    
    def fly(self):
        self.turkey.fly()
        
        
# Test
def testDuck(duck):
    duck.quack()
    duck.fly()

if __name__ == '__main__':
    mallardDuck = MallardDuck()
    turkeyAdapter = TurkeyAdapter(Turkey())
    

    testDuck(mallardDuck)
    testDuck(turkeyAdapter)
