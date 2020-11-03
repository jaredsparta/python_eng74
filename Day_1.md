# Basics

- What is a variable
- Dynamically typed language
- Overwriting variables
- Getting user input from the command line

**Pseudocode**
- A plain-language way to show what your code means
- Before you begin any projects, ensure you try to plan everything accordingly so you aren't 300 lines in and you forget to put a feature in.
- Comment lines to remind you and others that read it, what it does
- Don't overcomment

**Variables**
- They are things to store values in
- Check with ```type(<varname>)```
- Some types are: str, int, bool, complex, float, etc.

**String methods**

```python
    greetings = "Hello World!!"
    print(greetings.isalpha())
    # .isalpha() checks if all values in the string are letters, hence returns False

    print(greetings.islower())
    # .islower() returns True if all letters are lowercase

    print(greetings.startswith("H"))
    # .startswith returns True if the string starts with the value

    print(greetings.endswith("!"))
    # .endswith() returns True if the string ends with the value

    "abcd".isalpha() # returns True
    "abcd!!!".isalpha() #returns False
    "ab cd".isalpha() #returns False as it contains a space
```
```python
    string = "Hello World!"

    string[-1]
    # returns the last character in the string

    string[2:5]
    # returns the characters from 2 to 4 (ends at 5 but doesn't include it) 
```

```python
    whitespaces = "   lots of spaces at the end              "
    # spaces still count as characters and still consumes memory

    whitespaces.strip()
    # .strip() will delete all spaces at the beginning and end of the string
    # doesn't change variable

    weird_str = ",,,aaaJared..."
    weird_str.strip(",.a")
    # giving arguements will remove all leading and trailing instances of , . and a
    # so weird_str would now be "Jared"
    # doesn't change varaiable
```

```python
    example = "jared jared solano"
    print(example.count("jared"))
    # .count() returns the number of times the string arguement appears in the text
    # doesn't change variable

    print(example.replace("solano", "jared"))
    # .replace(x,y) will replace all instances of x with y
    # so this returns "jared jared jared"
    # doesn't change variable
```

- These functions come in-built and can be called with any string datatype

**Concatenation**
```python
    # concatenate two ways:
    first_name = "Jared"
    last_name = "Solano"
    age = 21

    print(first_name + last_name + str(age))
    # prints JaredSolano21
    # add spaces for spacing and you also need str(age) as the datatypes must be consistent when adding them 

    print(first_name, last_name, age)
    # prints out Jared Solano 21
    # this method doesn't care about data types and adds spacing already
```
