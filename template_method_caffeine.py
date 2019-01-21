from abc import ABCMeta, abstractmethod


class CaffeeineBeverage():
    __metaclass_ = ABCMeta
    
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addIngredients()
        
    def boilWater(self):
        print('물 끓이는 중')    
    
    def pourInCup(self):
        print('컵에 물 따르는 중')     

    @abstractmethod
    def brew(self):
        pass
    @abstractmethod
    def addIngredients(self):
        pass

class Coffee(CaffeeineBeverage):
    def brew(self):
        print('커피를 내리는 중')

    def addIngredients(self):
        print('설탕과 헤이즐넛을 추가하는 중')

class Tea(CaffeeineBeverage):
    def brew(self):
        print('녹차를 우리는 중')
    def addIngredients(self):
        print('레몬을 넣는 중')


#with Hook
class CaffeeineBeverageWithHook():
    __metaclass_ = ABCMeta
    
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsIngredients() :
            self.addIngredients()
        
    def boilWater(self):
        print('물 끓이는 중')    
    
    def pourInCup(self):
        print('컵에 물 따르는 중')     

    def customerWantsIngredients(self):
        return True
        
    @abstractmethod
    def brew(self):
        pass
    @abstractmethod
    def addIngredients(self):
        pass

class CoffeeWithHook(CaffeeineBeverageWithHook):

    def brew(self):
        print('커피를 내리는 중')
        
        
    def addIngredients(self):
        print('설탕과 헤이즐넛을 추가하는 중')
        
    
    def customerWantsIngredients(self):
        reply = input('커피에 설탕과 헤이즐넛을 추가할까요? (y/n) ')
        if reply == 'y':
            return True
        else:
            return False
    

class TeaWithHook(CaffeeineBeverageWithHook):
        
    def brew(self):
        print('녹차를 우리는 중')
    def addIngredients(self):
        print('레몬을 넣는 중')
    def customerWantsIngredients(self):
        reply = input('녹차에 레몬을 추가할까요? (y/n) ')
        if reply == 'y':
            return True
        else:
            return False
    
        

if __name__ == '__main__' :
    coffee = Coffee()
    coffee.prepareRecipe()
    print()
    
    tea = Tea()
    tea.prepareRecipe()
    print()
    
    coffeHook = CoffeeWithHook()
    coffeHook.prepareRecipe()
    print()
    teaHook = TeaWithHook()
    teaHook.prepareRecipe()
    