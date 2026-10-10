MENU = {
    1: {"name": "Burger", "price": 500},
    2: {"name": "Pizza", "price": 800},
    3: {"name": "Fries", "price": 250},
    4: {"name": "Drink", "price": 150}
}

def Show():
    print("\n-----MENU-----")
    for number, item in MENU.items():
        print(number, ".", item["name"], "for Rs.", item["price"])
 
def Total(order):
    total = 0
    for i in order:
        total += i["subtotal"]
    return total
 
order = []

while True:
    Show()
    choice = int(input("Select item number: "))
    if choice in MENU:
        qty = int(input("Quantity: "))
        subtotal = MENU[choice]["price"] * qty

        order.append({"name": MENU[choice]["name"], "qty": qty, "subtotal": subtotal})

    else:
        print("Invalid choice!")
 
    more = input("Order more items? (yes/no): ")
    if more.lower() != "yes":
        break
 
total = Total(order)
 
print("\n----FINAL BILL-----")
for o in order:
    print(o["name"], "x", o["qty"], "= Rs.", o["subtotal"])
print("Total: Rs.", total)
 
with open("orders.txt", "a") as f:      
    for o in order:
        f.write(o["name"] + " x " + str(o["qty"]) + " = Rs. " + str(o["subtotal"]) + "\n")
    f.write("Total: Rs. " + str(total) + "\n" + "-" * 20 + "\n")
