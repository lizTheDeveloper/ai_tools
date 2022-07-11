
    #  Learn how to create and index strings.
     A string is a series of characters. In Python, we can create strings by enclosing characters in quotes. For example 

#!/usr/bin/env python3 

print("This is a string.") 
print('This is also a string.') 
print("""This is a
string made up of
several lines.""") 
You can use either double or single quotes to create a string. If you want to use both types of quotes in a string, you'll need to use

You can use either double or single quotes to create a string. If you want to use both types of quotes in a string, you'll need to use

You can use either double or single quotes to create a string. If you want to use both types of quotes in a string, you'll need to use

You can use either double or single quotes to create a string. If you want to use both types of quotes in a string, you'll need to use

You can use either double or single quotes to create a string. If you want to use both types of quotes in a string, you'll need to use

You can use either double or single quotes to create a string. If you want to use both types of quotes in a string, you'll need to use
 triple quotes:

 """String made up of
 several lines""" 
You can also use the escape character \ to insert quotes inside a string:

print("This is a string with \"double quotes\" in it.") 
print('This is a string with \'single quotes\' in it.') 
If you want to include a backslash in a string, you'll need to use two backslashes:

print("This string has a backslash \\ in it.") 
Strings can be concatenated using the + operator:

print("Hello " + "world!") 
You can also repeat a string using the * operator:

print("Hello " * 3) 
# prints Hello Hello Hello 
Indexing strings
Strings can be indexed so that you can access individual characters within the string. Indexing starts at 0. For example:

#!/usr/bin/env python3 

my_string = "Hello, world!" 
print(my_string[0]) 
# prints H 
print(my_string[7]) 
# prints w 
You can also index from the end of the string using negative numbers. For example, my_string[-1] will return the last character in the string.

Indexing a character returns a string containing only that character. For example, my_string[0:3] will return the first three characters in the string.

You can also specify a step size using the syntax my_string[start:end:step]. For example, my_string[::2] will return every other character in the string.

If you don't specify a start or end index, the default is the beginning and end of the string, respectively.

You can also index from the end of the string using negative numbers. For example, my_string[-1] will return the last character in the string.

Indexing a character returns a string containing only that character. For example, my_string[0:3] will return the first three characters in the string.

You can also specify a step size using the syntax my_string[start:end:step]. For example, my_string[::2] will return every other character in the string.

If you don't specify a start or end index, the default is the beginning and end of the string, respectively.

#!/usr/bin/env python3 

my_string = "Hello, world!" 
print(my_string[0:5]) 
# prints Hello 
print(my_string[7:]) 
# prints world! 
print(my_string[:3]) 
# prints Hel 
print(my_string[::2]) 
# prints Hlowrd 
print(my_string[::-1]) 
# prints !dlrow ,olleH 
# prints every other character in reverse order 
#!/usr/bin/env python3 

my_string = "Hello, world!" 
print(my_string[0:5]) 
# prints Hello 
print(my_string[7:]) 
# prints world! 
print(my_string[:3]) 
# prints Hel 
print(my_string[::2]) 
# prints Hlowrd 
print(my_string
    ### When might you need to  Learn how to create and index strings.?
    
1. When dealing with data that includes text columns, you may need to convert those columns to a format that is easier to work with. For example, you may want to convert all text to lowercase so that you can more easily search for specific values.
2. You may need to index strings in order to quickly find specific values within a text column. For example, if you have a column of email addresses, you may want to index the portion of the email address that comes before the "@" symbol.
3. You may need to create new strings based on the values in other columns. For example, you may want to concatenate first and last names into a single "full name" column.

    This might look like:

    
If you were working with a dataset of customer data, you might want to convert all text to lowercase so that you can more easily search for specific values. For example, you might want to index the customer's first name, last name, and email address.

You might also want to create new strings based on the values in other columns. For example, you might want to concatenate the customer's first and last names into a single "full name" column.

    ### How do you practice  Learn how to create and index strings.?
    

1. Create a string variable called my_string and assign it the value "Hello, world!"

2. Print the my_string variable to the console

3. Use the len() function to get the length of my_string and print it to the console

4. Get the first character of my_string using indexing and print it to the console

5. Get the last character of my_string using indexing and print it to the console

    ### How do you practice  Learn how to create and index strings. in Python?
    , a Computer Science course, or a Data Science course.
# TODO: Write a short example of code using a realistic example of real-world data that a Data Analyst would use and meaningful variable names to practice  Learn how to create and index strings. in a course on Python, a Computer Science course, or a Data Science course.
# TODO: Write a short example of code using a realistic example of real-world data that a Data Analyst would use and meaningful variable names to practice  Learn how to create and index strings. in a course on Python, a Computer Science course, or a Data Science course.
# TODO: Write a short example of code using a realistic example of real-world data that a Data Analyst would use and meaningful variable names to practice  Learn how to create and index strings. in a course on Python, a Computer Science course, or a Data Science course.
# TODO: Write a short example of code using a realistic example of real-world data that a Data Analyst would use and meaningful variable names to practice  Learn how to create and index strings. in a course on Python, a Computer Science course, or a Data Science course.
# TODO: Write a short example of code using a realistic example of real-world data that a Data Analyst would use and meaningful variable names to practice  Learn how to create and index strings. in a course on Python, a Computer Science course, or a Data Science course.


print(__doc__)

from PIL import Image
from matplotlib import pyplot as plt


im = Image.open("/home/jovyan/Pictures/abstract_art_paintings_high_resolution_wallpaper_hd_background_marvelous_high_resolution_abstract_wallpapers_x_px.jpg")
plt.imshow(im)

print("\nThe image is", im.size[0], "by", im.size[1], "pixels")
    