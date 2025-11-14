#!python3
"""
##### Task 4
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to use the string.split() method to separate the command from the item.

Possible extensions:
* nicer format for displaying inventory
* use shortened/abbreviated names for items (recognizing first few characters or spelling errors)

possible items:
food
water
rope
torch
sack
wood
iron
steel
ginger
garlic
fish
stone
wool

example:
>get food
>get water
>get water
>get iron
>get 3 wood
>inventory
You have:
 1 food
 2 water
 1 iron
 3 wood
 >
"""

inv = {}
items = ["food", "water", "rope", "torch", "sack", "wood", "iron", "steel", "ginger", "garlic", "fish", "stone", "wool"]
BOLD = '\033[1m'
END = '\033[0m'

print("Type \"help\" for a list of commands")

while True:
    command = input("Command: ")
    commandList = command.split(" ")

    if commandList[0] == "get" or commandList[0] == "Get":
        if len(commandList) == 3: #checks to see if the amount is specified in the command
            if commandList[2] in items:#checks to see if the item exists in the list of possible items
                if commandList[2] in inv: #checks to see if the item is already in the inventory
                    try:
                        if int(commandList[1]) > 999:
                            print(f"Limit reached: Got {999 - inv[commandList[2]]} {commandList[2]}") 
                            inv[commandList[2]] = 999 #for formatting makes sure that number doesnt go too high
                        else:
                            inv[commandList[2]] += int(commandList[1]) #if it is then it adds the new amount to the old one in the dictionary
                            print(f"Got {commandList[1]} {commandList[2]}")
                    except:
                        print("Invalid amount")
                else:
                    try:
                        if int(commandList[1]) > 999:
                            print(f"Limit reached: Got 999 {commandList[2]}")
                            inv[commandList[2]] = 999
                        else:
                            inv[commandList[2]] = int(commandList[1]) #if the item isn't in the inventory then it just creates the item and its amount in the inventory
                            print(f"Got {commandList[1]} {commandList[2]}")
                    except:
                        print("Invalid amount")
            else:
                print("Item does not exist")
        elif len(commandList) == 2:
            if commandList[1] in items: #checks to see if the item exists in the list of possible items
                if commandList[1] in inv: #checks to see if the item is already in the inventory
                    if inv[commandList[1]] == 999:
                        print(f"Limit reached: got 0 {commandList[1]}")
                    else:
                        inv[commandList[1]] += 1 #adds one to the amount if the item already exists in the inventory
                        print(f"Got 1 {commandList[1]}")
                else:
                    inv[commandList[1]] = 1 #if the item isn't in the inventory then it just creates the item and its amount in the inventory
                    (f"Got 1 {commandList[1]}")
            else:
                print("Item does not exist")
        else:
            print("invalid command")

    elif commandList[0] == "drop" or commandList[0] == "Drop":
        if len(commandList) == 3: #checks to see if the amount is specified in the command
            if commandList[2] in inv: #checks to see if the item is in the inventory
                try:
                    if int(commandList[1]) <= inv[commandList[2]]: #Checks to see if the amount dropped is more than the amount owned
                        inv[commandList[2]] -= int(commandList[1]) #if it is in inventory then it removes the amount specified from the dictionary
                        print(f"Dropped {commandList[1]} {commandList[2]}")
                        if inv[commandList[2]] < 1:
                            del inv[commandList[2]]
                    else:
                        print(f"You don't have that many {commandList[2]} to drop")
                except:
                    print("Invalid amount")
            else:
                print(f"you dont have any {commandList[2]} to drop")
        elif len(commandList) == 2:
            if commandList[1] in items: #checks to see if the item exists in the list of possible items
                if commandList[1] in inv: #checks to see if the item is in the inventory
                    if inv[commandList[1]] >= 1:
                        inv[commandList[1]] -= 1 #removes one of the item from the inventory
                        print(f"Dropped 1 {commandList[1]}")
                        if inv[commandList[1]] < 1:
                            del inv[commandList[1]] #removes the item from the dictionary if the value is below 1
                    else:
                        print(f"You don't have that many {commandList[1]} to drop")
                else:
                    print(f"you dont have any {commandList[1]} to drop")
            else:
                print("Item does not exist")
        else:
            print("invalid command")

    elif commandList[0] == "inventory" or commandList[0] == "Inventory" or commandList[0] == "inv" or commandList[0] == "Inv":
        if len(inv) == 0:
            print("You have nothing in your inventory")
        else:
            print(f"---------------\n|  {BOLD + 'Inventory' + END}  |")
            for i in items:
                if i in inv:
                    print(f"|{(f'{i}: {inv[i]}'):^{13}}|")
            print("---------------")
    
    elif commandList[0] == "help" or commandList[0] == "Help":
        print(f"{BOLD + 'COMMAND LIST' + END}\nget (amount) (item)\ndrop (amount) (item)\ninventory\nend\n(leave amount empty if 1)")

    elif commandList[0] == "end" or commandList[0] == "End":
        print("quitting...")
        break
    
    else:
        print("command not recognized")

''' 
for this extenstion, I formatted the inventory output
I also limited the get command to not allow the amount of an item to pass 999
this is also for formatting reasons so that the inventory format isnt destroyed when a number too big is added
Another thing I added was a try except block to make sure that the amount that was inputted is an integer amount and wont crash the program
I also added an end feature so that the user can quit out whenever wanted
'''
