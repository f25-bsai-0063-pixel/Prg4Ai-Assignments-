def Cal_Bill(products):
    bill = 0
    for p in products:
        p["total"] = p["price"] * p["quantity"]
        bill += p["total"]
    
    discount = 0
    if bill > 10000:
        discount = bill * 0.10
    final_bill = bill - discount
    return bill, discount, final_bill
 
products = []

for i in range(5):
    print(f"\n--- Product {i + 1} ---")
    name = input("Product name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    products.append({"name": name, "price": price, "quantity": quantity})
 
bill, discount, final_bill = Cal_Bill(products)
 
expensive = products[0]
for p in products:
    if p["price"] > expensive["price"]:
        expensive = p

print("\n-----BILL-----")
for p in products:
    print(p["name"], "x", p["quantity"], "for Rs.", p["price"], "= Rs.", p["total"])
print("Total bill: Rs.", bill)
print("Discount: Rs.", discount)
print("Final bill: Rs.", final_bill)
print("Most expensive:", expensive["name"])

 
with open("bill.txt", "w") as f:
    for p in products:
        f.write(p["name"] + " x " + str(p["quantity"]) + " = Rs. " + str(p["total"]) + "\n")
    f.write("Total: Rs. " + str(bill) + "\n")
    f.write("Discount: Rs. " + str(discount) + "\n")
    f.write("Final Bill: Rs. " + str(final_bill) + "\n")
    f.write("Most expensive: " + expensive["name"] + "\n")

