# Collections
- Just data structures -- they store data values and will dictate what methods we can use with them-
- Lists, tuples, dictionaries, sets etc.

**Lists**
```python
    #Lists use [] and can mix data types
    list = ["bread", "apple", 1, 2, 3]

    # they are mutable -- we can add, remove and change values in a list
    list.append("bananas")  # adds "bananas" to the end of list
    list.remove("bread") # removes the value; if there are identical ones, it removes only the first index
    list.pop() # removes the last item in the list and returns the value

    # slice the list to get values
    print(list[1])

    # 

```