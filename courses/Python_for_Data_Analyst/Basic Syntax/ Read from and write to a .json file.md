#  Read from and write to a .json file
            a. Reading json file 
    b. Writing json file 

JSON file is a text file which uses the format of JavaScript Object Notation(JSON). JSON file is used to store data in an organized format and can be read in any programming languages. 

# Reading json file: 

JSON files can be read in python using the "load" method of the json library. The load method loads the data from the json file and convert it into Python dictionary. 

# Syntax: 

json.load(file) 

where, 

file: json file path 

# Example: 

import json 

with open("users.json", "r") as read_file: 
	data = json.load(read_file) 

print(data) 

Output: 

{'users': [{'name': 'John', 'age': '20', 'email': 'john@example.com'}, {'name': 'Mike', 'age': '21', 'email': 'mike@example.com'}], 'count': 2} 

# Writing json file: 

The "dump" method of the json library is used to store data in a json file. The dump method accepts a data object and the path of the json file as parameters. 

# Syntax: 

json.dump(data, file) 

where, 

data: data object 
file: path of the json file 

# Example: 

import json 

users = [{"name": "John", "age": 20, "email": "john@example.com"}, 
		{"name": "Mike", "age": 21, "email": "mike@example.com"}] 

with open("users.json", "w") as write_file: 
	json.dump(users, write_file) 



# Python for Data Analyst
#  Json Module 

In this article we'll cover Json module: 

    a. What is json module? 
    b. json.dumps method 
    c. json.dump method 
    d. json.loads method 
    e. json.load method 

# What is json module? 

Json module is a python library which is used to read, write, encode and decode json data. Json module can handle all the data types which are provided by python. Json module have an inbuilt method known as "dumps" which converts python data into json data. 

# json.dumps method: 

json.dumps method is used to convert python data into json data. It accepts a python object as a parameter and converts it into json data. 

# Syntax: 

json.dumps(data) 

where, 

data: python data object 

# Example: 

import json 

user = {"name": "John", "age": 20, "email": "john@example.com"} 

print(json.dumps(user)) 

Output: 

{"name": "John", "age": 20, "email": "john@example.com"} 

# json.dump method: 

json.dump method is used to store python data into a json file. It accepts a python data object and a file object as parameters and stores the data into the json file. 

# Syntax: 

json.dump(data, file) 

where, 

data: python data object 
file: file object 

# Example: 

import json 

user = {"name": "John", "age": 20, "email": "john@example.com"} 

with open("user.json", "w") as write_file: 
	json.dump(user, write_file) 

# json.loads method: 

json.loads method is used to convert json data into Python data. It accepts a string as a parameter and converts it into python data. 

# Syntax: 

json.loads(string) 

where, 

string: json data 

# Example: 

import json 

user_string = '{"name": "John", "age": 20, "email": "john@example.com"}' 

print(json.loads(user_string)) 

Output: 

{'name':
        ### When might you need to  Read from and write to a .json file?
        
1. You may need to read from a .json file when you are working with data that has been collected from a web-based application. The data may be in the form of user profiles, comments, or other information that is stored in a .json file.

2. You may need to write to a .json file when you are storing data that you have collected from a web-based application. The data may be in the form of user profiles, comments, or other information that you want to store for future analysis.

3. You may need to read from and write to a .json file when you are working with data that has been collected from a web-based application and you want to store the data for future analysis. The data may be in the form of user profiles, comments, or other information that is stored in a .json file.

        This might look like:

        
1. A data analyst working with user data from a social media application may need to read from and write to a .json file in order to store the data for future analysis.

2. A data analyst working with comments from an online forum may need to read from a .json file in order to analyze the data.

3. A data analyst working with customer data from an e-commerce website may need to read from and write to a .json file in order to store the data for future analysis.

        ### How do you practice  Read from and write to a .json file?
        

1. Read in the JSON file:

with open("course.json", "r") as file:
    course = json.load(file)

2. Print out the title of the course:

print(course["title"])

3. Change the title of the course:

course["title"] = "New Title"

4. Write the changes back to the file:

with open("course.json", "w") as file:
    json.dump(course, file)

        ### How do you practice  Read from and write to a .json file in Python?
         
 

# In[1]:


# Import libraries to use in project

import pandas as pd
import json


# In[2]:


# Create a dataframe using the .read_json method from the pandas library 
# Assign a variable to the dataframe 
# Display the dataframe to ensure it is complete and in order 
# Display the first ten rows of the dataframe to ensure it is complete and in order 


df = pd.read_json("supermarkets.json")
df.set_index("ID")
df.head(10)


# In[3]:


# Create a new column in the dataframe with a value assigned to each row of the column 
# Display the first ten rows of the dataframe to ensure the new column was added and that the values are correct 


df["Continent"] = df.shape[0]*["North America"]
df.head(10)


# In[4]:


# Create a new column in the dataframe with a value assigned to each row of the column 
# Display the first ten rows of the dataframe to ensure the new column was added and that the values are correct 


df["Continent"] = df["Country"] + "," + "North America"
df.head(10)


# In[5]:


# Create a new column in the dataframe with a value assigned to each row of the column 
# Display the first ten rows of the dataframe to ensure the new column was added and that the values are correct 


df_t = df.T # Transpose (flip) all columns and rows in dataframe  


# In[6]:


# Create a new column in the dataframe with a value assigned to each row of the column 
# Display the first ten rows of the dataframe to ensure the new column was added and that the values are correct 


df_t["My Address"] = ["My City", "My Country", 10,7,"My Shop","My State","My Continent","My Country",1,11] # Add a row at index 9 called "My Address" with values for each column in row 9   


# In[7]:


# Transpose (flip) all columns and rows in dataframe  
# Display all rows and columns of dataframe to ensure that values were added correctly

    
df = df_t.T    # Assign all columns and rows from transposed dataframe back into original dataframe without transposing it   

    
    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    
        