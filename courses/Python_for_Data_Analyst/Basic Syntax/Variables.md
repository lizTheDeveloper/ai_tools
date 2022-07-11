#Python: Basic Syntax
#Variables

#### Module Overview 
 In this module on Basic Syntax, we'll discuss Variables. 

 Learning Objectives: 

-  To understand what variables are and why they are used. 
-  To understand how to store and retrieve data using variables. 
-  To understand how to use variables for mathematical operations. 

##### Variable Introduction

Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory. 

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Hence, by defining variables we can store data in memory. 

##### Assigning Values to Variables

Assignment is done with a single equals (=) sign, and the variable on the left gets set to the value of the expression on the right. 

For example:

```python
x = 10
y = 5
z = x + y
```



##### Multiple Assignment 
In Python, you can also assign a single value to multiple variables simultaneously.

For example:
```python
x = y = z = 1
```

This assigns the integer value `1` to `x`, `y`, and `z`.

##### Storage Locations

Every value in Python has a data type. Different data types in Python are defined in the following table. 

Type |	Description
-----|------
int |	Stores whole numbers, without a decimal point
float |	Stores floating point numbers, with a decimal point.
str |	Stores textual information as a sequence of characters.
list |	Stores a sequence of heterogeneous items
tuple |	Stores a sequence of heterogeneous items. Immutable
dict |	Stores associations between keys and values

##### Standard Data Types

The data stored in memory can be of many types. For example, a person's age is stored as a numerical value and his or her address is stored as alphanumeric characters.

 Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

##### Python Variables

Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Hence, by defining variables we can store data in memory.

##### Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. For example:
```python
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print(counter)
print(miles)
print(name)
```

Here, `counter`, `miles`, and `name` are variables. This produces the following result:
```python
100
1000.0
John
```

##### Python allows you to assign values to multiple variables in one line:
```python
a = b = c = 1
```

And you can also assign multiple objects to multiple variables in one line:
```python
a, b, c = 1, 2, "john"
```

This is called `unpacking`.

##### Python accepts single, double, and triple quotes for strings. All the three represent the same objects.
For example:
```python
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
```

Here, the variable `paragraph` spans over multiple lines. But if you print it, only the part up to the last character that is placed on the source code line ends up being printed. The output produced by the above code will be:

```python
word
This is a sentence.
This is a paragraph. It is made up of multiple lines and sentences.
```

##### You can delete one or more objects by using the `del` statement. For example:
```python
del a
del a, b, c
```

##### Local and Global Variables

Variables that are defined inside a function body have a local scope, and those defined outside have a global scope.

This means that local variables