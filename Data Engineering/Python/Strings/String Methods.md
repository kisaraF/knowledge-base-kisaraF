# String Methods


## Capitalize(), Title(), Swapcase()

```python
my_str = 'once upon a time there was a man'

print(my_str.capitalize()) # only make the first letter capital (Once upon a time there was a man) 
print(my_str.title()) # every first letter of each word is capital (Once Upon A Time...)
print(my_str.swapcase()) # make the lowercase captial and uppercase simple
```

## Cleaning Strings

```python
whitespace_str = '     hello   '
print(whitespace_str.lstrip()) # Remove whitespace from the left side. Same for rstrip
print(whitespace_str.strip()) # Removes all the whitespace

website = 'www.helloi.org'

print(website.lstrip("w")) # will take off the "w"s to the left of the string. Same for rstrip
print(website.strip("worg."))
```


## Replacing strings

```python
phone_no = '075 277 3615'
print(phone_no.replace(" ", "-"))
```


## Using .format() function

```python
mad_libs = "{txt_1} laughed at the {txt_2} {txt_3}."
mad_libs_2 = "{} laughed at the {} {} {}."

print(mad_libs.format(txt_1= "Kisara", txt_2= "Cake made by", txt_3= "Sayuni"))
print(mad_libs.format(txt_3= "Kisara", txt_2= "Cake made by", txt_1= "Sayuni"))
print(mad_libs_2.format("Clark Kent", "Statement made by", "Bruce Wayne", "on beating him", "in a fist fight"))
```

* Now with new Python versions, `fstrings` are best used instead of `.format()`. It provides cleanliness and verbosity for the code being written.