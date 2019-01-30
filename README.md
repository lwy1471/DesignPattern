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
**Factory Method** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/factory-method/structure-indexed.png">  

**[Examples]**  
Franchise pizza store and its branches.  


## 4. Template method Pattern  
**[INTENT]**  
**Template Method** is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/template-method/structure-indexed.png">  

**[Examples]**  
Skelethon of an algorithm that preparing and drinking caffeine beverages - Coffee, Tea  


## 5. Command Pattern  
**[INTENT]**  
**Command** is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request’s execution, and support undoable operations.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/command/structure-indexed.png">  

**[Examples]**  
Remote controllers that contains all information about home appliances.  


## 6. Adapter Pattern  
**[INTENT]**  
**Adapter** is a structural design pattern that allows objects with incompatible interfaces to collaborate.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/adapter/structure-object-adapter-indexed.png">  

**[Examples]**  
Turkey interface makes the turkey possible to 'quack' which is the duck instacnes could.  


## 7. Facade Pattern  
**[INTENT]**  
**Facade** is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/facade/structure-indexed.png">  

**[Examples]**  
Home-Theater Facade class provides a simplified interface to the home theater stuffs.  


## 8. State Pattern  
**[INTENT]**  
**State** is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/state/structure-indexed.png">  

**[Examples]**  
Audio Player works differently dependion on its states when events are occured.
