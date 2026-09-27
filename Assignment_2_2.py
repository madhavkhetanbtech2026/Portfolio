#Grocery Billing System

#stock = {"item": [quantity,price_per_unit]}
stock = {"Rice":[50,100],"Wheat":[25,54],"Sugar":[59,56],"Salt":[24,25],"Banana":[65,56]}

# List to store each bill as a tuple (item_name, quantity, price_per_unit)
bills = []

print("Available items, available quantity and price :")
for item in stock:
    print(item, "-", stock[item][0], "units available and price per unit is :", stock[item][1]  )

n = int(input("How many items do you want to purchase : "))

for i in range(n):
    print("Purchase", i + 1)
    item_name = input("Enter item name : ")

    if item_name in stock:
        quantity = int(input("Enter quantity : "))

        if quantity <= stock[item_name][0]:
            price = stock[item][1]

            bill_entry = (item_name, quantity, price)
            bills.append(bill_entry)

            stock[item_name][0] = stock[item_name][0] - quantity  
            print("Purchase added successfully!")
        else:
            print("Insufficient stock!, Only", stock[item_name], "units available.")
    else:
        print("Item not found in stock.")

print(stock)
print(bills)

print("***********FINAL BILL***********")
total_amount = 0

for entry in bills:
    item_name = entry[0]
    quantity = entry[1]
    price = entry[2]

    amount = quantity * price
    total_amount = total_amount + amount

    print(item_name, "x", quantity, "@", price, "=", amount)

print("Total Bill Amount:", total_amount)


print("Updated Stock:")
for item in stock:
    print(item, "-", stock[item][0], "units remaining")