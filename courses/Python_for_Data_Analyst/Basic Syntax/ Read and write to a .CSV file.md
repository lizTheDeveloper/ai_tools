#  Read and write to a .CSV file
        
The CSV module is used for reading and writing files in the CSV (comma separated value) format. It contains functions and classes to easily perform that task. 


The CSV format is the most commonly used import and export format for databases and spreadsheets. For example, databases and contact managers often support CSV files. These files may sometimes be called Character Separated Values or Comma Delimited files. CSV files are not like Excel Workbook files, they are basically text files with a lot of data in them. CSV files can be created using Microsoft Excel, OpenOffice Calc, Google Spreadsheets, and Notepad. 

A CSV file is a plain text file that stores tabular data. CSV is short for comma-separated values, a file format that presents tabular data in plain text. Each line of the CSV file is a new data record. Each record consists of one or more fields, separated by commas. The use of the comma as a field separator is the source of the name for this file format. A CSV file typically stores tabular data (numbers and text) in plain text, in which case each line will have the same number of fields. 



## Examples 

### Example 1 
CSV files are very easy to work with programmatically. 

```python
import csv 
  
# reading csv file 
with open('employees.csv') as csv_file: 
    csv_reader = csv.reader(csv_file) 
    line_count = 0 
    for row in csv_reader: 
        if line_count == 0: 
            print(f'Column names are {", ".join(row)}') 
            line_count += 1 
        else: 
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.') 
            line_count += 1 
    print(f'Processed {line_count} lines.') 
  
# writing to csv file 
with open('employees.csv', mode='w') as employee_file: 
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
  
    employee_writer.writerow(['John Smith', 'Accounting', 'November']) 
    employee_writer.writerow(['Erica Meyers', 'IT', 'March']) 
```

### Example 2 

```python
import csv 
  
# reading csv file 
with open('employees.csv') as csv_file: 
    csv_reader = csv.DictReader(csv_file) 
    line_count = 0 
    for row in csv_reader: 
        if line_count == 0: 
            print(f'Column names are {", ".join(row)}') 
            line_count += 1 
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.') 
        line_count += 1 
    print(f'Processed {line_count} lines.') 
  
# writing to csv file 
with open('employees_new.csv', mode='w') as employee_file: 
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) 
  
    employee_writer.writerow(['John Smith', 'Accounting', 'November']) 
    employee_writer.writerow(['Erica Meyers', 'IT', 'March']) 
```

### Example 3 

```python
import csv 
  
# reading csv file 
with open('employees.csv', mode='r') as csv_file: 
    csv_reader = csv.DictReader(csv_file) 
    line_count = 0 
    for row in csv_reader: 
        if line_count == 0: 
            print(f'Column names are {", ".join(row)}') 
            line_count += 1 
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in
        ### When might you need to  Read and write to a .CSV file?
        
1. You receive a .CSV file from a colleague that contains data that you need for your analysis.
2. You need to export your data from your database into a .CSV file in order to share it with a colleague.
3. You have a .CSV file containing historical data that you need to analyze.

        This might look like:

        
1. An analyst working with customer data may receive a .CSV file from a colleague containing updated customer contact information.
2. An analyst working with sales data may need to export data from their database into a .CSV file in order to share it with a colleague for analysis.
3. An analyst working with financial data may have a .CSV file containing historical stock prices that they need to analyze.

        ### How do you practice  Read and write to a .CSV file?
        
1. Read in a .CSV file
2. Print out the contents of the file to the console
3. Add a new row to the file
4. Write the file back out to a .CSV file

        ### How do you practice  Read and write to a .CSV file in Python?
        
        