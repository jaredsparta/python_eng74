## A task utilising dictionaries

full_name = input("What's your name? ").title()
age = int(input("Please input, as a number, your age: "))
address = input("What's the first line of your address? ").title()
educ = input("What degree did you do at university? ").capitalize()
course = input("What course are you doing now? ").title()

hobby1 = input("Name a hobby: ").title()
hobby2 = input("Name another hobby: ").title()
hobby3 = input("Name a final hobby: ").title()
hobbies = [hobby1, hobby2, hobby3]

values = {}
values["NAME"] = full_name
values["AGE"] = age
values["ADDRESS"] = address
values["EDUCATION"] = educ
values["COURSE"] = course
values["HOBBIES"] = hobbies

print("")
for key in values.keys():
    print(key, ":", type(values[key]))

print(values["HOBBIES"][::-1])

values["HOBBIES"].append("jumping"))
print(values["HOBBIES"])

values["HOBBIES"].remove("jumping")
print(values["HOBBIES"])