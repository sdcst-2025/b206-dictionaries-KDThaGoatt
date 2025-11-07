"""
Task 3
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
"""

student = {}

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
stuNum = input("Enter your student number: ")
birthDate = input("Enter your birth date: ")
grade = input("Enter your grade: ")
email = input("Enter your email: ")

student["First Name"] = firstName
student["Last Name"] = lastName
student["Student Number"] = stuNum
student["Birth Date"] = birthDate
student["Grade"] = grade
student["Email"] = email

while True:
    key = input("Please enter a key: ")
    if key in student:
        print(student[key])
    elif key == "quit" or key == "Quit":
        print("quitting...")
        break
    else:
        print("Invalid input (try capitalizing the first letter of the words in the key)")
        True