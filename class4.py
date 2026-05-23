# ============================================================
# LESSON 4 PRESENTATION - USER INPUT AND WHILE LOOPS
# ============================================================

# ============================================================
# Slide 1 – Using the input() Function for User Input
# ============================================================

name = input("Please enter your name: ")
print(f"\nHello, {name}!")


# ============================================================
# Slide 2 – Prompt with String Concatenation
# ============================================================

prompt = "If you share your name, we can personalize the "
prompt += "messages you see. \nWhat is your first name? "

name = input(prompt)

print(f"\nHello, {name}!")


# ============================================================
# Slide 3 – Handling Numeric Input
# ============================================================

age = input("How old are you? ")

age = int(age)  # convert string to integer

if age >= 21:
    print("You can legally drink alcohol in the US. Drink responsibly!")
else:
    print("You can't legally buy alcohol in the US.")


# ============================================================
# Slide 4 – User Input with Exception Handling Example
# ============================================================

try:
    age = input("How old are you? ")
    age = int(age)

except ValueError:
    print("That's not a valid number. Please try again.")

else:
    if age >= 21:
        print("You can legally drink alcohol in the US. Drink responsibly!")
    else:
        print("You can't legally buy alcohol in the US.")


# ============================================================
# Slide 5 – For Loop compared to While Loop
# ============================================================

# For loop
for i in range(5):
    print(i)

# Equivalent while loop
i = 0

while i < 5:
    print(i)
    i += 1


# ============================================================
# Slide 6 – User Input with While Loop Example
# ============================================================

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)


# ============================================================
# Slide 7 – While Loop Example without printing "quit"
# ============================================================

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)


# ============================================================
# Slide 8 – While Loop using a Flag Variable
# ============================================================

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program.\nInput > "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


# ============================================================
# Slide 9 – Using break to Exit a Loop
# ============================================================

prompt = "\nTell me something, and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program.\nInput > "

while True:
    message = input(prompt)

    if message == 'quit':
        break
    else:
        print(message)


# ============================================================
# Slide 10 – Using continue in a Loop
# ============================================================

current_number = 0

while current_number < 10:
    current_number += 1

    if current_number % 2 == 0:
        continue

    print(current_number)


# ============================================================
# Slide 11 – While Loop with List Example 1
# ============================================================

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    print(f"Number of unconfirmed users: {len(unconfirmed_users)}")

    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")

    confirmed_users.append(current_user)

# Display all confirmed users
print("\nThe following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# ============================================================
# Slide 12 – While Loop with List Example 2
# ============================================================

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)


# ============================================================
# Slide 13 – Filling a Dictionary with User Input
# ============================================================

responses = {}

polling_active = True

while polling_active:

    name = input("\nWhat is your name? ")

    response = input("Which mountain would you like to climb someday? ")

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")

    if repeat == 'no':
        polling_active = False

# Polling is complete
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")