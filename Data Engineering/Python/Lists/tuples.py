address = (
    ['Street 1', "Area 1", "Coe 1"],
    ['Street 2', "Area 2", "Coe 2"],
    ['Street 3', "Area 3", "Coe 3"]
)

print(address)

address[0].append("New_element")
print(address)


# ------ Unpacking a tuple
employee = ("Kisara", "Fernando", "Associate Data Engineer", 24)

fname, lname, title, age = employee
print(fname, lname, title, age)

fname, lname, title = employee[:-1]
print(fname, lname, title)

fname, lname , *title = employee # This will store the extra values as a list in the last variable given
print(fname, lname, title)

*fname, lname , title = employee # Positioning is key
print(fname, lname, title)

fname, *lname , title = employee # Positioning is key
print(fname, lname, title)


# ------  Use of *args  ------

# Use to collect any number of arguments to a function and to return it as a tuple object
def accept_stuff(*args): # args is just a general name. Can use anything you want
    print(type(args))
    print(args)

accept_stuff(1,2,3,4,5,6,7,8,9)