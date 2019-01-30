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

**[Pros and Cons]**  
:sunny: You can swap algorithms used inside an object at runtime.  
:sunny: You can isolate the implementation details of an algorithm from the code that uses it.  
:sunny: You can replace inheritance with composition.  
:sunny: Open/Closed Principle. You can introduce new strategies without having to change the context.  

  
:x: If you only have a couple of algorithms and they rarely change, there’s no real reason to overcomplicate the program with new classes and interfaces that come along with the pattern.  
:x: Clients must be aware of the differences between strategies to be able to select a proper one.  
:x: A lot of modern programming languages have functional type support that lets you implement different versions of an algorithm inside a set of anonymous functions. Then you could use these functions exactly as you’d have used the strategy objects, but without bloating your code with extra classes and interfaces.  

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

**[Pros and Cons]**  
:sunny: Open/Closed Principle. You can introduce new subscriber classes without having to change the publisher’s code (and vice versa if there’s a publisher interface).  
:sunny: You can establish relations between objects at runtime.  
  
:x: Subscribers are notified in random order.  

  
## 3. Decorater method Pattern  
**[INTENT]**  
**Decorator** is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/decorator/structure-indexed.png">  

**[Examples]**  
Franchise pizza store and its branches.  

**[Pros and Cons]**  
:sunny: You can extend an object’s behavior without making a new subclass.  
:sunny: You can add or remove responsibilities from an object at runtime.  
:sunny: You can combine several behaviors by wrapping an object into multiple decorators.  
  
:x: It’s hard to remove a specific wrapper from the wrappers stack.    
:x: It’s hard to implement a decorator in such a way that its behavior doesn’t depend on the order in the decorators stack.    
:x:The initial configuration code of layers might look pretty ugly.  
  
## 4. Factory method Pattern  
**[INTENT]**  
**Factory Method** is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/factory-method/structure-indexed.png">  

**[Examples]**  
Franchise pizza store and its branches.  

**[Pros and Cons]**  
:sunny: You avoid tight coupling between the creator and the concrete products.  
:sunny: Single Responsibility Principle. You can move the product creation code into one place in the program, making the code easier to support.  
:sunny: Open/Closed Principle. You can introduce new types of products into the program without breaking existing client code.  
  
:x: The code may become more complicated since you need to introduce a lot of new subclasses to implement the pattern. The best case scenario is when you’re introducing the pattern into an existing hierarchy of creator classes.  
  
  
## 5. Command Pattern  
**[INTENT]**  
**Command** is a behavioral design pattern that turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request’s execution, and support undoable operations.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/command/structure-indexed.png">  

**[Examples]**  
Remote controllers that contains all information about home appliances.  

**[Pros and Cons]**  
:sunny: Single Responsibility Principle. You can decouple classes that invoke operations from classes that perform these operations.  
:sunny: Open/Closed Principle. You can introduce new commands into the app without breaking existing client code.  
:sunny: You can implement undo/redo.  
:sunny: You can implement deferred execution of operations.  
:sunny: You can assemble a set of simple commands into a complex one.  
  
:x: The code may become more complicated since you’re introducing a whole new layer between senders and receivers.  
  
  
## 6. Adapter Pattern  
**[INTENT]**  
**Adapter** is a structural design pattern that allows objects with incompatible interfaces to collaborate.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/adapter/structure-object-adapter-indexed.png">  

**[Examples]**  
Turkey interface makes the turkey possible to 'quack' which is the duck instacnes could.  

**[Pros and Cons]**  
:sunny: Single Responsibility Principle. You can separate the interface or data conversion code from the primary business logic of the program.  
:sunny: Open/Closed Principle. You can introduce new types of adapters into the program without breaking the existing client code, as long as they work with the adapters through the client interface.  
  
:x: The overall complexity of the code increases because you need to introduce a set of new interfaces and classes. Sometimes it’s simpler just to change the service class so that it matches the rest of your code.  
  
  
## 7. Facade Pattern  
**[INTENT]**  
**Facade** is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/facade/structure-indexed.png">  

**[Examples]**  
Home-Theater Facade class provides a simplified interface to the home theater stuffs.  

**[Pros and Cons]**  
:sunny: You can isolate your code from the complexity of a subsystem.  
 
:x: A facade can become a god object coupled to all classes of an app.  
  
  
## 8. Template method Pattern  
**[INTENT]**  
**Template Method** is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/template-method/structure-indexed.png">  

**[Examples]**  
Skelethon of an algorithm that preparing and drinking caffeine beverages - Coffee, Tea  

**[Pros and Cons]**  
:sunny: You can let clients override only certain parts of a large algorithm, making them less affected by changes that happen to other parts of the algorithm.  
:sunny: You can pull the duplicate code into a superclass.  
  
:x: Some clients may be limited by the provided skeleton of an algorithm.  
:x: You might violate the Liskov Substitution Principle by suppressing a default step implementation via a subclass.  
:x: Template methods tend to be harder to maintain the more steps they have.  
  
  
## 9. State Pattern  
**[INTENT]**  
**State** is a behavioral design pattern that lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/state/structure-indexed.png">  

**[Examples]**  
Audio Player works differently dependion on its states when events are occured.
  
**[Pros and Cons]**  
:sunny: Single Responsibility Principle. Organize the code related to particular states into separate classes.  
:sunny: Open/Closed Principle. Introduce new states without changing existing state classes or the context.  
:sunny: Simplify the code of the context by eliminating bulky state machine conditionals.  
  
:x: Applying the pattern can be overkill if a state machine has only a few states or rarely changes.  
  
  
