# Class Instances & Attributes

So far what was discussed were instance level attributes and methods.
In instance, attributes were descriptive qualities of how an instance should be and methods were how the state/ behavior was changed.

Apart from instances, we can do the same for classes as well. So class methods, change the state of class level attributes.

__When to use class attributes and methods?__

- When you need a class level/ higher level of attributes without being instance level

Pay attention to the below code piece

```python
# Define a Chocolate class that accepts and assigns a cacao_content attribute.

# Define a "sweet" class method that returns a 
# Chocolate object with a cacao_content value of 30.

# Define a "semisweet" class method that returns a 
# Chocolate object with a cacao_content value of 50.

# Define a "bittersweet" class method that returns a 
# Chocolate object with a cacao_content value of 70.

# Define a "bitter" class method that returns a 
# Chocolate object with a cacao_content value of 99.

class Chocolate():
    instance_count = 0 # a class level attribute

    def __init__(self, cacao_content):
        Chocolate.instance_count += 1 # each time at instantiation this increases
        self.cacao_content = cacao_content

    @classmethod
    def sweet(cls): # takes class as a parameter
        return cls(30) # sets the instance attribute to a default value

    @classmethod
    def bittersweet(cls):
        return cls(50)

    @classmethod
    def bitter(cls):
        return cls(99)


print(Chocolate.instance_count) # 0

toblerone = Chocolate(40)
print(toblerone.cacao_content) # 40
print(Chocolate.instance_count) # 1

mars = Chocolate.sweet()
print(mars.cacao_content) # 30
print(Chocolate.instance_count) # 2

revello_dark = Chocolate.bittersweet()
print(revello_dark.cacao_content) # 50

roccoa = Chocolate(25)
print(roccoa.cacao_content) # 25

print(Chocolate.instance_count) #4
print(revello_dark.instance_count) #4
```

In this code snippet the class attribute `instance_count` is being used keep track of how many instances are created with this class. And to determine these class attributes are not being modified at instance level pay attention to the last line. `revello_dark` was created way earlier but still refers to the updated, exact count since it's modified at class level.

Class methods can be used to set a pre-configured instance of the same class.

More reading can be done in [this](https://pynative.com/python-class-method/) article