#!python

# Dictionary Example
# A dictionary is defined using curly brackets, with a key and value pair

teachers = {
    "math" : "Dop",
    "science" : "Anderson",
    "english" : "Oliver",
    "pe" : "Gill",
    "compsci" : "Yang",
    "socials" : "Saip",
    "english" : "Westinghouse"
}

print("\nYou can access a single entry of the dictionary using the named key/index\n")
print(f"teachers[\"math\"] will yield {teachers['math']}")
input("Press enter to continue")

print("\nYou can iterate through a dictionary using a for loop")
print("Note that when you iterate through the loop, the index is stored in your temporary variable")
for i in teachers:
    print("  ",i)
input("Press enter to continue")

print("\nIf you want to access the values of your dictionary with a for loop")
print("you will need to include the key in a reference to the dictionary element")
for i in teachers:
    print(f"  key:{i} and value:{teachers[i]}")




