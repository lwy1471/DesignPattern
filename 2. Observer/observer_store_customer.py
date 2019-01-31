from abc import ABC, abstractmethod

class Store():
    def __init__(self):
        self.subscribers = []
        self.state = None
        self.inventory = None
    
    def addSubscriber(self, subscriber):
        self.subscribers.append(subscriber)
        
    def unSubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
        
    def notifySubscribers(self):
        for subscriber in self.subscribers:
            subscriber.update(self.inventory)
            
            
class Customer(ABC):
    def __init__(self, observer):
        self.observer = observer
        self.observer.addSubscriber(self)
        
    def update(self, inventory):
        print('{0} noticed {1} items'.format(self.__class__.__name__,inventory))
        print('The Cost is {0}.'.format(self.cost()*inventory))
    def cost(self):
        return 10
        
class NewMember(Customer):
    def cost(self):
        return super().cost()*0.9


class OldMember(Customer):
    def cost(self):
        return super().cost()*0.8

class NormalCustomer(Customer):
    pass
    


# Test
if __name__ == '__main__':
    store = Store()
    
    normal = NormalCustomer(store)
    newM = NewMember(store)
    oldM = OldMember(store)

    
    print('---Store\'s got new items---')
    store.inventory = 4
    store.notifySubscribers()
    
    print('---The normal customer wants to stop subscribing---')
    store.unSubscribe(normal)
    store.notifySubscribers()