# Class Instance Methods

Class instance methods are nothing but function blocks that describes the behavior or certain actions that the object has/ can perform. For example, look at the below,

```python
class Pokemon():
    def __init__(self, name:str, specialty:str, health:int=100):
        self.name = name
        self.specialty = specialty
        self.health = health

    def roar(self) -> str: 
        return f"I am {self.name}"
    
    def take_damage(self, amount:int) -> int:
        if self.health > 0 and self.health - amount < 0:
            self.health = 0
        elif self.health > 0:
            self.health -= amount
        else:
            self.health = 0
    
squirtle = Pokemon("squirtle", "water")
charmander = Pokemon("charmander", "fire", 120)

print(charmander.roar()) # "I am charmander"
print(charmander.health) # 120
charmander.take_damage(27) 
print(charmander.health) # 93
charmander.take_damage(89)
print(charmander.health) # 4
charmander.take_damage(56)
print(charmander.health) # 0
charmander.take_damage(23)
print(charmander.health) # 0
```

# Encapsulation

Encapsulation is whenever we want to make sure a certain attribute or a method is hidden from the public use in order to keep it constant and not to pollute it through altering it's values. If in case altering is needed, it should __only__ be done through a method. Take a look at the code below:

```python
class Smartphone():
    def __init__(self):
        self._comapny = "Apple"
        self._firmware = 10.0

    def get_os_version(self):
        return self._firmware
    
    def update_os(self):
        self._firmware+=1

iphone = Smartphone()
print(iphone._comapny) # Apple
print(iphone._firmware) # 10.0

print(iphone.get_os_version()) # 10.0
iphone.update_os()
print(iphone.get_os_version()) # 11.0
```

Python is considered as a __parent consent__ language. Meaning, even though private variables are created, the Python interpreter only sees the underscore just as another character only. It's up to the developer to adhere to the best practices.