# DesignPattern
this repository is the Design Pattern examples. these are Python codes which are interpreted with common Object-oriented languages(ex. Java) and not fit into the Python features.
The references is 
  1. Eric Freeman, and others. [Head First Design Patterns]. O'REILLY, 2005
  2. Refactoring.Guru. https://refactoring.guru/

## 1. Strategy Pattern
**[INTENT]**  
**Strategy** is a behavioral design pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/strategy/structure-indexed.png">  

**[Examples]**  
Diplays and those interfaces 

## 2. Observer Pattern  
**[INTENT]**  
**Observer** is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they’re observing.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/observer/structure-indexed.png">  

**[Examples]**  
Subject class : WeatherData send the weatherr data to the observers.  
Observer class :  
- CurrentCondition receive the data then display current conditions.  
- NextCondition receive the data then predict and display next cunditions.


## 3. Factory method Pattern  
**[INTENT]**  
**Factory** Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/factory-method/structure-indexed.png">  

**[Examples]**  
Franchise pizza store and its branches.
