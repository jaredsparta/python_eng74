#simple counter
number = 0

while number < 10:
    print(number)
    if number == 4:
        break
    number += 1

# take user input with while loop

user_prompt = True

while user_prompt:
    age = input("Input age: ")
    # .isdigit() returns True if all characters in string are numbers, o/w False
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide a valid answer")

print(f"You are {age} years old")

