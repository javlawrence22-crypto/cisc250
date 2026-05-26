# =============================================================================
# Student Name: Javrick Lawrence
# Lab Title: Lab 4 - Food Truck Order Queue
# Date: may 25,2026
# =============================================================================

# Food truck items
menu_items = ["burger", "hot dog", "fries", "fried chicken wings", "buffalo wings", "soda", "bottled water", "local drink"]

# List to store customer orders
order_queue = []

print("Welcome to the Food Truck!")

# Keep running until customer types doneme
while True:

    print("\nType 'menu' to see what we have.")
    print("Type 'done' if you are finished ordering.")

    choice = input("What would you like? ").strip().lower()

    # End program
    if choice == "done":
        print("\nFinishing your order...")
        break

    # Empty input
    if choice == "":
        print("You didn't type anything.")
        continue

    # Show menu
    if choice == "menu":

        print("\nToday's Menu")

        for item in menu_items:
            print("-", item)

        continue

    # Check if item exists
    if choice not in menu_items:
        print("Sorry, we don't have that item.")
        continue

    # Ask for quantity
    while True:

        amount = input(f"How many {choice} would you like? ")

        try:
            amount = int(amount)

            if amount <= 0:
                print("Please enter a number greater than 0.")
                continue

            # Add items to queue
            for i in range(amount):
                order_queue.append(choice)

            print(f"{amount} {choice}(s) added to your order.")
            break

        except ValueError:
            print("Please enter a valid number.")

# Show order summary
print("\nYour Order")

if order_queue:

    for item in order_queue:
        print("-", item)

    print(f"\nTotal items: {len(order_queue)}")

else:
    print("No items were ordered.")

# Process orders
print("\nPreparing Orders...\n")

while order_queue:

    current_item = order_queue.pop(0)

    print(f"Preparing {current_item}...")
    print(f"Items left: {len(order_queue)}\n")

print("All orders completed!")
print("Thanks for ordering from the Food Truck!")