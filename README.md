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
1. The Context maintains a reference to one of the concrete strategies and communicates with this object only via the strategy interface.  
2. The Strategy interface is common to all concrete strategies. It declares a method the context uses to execute a strategy.  
3. Concrete Strategies implement different variations of an algorithm the context uses.  
4. The context calls the execution method on the linked strategy object each time it needs to run the algorithm. The context doesn’t know what type of strategy it works with or how the algorithm is executed.  
5. The Client creates a specific strategy object and passes it to the context. The context exposes a setter which lets clients replace the strategy associated with the context at runtime.

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
1. The Publisher issues events of interest to other objects. These events occur when the publisher changes its state or executes some behaviors. Publishers contain a subscription infrastructure that lets new subscribers join and current subscribers leave the list.  
2. When a new event happens, the publisher goes over the subscription list and calls the notification method declared in the subscriber interface on each subscriber object.  
3. The Subscriber interface declares the notification interface. In most cases, it consists of a single update method. The method may have several parameters that let the publisher pass some event details along with the update.  
4. Concrete Subscribers perform some actions in response to notifications issued by the publisher. All of these classes must implement the same interface so the publisher isn’t coupled to concrete classes.  
5. Usually, subscribers need some contextual information to handle the update correctly. For this reason, publishers often pass some context data as arguments of the notification method. The publisher can pass itself as an argument, letting subscriber fetch any required data directly.  
6. The Client creates publisher and subscriber objects separately and then registers subscribers for publisher updates.  

**[Examples]**  
Subject class : WeatherData send the weatherr data to the observers.  
Observer class :  
- CurrentCondition receive the data then display current conditions.  
- NextCondition receive the data then predict and display next cunditions.

**[Pros and Cons]**  
:sunny: Open/Closed Principle. You can introduce new subscriber classes without having to change the publisher’s code (and vice versa if there’s a publisher interface).  
:sunny: You can establish relations between objects at runtime.  
  
:x: Subscribers are notified in random order.  

  
## 3. Decorater Pattern  
**[INTENT]**  
**Decorator** is a structural design pattern that lets you attach new behaviors to objects by placing these objects inside special wrapper objects that contain the behaviors.

**[STRUCTURE]**  
<img src="https://refactoring.guru/images/patterns/diagrams/decorator/structure-indexed.png">  
1. The Component declares the common interface for both wrappers and wrapped objects.  
2. Concrete Component is a class of objects being wrapped. It defines the basic behavior, which can be altered by decorators.  
3. The Base Decorator class has a field for referencing a wrapped object. The field’s type should be declared as the component interface so it can contain both concrete components and decorators. The base decorator delegates all operations to the wrapped object.  

4. Concrete Decorators define extra behaviors that can be added to components dynamically. Concrete decorators override methods of the base decorator and execute their behavior either before or after calling the parent method.  
5. The Client can wrap components in multiple layers of decorators, as long as it works with all objects via the component interface.  


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
1. The Product declares the interface, which is common to all objects that can be produced by the creator and its subclasses.  
2. Concrete Products are different implementations of the product interface.  
3. The Creator class declares the factory method that returns new product objects. It’s important that the return type of this method matches the product interface.  
You can declare the factory method as abstract to force all subclasses to implement their own versions of the method. As an alternative, the base factory method can return some default product type.  
Note, despite its name, product creation is not the primary responsibility of the creator. Usually, the creator class already has some core business logic related to products. The factory method helps to decouple this logic from the concrete product classes. Here is an analogy: a large software development company can have a training department for programmers. However, the primary function of the company as a whole is still writing code, not producing programmers.
4. Concrete Creators override the base factory method so it returns a different type of product.  
Note that the factory method doesn’t have to create new instances all the time. It can also return existing objects from a cache, an object pool, or another source.




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
1. The Sender class (aka invoker) is responsible for initiating requests. This class must have a field for storing a reference to a command object. The sender triggers that command instead of sending the request directly to the receiver. Note that the sender isn’t responsible for creating the command object. Usually, it gets a pre-created command from the client via the constructor.  
2. The Command interface usually declares just a single method for executing the command.  
3. Concrete Commands implement various kinds of requests. A concrete command isn’t supposed to perform the work on its own, but rather to pass the call to one of the business logic objects. However, for the sake of simplifying the code, these classes can be merged.  Parameters required to execute a method on a receiving object can be declared as fields in the concrete command. You can make command objects immutable by only allowing the initialization of these fields via the constructor.  
4. The Receiver class contains some business logic. Almost any object may act as a receiver. Most commands only handle the details of how a request is passed to the receiver, while the receiver itself does the actual work.  
5. The Client creates and configures concrete command objects. The client must pass all of the request parameters, including a receiver instance, into the command’s constructor. After that, the resulting command may be associated with one or multiple senders.  

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
1. The Class Adapter doesn’t need to wrap any objects because it inherits behaviors from both the client and the service. The adaptation happens within the overridden methods. The resulting adapter can be used in place of an existing client class.  

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
1. The Facade provides convenient access to a particular part of the subsystem’s functionality. It knows where to direct the client’s request and how to operate all the moving parts.  
2. An Additional Facade class can be created to prevent polluting a single facade with unrelated features that might make it yet another complex structure. Additional facades can be used by both clients and other facades.  
3. The Complex Subsystem consists of dozens of various objects. To make them all do something meaningful, you have to dive deep into the subsystem’s implementation details, such as initializing objects in the correct order and supplying them with data in the proper format.  
Subsystem classes aren’t aware of the facade’s existence. They operate within the system and work with each other directly.  
4. The Client uses the facade instead of calling the subsystem objects directly.  

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
1. The Abstract Class declares methods that act as steps of an algorithm, as well as the actual template method which calls these methods in a specific order. The steps may either be declared abstract or have some default implementation.  
2. Concrete Classes can override all of the steps, but not the template method itself.  

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
1. Context stores a reference to one of the concrete state objects and delegates to it all state-specific work. The context communicates with the state object via the state interface. The context exposes a setter for passing it a new state object.  
2. The State interface declares the state-specific methods. These methods should make sense for all concrete states because you don’t want some of your states to have useless methods that will never be called.  
3. Concrete States provide their own implementations for the state-specific methods. To avoid duplication of similar code across multiple states, you may provide intermediate abstract classes that encapsulate some common behavior.  
State objects may store a backreference to the context object. Through this reference, the state can fetch any required info from the context object, as well as initiate state transitions.  
4. Both context and concrete states can set the next state of the context and perform the actual state transition by replacing the state object linked to the context.  

**[Examples]**  
Audio Player works differently dependion on its states when events are occured.
  
**[Pros and Cons]**  
:sunny: Single Responsibility Principle. Organize the code related to particular states into separate classes.  
:sunny: Open/Closed Principle. Introduce new states without changing existing state classes or the context.  
:sunny: Simplify the code of the context by eliminating bulky state machine conditionals.  
  
:x: Applying the pattern can be overkill if a state machine has only a few states or rarely changes.  
  
  
