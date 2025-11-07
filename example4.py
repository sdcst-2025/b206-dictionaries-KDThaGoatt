#!python3

# Adding onto a dictionary

teachers = {}

print(teachers)
print("To add onto a dictionary, you can just assign a value")
teachers["math"] = "Yang"
teachers["french"] = "Turgeon"
print(teachers)

input("\nPress Enter to Continue")
print("\nTo remove an entry from a dictionary, we can do one of 2 things:")
print("We can use the del command (it is not a function)")
del teachers["math"]
print("Or we can use the .pop() method")
teachers.pop('french')
print(teachers)

