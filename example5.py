#!python3

teachers = {
    "math" : "Dop",
    "science" : "Anderson",
    "english" : "Oliver",
    "pe" : "Gill",
    "compsci" : "Yang",
    "socials" : "Saip",
    "english" : "Westinghouse"
}

print("\n\nWe can use the _in_ operator to check to see if a key exists")
print("Check to see if _math_ is a dictionary key")
if "math" in teachers:
    print(f"math exists in the dictionary with a value of {teachers['math']}")
else:
    print("math is not a dictionary key")

print(f"\nCheck to see if _cafeteria_ is a dictionary key")
if "cafeteria" in teachers:
    print(f"cafeteria exists in the dictionary with a value of {teachers['cafeteria']}")
else:
    print('cafeteria is not a dictionary key')