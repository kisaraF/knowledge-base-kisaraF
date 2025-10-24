# Map Function

Map is a functional programming thing that you can use to do sort of lazy conversions.

For example I have a list of words like this:

```
animals = ["cat", "Bat", "Giraffe", "Bitch", "Pig"]
```

The usual way to make a list of each word's length would be:

```
animals_len = [len(i) for i in animals]
```

But with `map` functions we can make an iterable object like below:

```
animals_len = map(len, animals)
```

Here `len` is a buit-in function. So it can be used to pass as a straight argument.

Moreover, we can use custom function like below as well

```
def greet_animals(animal):
    return f"Hello cute {animal}"
```

```
animals_greet = map(greet_animals, animals)
```