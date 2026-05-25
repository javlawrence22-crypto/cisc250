# =============================================================================
# Student Name: Javrick Lawrence
# Lab Title: Lab 4 - Food Truck Order Queue
# Date: may 25,2026
# =============================================================================

# Task 1.1: Create two lists
order_queue = []
menu_items = ["burger", "hot dog", "fries", "fried chicken wings", "buffalo wings", "soda", "bottled water", "local drink"]

# Task 1.2: Display a welcome message and create an infinite while loop
print("Welcome to the Food Truck!")
while True:

    # Task 2.1: Setup user input
    print("\nType 'menu' to see the menu or 'done' to complete order:")
    user_input = input("Enter your choice: ").strip().lower()

    # Task 2.2: break out of the loop
    if user_input == 'done':
        break
 
    # Task 2.3
    # If user input is empty press (enter), continue to start of loop
    if user_input == '':
        print("No input detected. Please enter an item.")
        continue
    
    # Handle menu display
    if user_input == 'menu':
        print("\n" + "-" * 30)
        print("MENU:")
        for index, item in enumerate(menu_items, 1):
            print(f"{index}. {item}")
        print("-" * 30)
        continue
    
    # Task 2.4: Check if user input is on the menu.
    if user_input not in menu_items:
        print(f"Invalid choice: '{user_input}' is not on the menu.")
        print("Please choose from the menu or type 'menu' to see options.")
        continue
 
    # Task 2.5 
    # If item is on the menu, find out quantity requested
    while True:
        try:
            # Ask for quantity
            quantity_input = input(f"How many {user_input}(s) would you like? ")
            quantity = int(quantity_input)
            
            # Validate quantity is positive
            if quantity <= 0:
                print("Please enter a positive number (1 or more).")
                continue
            
            # Append item to order queue 
            for i in range(quantity):
                order_queue.append(user_input)
            
            # display that quantity was added
            print(f"✓ Added {quantity} x {user_input} to your order.")
            break  # Exit quantity input loop
            
        except ValueError:
            print("Invalid quantity. Please enter a number!")

# Task 3.1
# Display the order queue to be processed
print("\nORDER SUMMARY")
print("Order queue to be processed:")
if order_queue:
    for item in order_queue:
        print(f"  - {item}")
    print(f"Total items: {len(order_queue)}")
else:
    print("  No items in order queue.")

# Task 3.2
# Process the order queue using another while loop
print("\nPROCESSING ORDERS")

# Loop through the order queue until it is empty
while order_queue:
    # Pop off the first item from the beginning of the list
    current_item = order_queue.pop(0)
    
    # Display which item is being fulfilled and how many remain
    items_remaining = len(order_queue)
    print(f"Fulfilling: {current_item}... ({items_remaining} items remaining in queue)")

# Task 3.3
# Display message that all order entries were fulfilled successfully
print("\n✓ All order entries were fulfilled successfully!")
print("Thank you for using the Food Truck Order System!")