# shopping_list = ["apple", "milk", "bread"]
# print(shopping_list)
# print(type(shopping_list))

# Task: create a list of length 7 of different data types
# display the data
# add, remove, replace, pop
# print the list in reverse

task1 = ["apple", "hash browns", 1, 2, 5, 1+6j, ["bananas"]]
task1.append("milk") #adds milk at the end
task1.remove(2) # removes the first instanceof 2
task1.insert(2, "bread") # inserts bread at index 2
task1[4] = "beans" # changes index 4

print(type(task1[0]))
print(type(task1[1]))
print(type(task1[2]))
print(type(task1[3]))
print(type(task1[4]))
print(type(task1[5]))
print(type(task1[6]))
print(type(task1[7]))



print(task1[::-1]) # prints out list in reverse
