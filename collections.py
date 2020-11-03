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

print(task1[::-1]) # prints out list in reverse
