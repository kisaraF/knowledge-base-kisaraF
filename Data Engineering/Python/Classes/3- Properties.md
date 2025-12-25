# Properties

Properties are like attribute but underneath them, a method is getting invoked. For example, refer to the code piece below,

```python
class Height():
    def __init__(self, feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12
    
    def _set_feet(self, feet):
        self._inches = feet * 12

    feet = property(_get_feet, _set_feet)

h = Height(6)
print(h.feet) # 6.0
h.feet = 5
print(h.feet) # 5.0
```

Here even though at the instantiation, you pass a feet value, inside the class, every transaction is being handled in inches. When you need to retrieve the feet value as retrieving feet as a normal attribute like `h.feet` it refers to the "feet" property. 

The positioning here is important. First it's the getter then the setter. Changing the positions will throw errors.

## Alternate Way (Using Decorators)

```python
class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100
    
    @dollars.setter
    def dollars(self, dollars):
        if dollars > 0:
            self._cents = dollars * 100
    

balance = Currency(100)
print(balance.dollars) # 100.0

balance.dollars = 400
print(balance.dollars) # 400.0
```

This is what's more common on professional code bases. Here we are using `@property` decorator as the "getter". Then setter will be a little bit different at defining by keeping it as `@dollars.setter`. This is the pythonic way of telling that "dollars" is the property and this is the setter.