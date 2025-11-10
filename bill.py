#Store Billing System

print("------ Welcome to Store ------")

menu = {
    "Rice": 60,
    "Sugar": 45,
    "Oil": 180,
    "Soap": 40,
    "Tea": 100,
    "Salt": 20,
    "Flour": 55,
    "Milk": 50,
    "Biscuits": 30,
    "Toothpaste": 75,
    "Shampoo": 120,
    "Detergent": 90,
    "Coffee": 150,
    "Dal": 110,
    "Spices": 130
}

print("\nMenu:")
print("--------")
for item in menu:
    print(item, "-", menu[item])
print("----------------")

# Customer details
name = input("\nEnter your name: ")
phone = input("Enter your phone number: ")

total = 0

# Purchase
while True:
    item = input("\nEnter item name (or 'done' to finish): ").capitalize()
    if item == "Done":
        break
    if item in menu:
        qty = int(input("Enter quantity: "))
        total += menu[item] * qty
    else:
        print("Item not found!")

# Bill
print("\n------ BILL ------")
print("Customer Name:", name)
print("Phone Number :", phone)
print("------------------")
print("Total Amount : ₹", total)

if total > 1000:
    discount = total * 0.1
elif total > 500:
    discount = total * 0.05
else:
    discount = 0

final = total - discount
print("Discount     : ₹", discount)
print("Final Amount : ₹", final)
print("------------------")

# Feedback
feedback = input("Please share your feedback: ")
print("\nThanks for visiting Sona Store!")
print("Your feedback:", feedback)
print("------------------------------")
