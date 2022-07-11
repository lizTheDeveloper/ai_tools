#  Write a file
            open()
    write()
    close()

# Steps

1. Open a file
2. Write to the file
3. Close the file

# Open a file

The first step is to open a file. 

You do this by using the 
open()
function.

The 
open()
function requires a few parameters. The first parameter is the name of the file you want to open. The second parameter is the mode. The mode is how you want to open the file.

The most common modes are:

    "r" - Read - Default value. Opens a file for reading, error if the file does not exist

    "a" - Append - Opens a file for appending, creates the file if it does not exist

    "w" - Write - Opens a file for writing, creates the file if it does not exist

For our example, we will use the mode 
"w"
for write.

# Write to the file

The second step is to write to the file.

To do this, you use the 
write()
function.

The write function takes a string as a parameter.

# Close the file

The last step is to close the file.

You do this by using the 
close()
function.

It is important to close the file because if you don't, anything you wrote to the file may not actually get saved.

# Example

Let's put all these steps together in an example.

We are going to write a file called 
"textfile.txt".

The contents of the file are going to be a simple sentence.

Here is the code:

# Open the file

f = open("textfile.txt", "w")

# Write some lines of text

f.write("Hello, world!\n")
f.write("This is our new text file\n")
f.write("and this is another line.\n")
f.write("Why? Because we can.\n")

# Close the file

f.close()

# Read the file we just created

f = open("textfile.txt", "r")

# Print the contents of the file

print(f.read())
        ### When might you need to  Write a file?
        
1. When creating a new dataset from scratch, you will need to write the data to a file.
2. When cleaning and transforming data, you may need to output the results to a file.
3. When creating reports or visualizations, you may need to save them to a file.

        This might look like:

        1. When writing up a report on the results of data analysis, the Data Analyst may need to output the results to a file in order to include them in the report.
2. When creating visualizations to accompany the report, the Data Analyst may need to save them to a file in order to include them in the report.
3. When creating a presentation on the results of data analysis, the Data Analyst may need to save the presentation to a file in order to share it with others.

        ### How do you practice  Write a file?
        
Create a Python file named "analyze.py" with the following code:

import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

This code will read in a CSV file called "data.csv" and print out the first 5 rows of data.

        ### How do you practice  Write a file in Python?
        

#calculate median age
median_age = df['age'].median()
print(median_age)

#calculate mode age
mode_age = df['age'].mode()
print(mode_age)

#calculate standard deviation of age
sdev_age = df['age'].std()
print(sdev_age)

#calculate variance of age
variance_age = df['age'].var()
print(variance_age)
        