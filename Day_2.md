# Collections
- Just data structures -- they store data values and will dictate what methods we can use with them-
- Lists, tuples, dictionaries, sets etc.

**Lists**
```python
    # Lists use [] and can mix data types
    list = ["bread", "apple", 1, 2, 3]

    # they are mutable -- we can add, remove and change values in a list
    list.append("bananas")  # adds "bananas" to the end of list
    list.remove("bread") # removes the value; if there are identical ones, it removes only the first index
    list.pop() # removes the last item in the list and returns the value

    # slice the list to get values
    print(list[1])

    # replace values, this replaces the index 0 with "milk"
    list[0] = "milk"
```

**Tuples**
```python
    # Tuples use () and can mix data types
    # You must use commas to separate: tuple = 1,2,3,4 is the same
    tuple = (1,2,3,4, "apple")

    # they are immutable and can't be changed
    tuple.index("apple") # returns the index of "apple"

    # one can still slice tuples
```

**Dictionaries**
```python
    # Dictionaries use {} and can mix data types
    # Each entry has a key:value pair associated with it
    ### Dictionaries aren't indexed by numbers but by the keys ###
    dictionary = {"name":"jared", "age":21, "dob":"2nd may 1999"}
    
    # some useful dict methods are:
    dictionary.keys()    # returns all keys in a list
    dictionary.values()  # returns all values in a list
    dictionary.items()  # returns all key:value pairs in the list
    dictionary["name"] # returns the value of the key "name"
```

**Sets**
```python
    # Sets use {}
    # They are unindexed and unordered
    # To access, you can print with a for loop or you can test whether it has a specific value using in
    set = {"apple", "banana", "bread"}

    print(set) # Printing a set will pick a random order of the values and print them
    print(bool("apple" in set)) # Returns True because "apple" is in the set
```

# Control Flow

**if, elif and else**
```python
    # these check a condition and if true, it will run that corresponding code
    if <condition>:
        <code>
    elif <condition>:
        <code>
    else:
        <code>    
```

**loops**
```python
    # break makes you escape the loop
    for <name> in <iterable>:
        <code>
        if <condition>:
            break

    # continue escapes that loop and goes to the next one
    for <name> in <iterable>:
        <code>
        if <condition>:
            continue
```