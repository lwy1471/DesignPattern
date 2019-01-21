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

        
class NYCheesepizza(Pizza):
    def prepare(self):
        print('NYCheesepizza is prepared')

    def bake(self):
        print('NYCheesepizza is baked')

    def cut(self):
        print('NYCheesepizza is cut')

    def box(self):
        print('NYCheesepizza is boxed')

class CFCheesepizza(Pizza):
    def prepare(self):
        print('CFCheesepizza is prepared')

    def bake(self):
        print('CFCheesepizza is baked')

    def cut(self):
        print('CFCheesepizza is cut')

    def box(self):
        print('CFCheesepizza is boxed')        
        
class NYClampizza(Pizza):
    def prepare(self):
        print('NYClampizza is prepared')

    def bake(self):
        print('NYClampizza is baked')

    def cut(self):
        print('NYClampizza is cut')

    def box(self):
        print('NYClampizza is boxed')

class CFClampizza(Pizza):
    def prepare(self):
        print('CFClampizza is prepared')

    def bake(self):
        print('CFClampizza is baked')

    def cut(self):
        print('CFClampizza is cut')

    def box(self):
        print('CFClampizza is boxed')        
        
class NYPepperonipizza(Pizza):
    def prepare(self):
        print('NYPepperonipizza is prepared')

    def bake(self):
        print('NYPepperonipizza is baked')

    def cut(self):
        print('NYPepperonipizza is cut')

    def box(self):
        print('NYPepperonipizza is boxed')


class CFPepperonipizza(Pizza):
    def prepare(self):
        print('CFPepperonipizza is prepared')

    def bake(self):
        print('CFPepperonipizza is baked')

    def cut(self):
        print('CFPepperonipizza is cut')

    def box(self):
        print('CFPepperonipizza is boxed')        
        


class PizzaStore():

    __metaclass__ = ABCMeta
    
    def __init__(self):
        pass
    def orderPizza(self, type):
        pizza = self.createPizza(type)
        
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza
    
    @abstractmethod
    def createPizza(self, type):
        pass



class NYPizzaStore(PizzaStore):
    
    def createPizza(self, type):
        if type == 'cheese':
            pizza = NYCheesepizza()
        elif type == 'clam':
            pizza = NYClampizza()
        elif type == 'pepperoni':
            pizza = NYPepperonipizza()
        
        return pizza

class CFPizzaStore(PizzaStore):

    def createPizza(self, type):
        if type == 'cheese':
            pizza = CFCheesepizza()
        elif type == 'clam':
            pizza = CFClampizza()
        elif type == 'pepperoni':
            pizza = CFPepperonipizza()
        
        return pizza    
        
if __name__ == '__main__':
    
    nyPizzaStore = NYPizzaStore()
    
    nyPizzaStore.orderPizza('clam')
    nyPizzaStore.orderPizza('cheese')
    nyPizzaStore.orderPizza('pepperoni')
    print()
    
    cfPizzaStore = CFPizzaStore()
    cfPizzaStore.orderPizza('clam')
    cfPizzaStore.orderPizza('cheese')
    cfPizzaStore.orderPizza('pepperoni')
    