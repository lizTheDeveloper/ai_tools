# Python: Basic Syntax
# Data types

#### Module Overview 
 In this module on Basic Syntax, we'll discuss Data types. 

 Learning Objectives: 

-  Learn about the different data types and how Python uses them.
-  Learn about how to convert data types into others.
-  Learn how to create and index strings.

##### Code Overview 

* [Data Types](#data-types)
* [Data Types](#data-types)
* [Data Type Conversion](#data-type-conversion)
* [Strings](#strings)

## Data Types

In Python, there are different data types:

* int (integer; a whole number with no decimal place)
* float (floating point; a number that has a decimal place)
* str (string; a sequence of characters enclosed in single/double/triple quotes)
* list (list; a sequence of elements enclosed in square brackets)
* tuple (tuple; a sequence of elements enclosed in parentheses)
* dict (dictionary; a mapping of elements with curly braces)
* set (set; a unique collection of elements)
* bool (boolean; True or False, 1 or 0)

We'll discuss these data types in more detail in a later module.

## Data Type Conversion

Sometimes, you'll need to convert data types to others. For example, you might need to convert numbers to strings, or strings to lists. Python makes this easy to do with built-in functions.

To convert data types, you'll use the name of the type as a function:

```python
int()
float()
str()
list()
tuple()
dict()
set()
bool()
```

Here's how you'll convert an integer to a float:

```python
float(2)
```

And how you'll convert a float to an integer:

```python
int(2.8)
```

You can also convert strings to lists:

```python
list("hello")
```

This is how you'll convert a list to a string:

```python
str([1, 2, 3, 4, 5])
```

You can also use `list()` to convert a tuple:

```python
list((1, 2, 3, 4, 5))
```

Converting data types can be useful if you need to make sure that an element has the right format.

## Strings

Strings can contain letters, numbers, and symbols. They're enclosed in quotation marks.

```python
"Hello, world!"
```

You can use either single or double quotes.

```python
'Hello, world!'
```

If you need to use quotation marks inside of a string, you can use different quotation marks on either end.

```python
"Hello, I'm a string!"
```

You can also use triple quotes:

```python
"""Hello,
I'm a string!"""
```

You can concatenate strings with the `+` operator:

```python
"Hello, " + "world!"
```

You can repeat strings with the `*` operator:

```python
"Hello, " * 3
```

You can use the `len()` function to find the length of a string:

```python
len("Hello, world!")
```

You can index and slice strings:

```python
"Hello, world!"[0]
"Hello, world!"[1:5]
```

You'll learn more about indexing and slicing in a later module.

##### More on strings

Strings are complex data types, and we'll discuss them in more detail in a later module. In the meantime, here are a few useful functions for working with strings:

* `upper()`: converts a string to uppercase
* `lower()`: converts a string to lowercase
* `title()`: capitalizes the first letter of each word in a string
* `find()`: searches for a substring and returns the index
* `replace()`: replaces a substring with another
* `strip()`: removes whitespace from the beginning and end of a string

You can read more about strings in the [Python documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).
