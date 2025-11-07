## SDSS Computing Studies Python Assignment


Objectives:
* Understand the difference a list and a dictionary
* Create and use dictionary (dict) type variables
* Explore how the "for" command can be used to iterate through a tuple, dict or list
* Understand what is meant by a key,value pair

tuples, lists and dicts are multi value variables.  There is no set number of values that they may store.

Lists:
https://www.w3schools.com/python/python_lists.asp

Tuples:
https://www.w3schools.com/python/python_tuples.asp

Dictionaries:
https://www.w3schools.com/python/python_dictionaries.asp

The examples will show you how you can declare variables of these types and how you can add or retrieve their values.

# Dictionaries
Dictionaries are lists where the indexes or **keys** are not set by their position in the list, but by a defined key.  Consider the code:

```
    names = {
        'first'  : 'Bobby',
        'middle' : 'Ray',
        'last'   : 'Keith' 
    }

```

A dictionary is defined by using {} instead of [].  The dictionariy is sorted into *key* and *value* pairs.  They are accessed like a list:
```
print( names['first'] )
```

Note that a dictionary's keys do not need to be strings, you can also use integer values and we can also mix integer keys with string literal keys, although this is not necessarily a good idea and there is generally a better way to accomplish the same task:
```
inventory =  {
    5 : 20000,
    9 : 1000000,
    19 : 30,
    'none' : 0
}


##### Task 1
Write a python script display the values of the dictionary that are sorted by their keys (ascending values)
(3 points)

##### Task 2
write a python script to use all of the integers from 1-10 as the keys and the squares of those numbers as the values
(2 points)

##### Task 3
Have the user enter in the following information and 
store it into a dictionary.  Use an appropriate key 
for each element of the dictionary.

first name
last name
student number
birthdate
grade
email

Then create a loop to repeatedly ask the user for a key.
If the key is in the dictionary, display the value.
If the user types in "quit" then stop the loop.

##### Task 4
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to make use of the string.split() method in order to separate the item name from the action that precedes it.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

(3 points)


