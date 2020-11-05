**while loops**
```python
    # This is used to execute code until a certain condition is met
    while <condition>:
        <code>
```
- Use ```break``` and ```continue``` in tandem with while loops
- In industry, mainly used for monitoring purposes

- Example:
```python
# simple counter #
number = 0

while number < 10:
    print(number)
    if number == 4:
        break
    number += 1


# take user input with while loop #
user_prompt = True

while user_prompt:
    age = input("Input age: ")
    # .isdigit() returns True if all characters in string are numbers, o/w False
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide a valid answer")

print(f"You are {age} years old")
```

# Functions
- This was done in another repo: [functions](https://github.com/jaredsparta/python_functions)