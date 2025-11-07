#!python3

"""
Write a python script display the values of the dictionary
  1. that are sorted by their keys (ascending values) 
  2. that are sorted by their values (ascending) 
Note: You are not actually sorting the dictionary, but creating a new list from the values, and
sorting those
(3 points)
"""
sortMe = {
    1: -2, 
    2: 6, 
    4: 0, 
    11: 0, 
    6: 1, 
    10: 3, 
    9: 2, 
    13: 3, 
    14: 4, 
    15: -2, 
    17: 0, 
    18: -1, 
    20: 3
  }

keys = []
values = []



assert keys == [1, 2, 4, 6, 9, 10, 11, 13, 14, 15, 17, 18, 20]
assert values == [-2, -2, -1, 0, 0, 0, 1, 2, 3, 3, 3, 4, 6]