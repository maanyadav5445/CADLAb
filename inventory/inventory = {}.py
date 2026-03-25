inventory = {}

def add_item():
    name = input()
    qty = int(input())
    price = int(input())
    inventory[name] = {"qty": qty, "price": price}

def update_item():
    name = input()
    if name in inventory:
        qty = int(input())
        price = int(input())
        inventory[name]["qty"] = qty
        inventory[name]["price"] = price

def delete_item():
    name = input()
    if name in inventory:
        del inventory[name]

def sell_item():
    name = input()
    qty = int(input())
    if name in inventory and inventory[name]["qty"] >= qty:
        inventory[name]["qty"] -= qty

def show_inventory():
    for k, v in inventory.items():
        print(k, v["qty"], v["price"])

while True:
    choice = input()
    if choice == "1":
        add_item()
    elif choice == "2":
        update_item()
    elif choice == "3":
        delete_item()
    elif choice == "4":
        sell_item()
    elif choice == "5":
        show_inventory()
    elif choice == "6":
        break