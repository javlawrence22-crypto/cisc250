# Name: Javrick Lawrence
# LAB 2
# =============
# Question 1
# ============

messy_menu = "    Pizza, burGER, SaLAd "

# using strip to remove spaces
clean_menu = messy_menu.strip()

# using lower case
clean_menu = clean_menu.lower()

# displaying today's menu
print("Today's special menu list:", clean_menu)

# ================
# Question 2
# ================

# a list of even numbers
even_numbers = list(range(2, 51, 2))

#display even numbers
print("Even numbers from 2 to 50:")
print(even_numbers)

#Calculate the total number of items and display
total_items = len(even_numbers)
print("Total number of items in the list:")
print(total_items)

# sum of even numbers
total_sum = sum(even_numbers)
print("Sum of even numbers:")
print(total_sum)

# Multiplier with sum of max and min
Multiplier = 2
max_number = max(even_numbers)
min_number = min(even_numbers)
sum_max_min = max_number + min_number
product = Multiplier * sum_max_min
print("Maximum number:")
print(max_number)
print("Minimum number:")
print(min_number)
print("sum of max and min number:")
print(sum_max_min)
print("product of multipler:")
print(Multiplier)
print("sum of max and min")
print(product)

# ================
# Question 3
# ================

# a guest list
guest_list = ["ashley", "aaron", "joel", "john"]
print("guest list:")
print(guest_list)

#add "linus" to end of the list
guest_list.append("linus")
print("list after adding linus:")
print(guest_list)

#Add "guido" to the beginning of the list
guest_list.insert(0,"guido")
print("list after adding guido:")
print(guest_list)

#Sort the list alphabetically and permanently
guest_list.sort()
print("list sorted permanently:")
print(guest_list)

#Invitation list
invitations = [f"You are invited, {name.capitalize()}!" for name in guest_list]
print("Invitation list:")
print(invitations)

#Slice for the first 3 invitations
print("first three invitations:")
for invitation in invitations[:3]:
 print(invitation)   