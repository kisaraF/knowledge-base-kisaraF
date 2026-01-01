# Static Methods

Static methods are like helper functions. The are not bound by the class or instances of the class. And they can be used outside the class without invoking class instances as well. 

```python
class Temperature:
    def __init__(self, temperature):
        self.temperature = temperature

    @staticmethod
    def to_celcius(temp):
        cel_temp = (5/9) * (temp - 32)
        return round(cel_temp,2)

    def fahr_to_celcius(self):
        return [self.to_celcius(i) for i in self.temperature]


today_temperature = Temperature([100])
print(today_temperature.temperature) # [100]

print(today_temperature.fahr_to_celcius()) # [37.78]

print(Temperature.to_celcius(150)) # 65.56
```

