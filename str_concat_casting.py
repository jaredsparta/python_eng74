# What is concatenation

# f_name = "James"
# m_name = "Bond"
# l_name = "007"
# age = 18
# 
# print(f_name)
# print(m_name)
# print(l_name)

# two ways to concat - first one you can mix datatypes but if you do 2nd they have to be the same type
#print(f_name, m_name, l_name, age)
#print(f_name+ " " + m_name + " " + l_name + " " + str(age))
# str() method returns a string of the arguement

name = input("Please input your name: ")
age = input("Please input your age: ")
dob = input("What's your date of birth? ")
post_code = input("What is your postcode? ")
address_firstline = input("What is your door number? ")

print(f"\nHello {name}, you are /{} {age} years old and were born on {dob}.")
print(f"You live at door {address_firstline} in post code {post_code}.\n")
