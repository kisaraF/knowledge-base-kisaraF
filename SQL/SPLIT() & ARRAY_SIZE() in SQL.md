# SPLIT() & ARRAY_SIZE() in SQL

## SPLIT()

Can be used to split any string by a given delimiter

### Syntax:

```
SPLIT(*string*, *delimiter*)
```

### Example:

```
select SPLIT('My name is Joe Black!', ' '); 

/* 
Result: 
[
  "My",
  "name",
  "is",
  "Joe",
  "Black!"
]
*/
```

## ARRAY_SIZE()

Can be used to get the array's size of a given array

### Syntax:

```
ARRAY_SIZE(*array*)[*indice*]
```
- Indice is optional

### Example:

```
select SPLIT('My name is Joe Black!', ' ')[array_size(SPLIT('My name is Joe Black!', ' '))-1];

/* 
Result: 
"Black!"
*/
```