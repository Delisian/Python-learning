# stuff = {"chain": 1, "big dick": 0, "arrow": 5}
#
#
def display_inventory(inventory):
    print("Inventory")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))


print("""Create your own inventory!
Firstly input item name, then quantity.
Blank to quit""")
current_inventory = {}

while True:
    print("Item name:")
    item_name = input()
    if item_name == "":
        break
    print("Great! Now enter quantity")
    while True:
        try:
            item_number = int(input())
        except ValueError:
            print("You have to enter number!")
            continue
        break
    current_inventory.setdefault(item_name, item_number)


display_inventory(current_inventory)

