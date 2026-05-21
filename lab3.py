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
# Loop 
for product_id, product_info in product_list.items():
    product_name = product_info["name"]         
    category = product_info["category"]        
    unit_price = product_info["price"]          
    quantity = product_info["quantity"]         
    
    # subtotal 
    subtotal = unit_price * quantity
    
    #match-case 
    match category:
        case "Appliance":                       # 20% discount on Appliances
            discount_percent = 0.20
        case "Clothing":                        # 10% discount on Clothing
            discount_percent = 0.10
        case _:                                 # No discount for other categories
            discount_percent = 0.00
    
    #  sales discount 
    sales_discount = subtotal * discount_percent
    
    # final product price 
    final_product_price = subtotal - sales_discount
    
    # Add current product's final price to running total
    total_after_discounts += final_product_price
    
    print(f"\nProduct: {product_name}")
    print(f"  Subtotal: ${subtotal:.2f}")
    print(f"  Discount: ${sales_discount:.2f} ({discount_percent * 100}% off)")
    print(f"  Final Price: ${final_product_price:.2f}")

# Task 4
# total after all product discounts
print(f"\nTotal after product discounts: ${total_after_discounts:.2f}")

#
member_tier = customer_data["tier"]            

# membership discount percentage based on tier
if member_tier == "Platinum":                  
    member_discount_percent = 0.16
elif member_tier == "Gold":                     
    member_discount_percent = 0.11
elif member_tier == "Silver":                  
    member_discount_percent = 0.05
else:                                          
    member_discount_percent = 0.00

# membership discount amount
member_discount_amount = total_after_discounts * member_discount_percent

# final total owed by customer
final_total_owed = total_after_discounts - member_discount_amount


#membership discount amount and final total owed
print(f"Membership discount ({member_tier} tier, {member_discount_percent * 100}%): ${member_discount_amount:.2f}")
print(f"Final Total Owed by customer: ${final_total_owed:.2f}")

