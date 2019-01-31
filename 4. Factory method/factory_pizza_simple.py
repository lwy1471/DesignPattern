from abc import ABCMeta, abstractmethod

class Pizza():
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def prepare(self):
        pass
    @abstractmethod
    def bake(self):
        pass
    @abstractmethod
    def cut(self):
        pass
    @abstractmethod
    def box(self):
        pass

        
class Cheesepizza(Pizza):
    def prepare(self):
        print('Cheesepizza is prepared')

    def bake(self):
        print('Cheesepizza is baked')

    def cut(self):
        print('Cheesepizza is cut')

    def box(self):
        print('Cheesepizza is boxed')

class Clampizza(Pizza):
    def prepare(self):
        print('Clampizza is prepared')

    def bake(self):
        print('Clampizza is baked')

    def cut(self):
        print('Clampizza is cut')

    def box(self):
        print('Clampizza is boxed')
        
        
class Pepperonipizza(Pizza):
    def prepare(self):
        print('Pepperonipizza is prepared')

    def bake(self):
        print('Pepperonipizza is baked')

    def cut(self):
        print('Pepperonipizza is cut')

    def box(self):
        print('Pepperonipizza is boxed')

        

class SimplePizzaFactory():
    def createPizza(self, type):
        if type == 'cheese':
            pizza = Cheesepizza()
        elif type == 'clam':
            pizza = Clampizza()
        elif type == 'pepperoni':
            pizza = Pepperonipizza()
        
        return pizza

class PizzaStore():
    
    def __init__(self, factory):
        self.pizzaFactory = factory
    def orderPizza(self, type):
        pizza = self.pizzaFactory.createPizza(type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
        
        
        
if __name__ == '__main__':
    simpleFactory = SimplePizzaFactory()
    pizzaStore = PizzaStore(simpleFactory)
    
    pizzaStore.orderPizza('clam')
    pizzaStore.orderPizza('cheese')
    pizzaStore.orderPizza('pepperoni')