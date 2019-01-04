from abc import ABCMeta, abstractmethod
from time import sleep

class Subject:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def registerObserver(self, o):
        pass
        
    @abstractmethod
    def removeObserver(self, o):
        pass
    
    @abstractmethod
    def notifyObserver(self, o):
        pass
        
        
class Observer:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def update(temp, humidity, pressure):
        pass

        

class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = None
        self.humidity = None
        self.pressure = None
    
    def registerObserver(self, o):
        self.observers.append(o)
        
    def removeObserver(self, o):
        observers.remove(o)
        
    def notifyObserver(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
        
    
    def measurementsChanged(self):
        self.notifyObserver()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()
        

class CurrentCondition(Observer):
    
    def __init__(self, weatherData):
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()
        
    def display(self):
        print("Current conditions: " + str(self.temperature) + "F degrees and " + str(self.humidity) + "% humidity")


class NextCondition(Observer):
    
    def __init__(self, weatherData):
        self.weatherData = weatherData
        weatherData.registerObserver(self)
    
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()
        
    def display(self):
        print("Next conditions: " + str(self.temperature+10) + "F degrees and " + str(self.humidity+10) + "% humidity")
        
        
        
if __name__ == '__main__':
    weatherData = WeatherData()
    currentCondition = CurrentCondition(weatherData)
    nextCondition = NextCondition(weatherData)
    weatherData.setMeasurements(82, 70, 29.1)
    sleep(0.5)
    weatherData.setMeasurements(42, 50, 30.1)
    