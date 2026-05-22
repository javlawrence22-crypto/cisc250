# =============================================================================
# Student Name: Javrick lawrence
# Lab Title: Invoice Creator
# Date: may 20, 2026
# =============================================================================

# TASK 1: Nesting - Create a dictionary of dictionaries of the products being 
# purchased. Complete the nested dictionary below with the data in the lab 
# table.
product_list = {
    "el2234" : { 
        "name" : "Head Phones",           
        "category" : "Electronics",       
        "price" : 19.99,                  
        "quantity" : 2                    
        },
    "sh9989" : {
        "name" : "Running Shoes",        
        "category" : "Footwear",         
        "price" : 99.99,                  
        "quantity" : 2                    
        },
    "ap0098" : {
        "name" : "Smart Toaster",         
        "category" : "Appliance",         
        "price" : 130.00,                 
        "quantity" : 1                   
        },
    "cl3321" : {
        "name" : "Cotton Shirt",          
        "category" : "Clothing",          
        "price" : 10.00,                 
        "quantity" : 4                    
        },
    }

#Create a dictionary to hold the customer data
customer_data = {
    "name": "Hannah Davis",               
    "tier": "Gold"                       
}
print(f"Processing Order for: {customer_data['name']} [{customer_data['tier']} Tier Member]...")

total_after_discounts = 0

# Loop through each product in the product list
for product_id, product_info in product_list.items():
    product_name = product_info["name"]         
    category = product_info["category"]        
    unit_price = product_info["price"]          
    quantity = product_info["quantity"]         
    
    # calculate subtotal (price times quantity)
    subtotal = unit_price * quantity
    
    # figure out discount based on category using match-case
    match category:
        case "Appliance":
            discount_percent = 0.20
        case "Clothing":
            discount_percent = 0.10
        case _:
            discount_percent = 0.00
    
    # calculate how much money they save
    sales_discount = subtotal * discount_percent
    
    # price after the product discount
    final_product_price = subtotal - sales_discount
    
    # add to the running total for later
    total_after_discounts = total_after_discounts + final_product_price
    
    # print info for this product
    print(f"\nProduct: {product_name}")
    print(f"  Subtotal: ${subtotal:.2f}")
    print(f"  Discount: ${sales_discount:.2f} ({discount_percent * 100}% off)")
    print(f"  Final Price: ${final_product_price:.2f}")

# Task 4 starts here
# show total after all product discounts
print(f"\nTotal after product discounts: ${total_after_discounts:.2f}")

# get customer's membership tier from the dictionary we made earlier
member_tier = customer_data["tier"]            

# decide what percent discount they get based on their tier
if member_tier == "Platinum":                  
    member_discount_percent = 0.16
elif member_tier == "Gold":                     
    member_discount_percent = 0.11
elif member_tier == "Silver":                  
    member_discount_percent = 0.05
else:                                          
    member_discount_percent = 0.00

# calculate how much the membership saves them
member_discount_amount = total_after_discounts * member_discount_percent

# apply membership discount to get final amount due
final_total_owed = total_after_discounts - member_discount_amount

# print the membership discount and final bill
print(f"Membership discount ({member_tier} tier, {member_discount_percent * 100}%): ${member_discount_amount:.2f}")
print(f"Final Total Owed by customer: ${final_total_owed:.2f}")

