# Map Function

Map is a functional programming thing that you can use to do sort of lazy conversions.

For example I have a list of words like this:

```python
animals = ["cat", "Bat", "Giraffe", "Bitch", "Pig"]
```

The usual way to make a list of each word's length would be:

```python
animals_len = [len(i) for i in animals]
```

But with `map` functions we can make an iterable object like below:

```python
animals_len = map(len, animals)
```

Here `len` is a buit-in function. So it can be used to pass as a straight argument.

Moreover, we can use custom function like below as well

```python
def greet_animals(animal):
    return f"Hello cute {animal}"
```

```python
animals_greet = map(greet_animals, animals)
```