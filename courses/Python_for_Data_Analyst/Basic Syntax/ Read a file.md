
    #  Read a file
     1. Reading a .txt file 
 2. Reading a .csv file 
 3. Reading a .xls file 
 4. Reading a .json file 

# 1. Reading a .txt file 

Reading a .txt file is the easiest. The file is read line by line and each line is passed to a list. 


```python
# Open the file with read only permit
f = open('my_text_file.txt', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
lines = f.readlines()
# close the file after reading the lines.
f.close()
```

# 2. Reading a .csv file 

Reading a .csv file requires the use of the csv module. 

The csv module comes with a function reader() which can be used to read the contents of a .csv file as a list of lists. 


```python
# Open the file with read only permit
f = open('my_csv_file.csv', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
reader = csv.reader(f)
# close the file after reading the lines.
f.close()
```

# 3. Reading a .xls file 

Reading a .xls file requires the use of the xlrd module. 

If you don't have the module installed, run the following command in the terminal: 

pip install xlrd 

The xlrd module comes with a function open_workbook() which can be used to open and read a .xls file. 


```python
# Open the file with read only permit
wb = open_workbook('my_xls_file.xls')
# Get workbook active sheet
sheet = wb.sheet_by_index(0)
# read a row
print(sheet.row_values(0))
```

# 4. Reading a .json file 

Reading a .json file requires the use of the json module. 

The json module comes with a function loads() which can be used to load the contents of a .json file as a dictionary. 


```python
# Open the file with read only permit
f = open('my_json_file.json', "r")
# use readlines to read all lines in the file
# The variable "lines" is a list containing all lines in the file
data = json.loads(f.read())
# close the file after reading the lines.
f.close()
```
    ### When might you need to  Read a file?
    
1. You may need to read a file in order to extract data that is stored in that file. 
2. You may need to read a file in order to transform it into another format that can be used by another program. 
3. You may need to read a file in order to load it into a database.

    This might look like:

    1. Extracting data from a file in order to analyze it.
2. Transforming a file into a different format in order to be able to use it with another program.
3. Loading a file into a database in order to be able to query it.

    ### How do you practice  Read a file?
    
1. Read in a text file
2. Print out the contents of the file
3. Close the file

    ### How do you practice  Read a file in Python?
    

f.close()

Next, we run the code by pressing the Run button. The script will run and print the contents of data.txt to the console:

And that’s it! You’ve written your first Python script in Google Colaboratory!

If you want to get started with Machine Learning but you’re having trouble installing Python or specific packages such as TensorFlow, PyTorch, or OpenCV on your system, Google Colaboratory is a good place to start.
    