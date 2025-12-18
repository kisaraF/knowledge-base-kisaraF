# User Defined Exceptions

Sometimes user defined functions are needed when the error cataching is explicit to certain use cases.

For example see the following,

```python
class NegativeNumbersError(Exception):
    """One or more inputs are negative"""

    pass 

def add_positive_numbers(a,b):
    try:
        if a <= 0 or b <=0:
            raise NegativeNumbersError("Shit here we go again!!!")
        else:
            return a + b
    except NegativeNumbersError as err:
        print(f"{err}...Shame on you, not valid... Let me fix it up for you")
        return abs(a) + abs(b)

print(add_positive_numbers(2,-4))
```

Here we are making a sub `exception` class from the base `Exception` class by inheriting. This is why it's getting __pass__ in the class body. 

In other words we are creating a new exception that behaves exactly as an exception but has a different name.

This way we can catch only the necessary errors rather than catching everything. 

Here the `NegativeNumbersError` is actually getting raised in the 14th code cell. The exception is caught at 15th with the __"except"__ keyword.

### Difference between raising vs catching an exception

- __Raising__- reporting that something has gone wrong
- __Catching__- deciding what to do about it