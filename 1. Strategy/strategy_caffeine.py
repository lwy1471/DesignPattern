from abc import ABCMeta, abstractmethod

class CaffeineBeverage():
    __metaclass_ = ABCMeta
    
    def __init__(self, brewBehavier, addIngredientsBehavier):
        self.brew = brewBehavier
        self.addIngredients = addIngredientsBehavier
        
    def prepareBeverage(self):
        self.boilWater()
        self.brew.brew()
        self.pourInCup()
        if self.customerWantsIngredients():
            self.addIngredients.addIngredients()
    
    def boilWater(self):
        print('물 끓이는 중') 
    def pourInCup(self):
        print('컵에 물 따르는 중')
    
    def customerWantsIngredients(self):
        return True

        
class Coffee(CaffeineBeverage):

    def customerWantsIngredients(self):
        reply = input('설탕과 헤이즐넛을 넣을까요? (y/n) ')
        if reply == 'y':
            return True
        else :
            return False

class Tea(CaffeineBeverage):
    def customerWantsIngredients(self):
        reply = input('레몬을 넣을까요? (y/n) ')
        if reply == 'y':
            return True
        else :
            return False
            
# changeable Behavier
class BrewBehavier():
    __metaclass_ = ABCMeta
    
    @abstractmethod
    def brew(self):
        pass

class CoffeeBrew(BrewBehavier):
    def brew(self):
        print('커피 가는 중')

class TeaBrew(BrewBehavier):
    def brew(self):
        print('차 우리는 중')
        
class AddIngredientsBehavier():
    __metaclass_ = ABCMeta
    
    @abstractmethod
    def addIngredients(self):
        pass

class CoffeeIngredients(AddIngredientsBehavier):
    def addIngredients(self):
        print('설탕과 헤이즐넛 넣는 중')
        
class TeaIngredients(AddIngredientsBehavier):
    def addIngredients(self):
        print('레몬 넣는 중')
        
        
        
# Test Code

if __name__ == '__main__':
    coffeeBrew = CoffeeBrew()
    coffeeIngredients = CoffeeIngredients()
    coffee = Coffee(coffeeBrew, coffeeIngredients)
    coffee.prepareBeverage()
    print()
    
    teaBrew = TeaBrew()
    teaIngredients = TeaIngredients()
    tea = Tea(teaBrew, teaIngredients)
    tea.prepareBeverage()
    
    #change the Brewing
    print('Change the Brewing')
    tea = Tea(coffeeBrew, TeaIngredients)
    tea.prepareBeverage()