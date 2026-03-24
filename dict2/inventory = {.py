inventory = {
    "apple": {"price": 50, "qty": 10},
    "banana": {"price": 20, "qty": 25},
    "orange": {"price": 40, "qty": 15}
}

bill = {}
for item, details in inventory.items():
    cost = details["price"] * details["qty"]
    bill[item] = cost

total = sum(bill.values())

for item in bill:
    print(item, bill[item])

print("Total:", total)