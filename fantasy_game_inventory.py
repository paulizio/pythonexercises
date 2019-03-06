def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        # FILL IN THE CODE HERE
        print(str(v)+' '+k)
        item_total+=v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    # your code goes here
    for i in addedItems:
        inventory[i]=inventory.setdefault(i,0)
        inventory[i]=inventory[i]+1
     
    
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
addToInventory(inv, dragonLoot)
displayInventory(inv)


