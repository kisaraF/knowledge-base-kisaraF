# Classes Overview

When programs grow in size and when you need to represent real world objects in code, the native data structures like strings, lists, etc. are not going to be sufficient. Hence, we would need out own data structures and a way to model these objects of real world into code. That's where OOP shines in.

An object has,
1. Attributes- State of the object/ internal data
2. Methods- Behavior of an object. Also can be instructions that alters the state by modifying attributes

Then what is a __Class__?
- A class is the blueprint for defining those new objects. 

Instances
- Instances are the objects created by a class
- Instantiating is the process of creating an instance from a class

## `__init__` What is it?

This is a dunder method in Python which will instantly assign the attributes passed to an object at the instantiation.

```python
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello {self.name}! You are {self.age} years old"

kisara = Person("kisara", 24)
print(kisara.greet())
print(kisara.age)
```

As the above example, we can use the `__init__` method to instantiate an object and assign the attributes sent as parameters to an object.

### Default Values For Attributes

What if we want to keep a default value for attribute? That's simple and very intuitive

```python
class Book():
    def __init__(self, name, price, issue = 1):
        self.name = name
        self.price = price
        self.issue = issue
    
book_1 = Book("pro git", 29,56)
book_2 = Book("data warehousing toolkit", 34.78, 3) 
```

Here we want to keep most of our book's version as 1. Therefore, rather than having to pass "1" each time at an object instantiation, we can give that as a default value. And if needed (like in `book_2` variable), we can pass a specific version id.