"""
##### Task 4
create a dictionary for an inventory of items in a game.  Ask the user for input, and if the item they choose to 'get item', add that item to their inventory.  If they choose to drop item' remove that item from that invenory.  If they choose 'show inventory' give them a list of the items that they have. You will need to use the string.split() method to separate the command from the item.

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

print("COMMAND LIST:\n>get (amount) (item)\n>drop (amount) (item)\n>inventory\n(leave amount empty if 1)")

while True:
    command = input("Command: ")
    commandList = command.split(" ")

    if commandList[0] == ">get":
        if len(commandList) == 3: #checks to see if the amount is specified in the command
            if commandList[2] in items:#checks to see if the item exists in the list of possible items
                if commandList[2] in inv: #checks to see if the item is already in the inventory
                    inv[commandList[2]] += commandList[1] #if it is then it adds the new amount to the old one in the dictionary
                else:
                    inv[commandList[2]] = commandList[1] #if the item isn't in the inventory then it just creates the item and its amount in the inventory
            else:
                print("Item does not exist")
        if len(commandList) == 2:
            if commandList[1] in items: #checks to see if the item exists in the list of possible items
                if commandList[1] in inv: #checks to see if the item is already in the inventory
                    inv[commandList[1]] += 1 #adds one to the amount if the item already exists in the inventory
                else:
                    inv[commandList[1]] = 1 #if the item isn't in the inventory then it just creates the item and its amount in the inventory
            else:
                print("Item does not exist")
        else:
            print("invalid command")

    elif commandList[0] == ">drop":
        if len(commandList) == 3: #checks to see if the amount is specified in the command
            if commandList[2] in inv: #checks to see if the item is already in the inventory
                inv[commandList[2]] -= commandList[1] #if it is then it removes the amount specified from the dictionary
            else:
                print(f"you dont have any {commandList[2]} to drop")
        if len(commandList) == 2:
            if commandList[1] in items: #checks to see if the item exists in the list of possible items
                if commandList[1] in inv: #checks to see if the item is already in the inventory
                    inv[commandList[1]] += 1 #adds one to the amount if the item already exists in the inventory
                else:
                    inv[commandList[1]] = 1 #if the item isn't in the inventory then it just creates the item and its amount in the inventory
            else:
                print("Item does not exist")
        else:
            print("invalid command")

    elif commandList[0] == ">inventory":
    
    else:
        print("command not recognized")
