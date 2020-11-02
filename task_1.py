# gets the input of the person's name, dob and age
# outputs all the values in one line

name = input("What is your name?")
dob = input("What is your date of birth?")
age = input("What is your age?")

print("You are "+ name + ", born on", dob, ", which makes you", age, "years old!")

print("")

print("the types of data here are:")
print("name is a", type(name))
print("date of birth is a", type(dob))
print("age is a", type(age))
