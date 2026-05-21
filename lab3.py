# =============================================================================
# Student Name: [Your Name]
# Lab Title: Invoice Creator
# Date: [Current Date]
# =============================================================================

# TASK 1: Nesting - Create a dictionary of dictionaries of the products being 
# purchased. Complete the nested dictionary below with the data in the lab 
# table.
product_list = {
    "el2234" : { 
        "name" : "Head Phones",           # Product name
        "category" : "Electronics",       # Product category
        "price" : 19.99,                  # Unit price in USD
        "quantity" : 2                    # Quantity ordered
        },
    "sh9989" : {
        "name" : "Running Shoes",         # Product name
        "category" : "Footwear",          # Product category
        "price" : 99.99,                  # Unit price in USD
        "quantity" : 2                    # Quantity ordered
        },
    "ap0098" : {
        "name" : "Smart Toaster",         # Product name
        "category" : "Appliance",         # Product category
        "price" : 130.00,                 # Unit price in USD
        "quantity" : 1                    # Quantity ordered
        },
    "cl3321" : {
        "name" : "Cotton Shirt",          # Product name
        "category" : "Clothing",          # Product category
        "price" : 10.00,                  # Unit price in USD
        "quantity" : 4                    # Quantity ordered
        },
    }

# Task 2.1: Create a dictionary to hold the customer data
# Create dictionary with customer name and loyalty tier
customer_data = {
    "name": "Hannah Davis",               # Customer full name
    "tier": "Gold"                        # Customer loyalty tier
}

# Task 2.2: Print a processing order statement using an f string
# Use f-string to format and print the processing message with customer info
print(f"Processing Order for: {customer_data['name']} [{customer_data['tier']} Tier Member]...")

# Task 3: Loop through dictionary with match-case discount calculations
# Initialize running total after all discounts (for Task 4)
total_after_discounts = 0

# Loop through each product in the product_list dictionary
for product_id, product_info in product_list.items():
    # Extract product details from the nested dictionary
    product_name = product_info["name"]         # Get product name
    category = product_info["category"]         # Get product category
    unit_price = product_info["price"]          # Get unit price
    quantity = product_info["quantity"]         # Get quantity ordered
    
    # Calculate subtotal (unit price * quantity)
    subtotal = unit_price * quantity
    
    # Use match-case to determine product discount percentage based on category
    match category:
        case "Appliance":                       # 20% discount on Appliances
            discount_percent = 0.20
        case "Clothing":                        # 10% discount on Clothing
            discount_percent = 0.10
        case _:                                 # No discount for other categories
            discount_percent = 0.00
    
    # Calculate sales discount amount
    sales_discount = subtotal * discount_percent
    
    # Calculate final product price after discount
    final_product_price = subtotal - sales_discount
    
    # Add current product's final price to running total
    total_after_discounts += final_product_price
    
    # Print the results for each product
    print(f"\nProduct: {product_name}")
    print(f"  Subtotal: ${subtotal:.2f}")
    print(f"  Discount: ${sales_discount:.2f} ({discount_percent * 100}% off)")
    print(f"  Final Price: ${final_product_price:.2f}")

# Task 4: Subtotals, membership discounts, and final invoice total
# Print the total after all product discounts
print(f"\nTotal after product discounts: ${total_after_discounts:.2f}")

# Use if-elif-else statement to calculate membership discount based on tier
member_tier = customer_data["tier"]            # Get customer's loyalty tier

# Determine membership discount percentage based on tier
if member_tier == "Platinum":                  # Platinum tier = 16% discount
    member_discount_percent = 0.16
elif member_tier == "Gold":                    # Gold tier = 11% discount
    member_discount_percent = 0.11
elif member_tier == "Silver":                  # Silver tier = 5% discount
    member_discount_percent = 0.05
else:                                          # Non-member = 0% discount
    member_discount_percent = 0.00

# Calculate membership discount amount
member_discount_amount = total_after_discounts * member_discount_percent

# Calculate final total owed by customer
final_total_owed = total_after_discounts - member_discount_amount

# Display membership discount amount and final total owed
print(f"Membership discount ({member_tier} tier, {member_discount_percent * 100}%): ${member_discount_amount:.2f}")
print(f"Final Total Owed by customer: ${final_total_owed:.2f}")