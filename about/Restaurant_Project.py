menu = {
    "Small Chicken Pizza": 400,
    "Medium BBQ Pizza": 700,
    "Large Malai Boti Pizza": 1000,
    "Chicken Tikka Burger": 400,
    "Zinger Burger": 400,
    "BBQ Sandwich": 400,
    "Chicken Tikka Sandwich": 400,
    "Club Sandwich": 400,
    "Chicken Tikka Roll": 330,
}

order_total = 0

print("\n>>>  Welcome to Hunger-Byte Restaurant  <<<\n")
print("Please select your order from the following menu\n")
for item, price in menu.items():
    print(f"{item}: {price} PKR")

items = input("\nEnter the item name you want to order: ")
if items in menu:
    quantity = int(input("Enter the quantity: "))
    order_total += menu[items] * quantity
    print(f"Your {items} has been added to your order")
else:
    print(f"Sorry, {items} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No): ")
if another_order == "Yes":
    print("Please select your order from the following menu\n")
    for item, price in menu.items():
        print(f"{item}: {price} PKR")
    items = input("\nEnter the item name you want to order: ")
    if items in menu:
        quantity = int(input("Enter the quantity you want to order: "))
        order_total += menu[items] * quantity
        print(f"Your total bill is {order_total} PKR")
else:
    print(f"Your total bill is {order_total} PKR")
