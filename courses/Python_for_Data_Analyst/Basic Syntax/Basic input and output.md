#Python: Basic input and output
#Basic input and output

#### Module Overview 
 In this module on Basic input and output, we'll discuss Basic input and output. 

 Learning Objectives: 

-  Read a file
-  Write a file
-  Convert data types
-  Read and write to a .CSV file
-  Read from and write to a .json file

#### Read a file


```python
file=open("file.txt","r")

```


```python
file.read()

```




    'This is a text file.\n'




```python
file.readline()

```




    ''




```python
file.readlines()

```




    ['This is a text file.']



#### Write a file


```python
file=open("file.txt","w")

```


```python
file.write("this is the new version of the file")
file.close()

```

#### Convert data types


```python
#Converting a string to an integer
int("56")

```




    56




```python
#Converting an integer to a string
str(56)

```




    '56'




```python
#Converting a float to an integer
int(56.5)

```




    56




```python
#Converting an integer to a float
float(56)

```




    56.0



#### Read and write to a .CSV file


```python
import csv

```


```python
#Reading from a .csv file
file=open("file.csv","r")
reader=csv.reader(file)
for row in reader:
    print(row)
```

    ['Name', 'Age', 'Sex']
    ['Homer', '40', 'Male']
    ['Bart', '10', 'Male']
    ['Lisa', '8', 'Female']
    ['Marge', '35', 'Female']
    


```python
#Writing to a .csv file
file=open("file.csv","a",newline="")
writer=csv.writer(file)
writer.writerow(["Maggie","1","Female"])
file.close()

```

#### Read from and write to a .json file


```python
import json

```


```python
#Reading from a .json file
file=open("file.json","r")
json.load(file)
```




    {'name': 'Homer', 'age': 40, 'sex': 'Male'}




```python
#Writing to a .json file
file=open("file.json","w")
json.dump({'name':'Maggie', 'age':1, 'sex':'Female'},file)
file.close()
```