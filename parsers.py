

### Parsers 
def parse_data_to_table(data,column_names,description):
    print("parsing data to table", data)
    ## check to see if data already exists in f"./table_data/{column_names}{description}.csv"
    if os.path.exists(f"./table_data/{column_names}{description}.csv"):
        print("data already exists")
        ## read the data from the file
        file = open(f"./table_data/{column_names}{description}.csv")
        data = file.read()
        print("data read from file:\n", data)
        accepted_response = input(f"{data} \n\n Do you want to re-parse the existing data above? (y/n) \n\n")
        print("accepted_response", accepted_response)
        if accepted_response == "y":
            ## delete the file
            os.remove(f"./table_data/{column_names}{description}.csv")
            ## parse the data
            parse_data_to_table(data,column_names,description)
        else:
            response_text = data
    else:
        accepted_response = "y"
    while accepted_response == "y":
        prompt = f"{data} \n\nCreate a table using the | character from the above text with {description}: \n\n | {column_names} |"
        print("sending prompt:", prompt)
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1012,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        response_text = response.get("choices", [{"text": ""}])[0].get("text","")
        response_text = f"| {column_names} |\n {response_text}"
        print("parse_data_to_table got_response ",response_text)
        accepted_parse = input("Does the data look right? (y/n) ")

        if accepted_parse == "y":
            save_to_file(f"./table_data/{column_names}{description}.csv", response_text)
            accepted_response = "n"
    return response_text

## parses any table with a | character
def parse_table_text(table_text,column_names):
    rows = table_text.split("\n")
    rows = [row.split("|") for row in rows]
    rows = [row for row in rows if len(row) > 1]
    ## sometimes the last column or first column is empty, but not always, so we remove those when they are
    for row in rows:
        if row[0] == "":
            row.pop(0)
        if row[-1] == "":
            row.pop(-1)

    column_names = column_names.split("|")
    ## loop over each row until we find the first row with alphabetical characters
    start = 0
    for row in rows:
        start += 1
        print(row)
        if len(row) > 0 and any(char.isalpha() for char in row[0]):
            print("start is ", start)
            break
    rows = rows[start:]
    table = []
    for row in rows:
        element = {}
        if len(row) == len(column_names):
            for i in range(len(column_names)):
                ## check to see if the value contains "--"
                if "--" not in row[i]:
                    print(i,row[i],column_names[i])
                    element[column_names[i]] = row[i]
            table.append(element)
    print("parsed table", table)
    return table


# mocks

table_text = """
|Topic|Subtopic|
|:--|:--|
|Introduction to NumPy|What is NumPy?|
|Introduction to NumPy|Benefits of using NumPy|
|Introduction to NumPy|Key features of NumPy|
|NumPy Arrays|Creating NumPy arrays|
|NumPy Arrays|Indexing and slicing NumPy arrays|
|NumPy Arrays|Manipulating NumPy arrays|
|NumPy Array Operations|Mathematical operations with NumPy arrays|
|NumPy Array Operations|Logical operations with NumPy arrays|
|NumPy Array Operations|Set operations with NumPy arrays|
|NumPy Broadcasting|What is Broadcasting?|
|NumPy Broadcasting|Rules of Broadcasting|
|NumPy Broadcasting|Broadcasting examples|
|NumPy Linear Algebra|NumPy matrix objects|
|NumPy Linear Algebra|Matrix operations with NumPy|
|NumPy Linear Algebra|Determinants and inverses with NumPy|
|NumPy Random Numbers|Generating random numbers with NumPy|
|NumPy Random Numbers|Probability distributions with NumPy|
|NumPy Random Numbers|Permutations and combinations with NumPy|
|NumPy Reading and Writing Data|NumPy binary files|
|NumPy Reading and Writing Data|NumPy text files|
|NumPy Reading and Writing Data|CSV files with NumPy|
|NumPy Advanced Topics|NumPy masked arrays|
|NumPy Advanced Topics|NumPy structured arrays|
|NumPy Advanced Topics|NumPy dates and times|
|NumPy Advanced Topics|Plotting with NumPy|
"""

table_text_2 = """
| topic|subtopic|day_number|week_number |
 
 
 | —————|—————————————-|————————————-|—————————————-| 
 |Introduction to NumPy|What is NumPy?|1|1| 
 |Introduction to NumPy|Why is NumPy useful?|1|1| 
 |Introduction to NumPy|Basic NumPy functions|1|1| 
 |Interpreting data using NumPy|How to read in data using NumPy|2|1| 
 |Interpreting data using NumPy|How to manipulate data using NumPy|2|1| 
 |Interpreting data using NumPy|How to visualize data using NumPy|2|1| 
 |Analyzing data using NumPy|Basic statistical analysis with NumPy|3|1| 
 |Analyzing data using NumPy|Advanced statistical analysis with NumPy|3|1| 
 |Evaluating data using NumPy|How to perform hypothesis testing with NumPy|1|2| 
 |Evaluating data using NumPy|How to create predictive models with NumPy|1|2| 
 |Evaluating data using NumPy|How to validate models with NumPy|1|2| 
 |Applying NumPy in real-world scenarios|NumPy case studies|2|2| 
 |Applying NumPy in real-world scenarios|Hands-on practice with NumPy|2|2| 
 |Applying NumPy in real-world scenarios|Q&A with instructor|2|2| 
 |Project work day|-|3|2|
"""

