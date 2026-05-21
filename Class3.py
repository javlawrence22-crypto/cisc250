animals = ["dog", "cat", "cow", "donkey", "sheep"]
if "cow" in animals:
    print("moooo")

if "pig" not in animals:
    print("no pigs found")


age = 17
if age >= 18:
    print("You are eligible to vote!") 
else:    
    print("Sorry, you are too young to vote.")   
    print("Please register to as soon as you turn 18!")


r_toppings = ["green peppers", "mushrooms", "extra cheese"]
for r_topping in r_toppings:
    if r_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {r_topping}.")
print("\nFinished making your pizza!")

status = 403
match status:
    case 400:
        print("Bad request")
    case 401 | 403 | 404:
        print("Not allowed")
    case 418:
        print("I'm a teapot")
    case _:
        print("Something's wrong with the internet")

# dictionary example
dict = {
    'id': "Jlaw",
    'first': "jav",
    'last': "lawrence",
    'title': "Mr",
    'age': 23,
    'married': False,
}
# looping through the dictionary is the same as looping through the keys
for k in dict: 
    print(k) 

print(dict)
print(dict.items())
print(dict.keys())
print(dict.values())    

# looping through key-value pairs
for key, value in dict.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# looping through keys only
for key in dict.keys():
    print(f"\nKey: {key}")
# looping through values only
for value in dict.values():
    print(f"Value: {value}")
# You can loop through a dictionary by sorting its keys, using the sorted() function
# Try it:
for key, value in sorted(dict.items()):
    print(f"\nKey: {key}")
    print(f"Value: {value}")

    