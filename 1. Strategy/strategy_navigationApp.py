'''
    Strategy Pattern : Navigation Application

'''

from abc import ABC, abstractmethod


class Navigator():
    def __init__(self):
        self.route = None
    
    def setRouteStrategy(self, route):
        self.route = route
    def getRoute(self):
        self.route.routesPlan()
        self.route.time()
    
    def displayMap(self):
        print('Diplay Map')
    def displayVelocity(self):
        print('60km/h')
        

class RoutesStrategy(ABC):
    @abstractmethod
    def routesPlan(self):
        pass
    @abstractmethod
    def time(self):
        pass
        
class WalkingStrategy(RoutesStrategy):
    def routesPlan(self):
        print('This is walking routes')
    def time(self):
        print('It takes 120 minutes')

class RoadStrategy(RoutesStrategy):
    def routesPlan(self):
        print('This is Road routes')
    def time(self):
        print('It takes 10 minutes')

class PublicTransportStrategy(RoutesStrategy):
    def routesPlan(self):
        print('This is Public Transport routes')
    def time(self):
        print('It takes 20 minutes')
        
        
        
if __name__ == '__main__':
    navi = Navigator()
    navi.displayMap()
    navi.displayVelocity()
    
    print('---asking Walking routes---')
    navi.setRouteStrategy(WalkingStrategy())
    navi.getRoute()
    
    print('---asking RoadStrategy---')
    navi.setRouteStrategy(RoadStrategy())
    navi.getRoute()
    
    print('---asking Public transport routes---')
    navi.setRouteStrategy(PublicTransportStrategy())
    navi.getRoute()