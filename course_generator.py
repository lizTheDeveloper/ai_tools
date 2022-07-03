from numpy import number

import os

import openai

def generate_course(topic,number_of_weeks,hours_per_week,target_job):
    competencies = competencies_from_course_generator(topic,target_job,number_of_weeks,hours_per_week)
    course_outline = course_from_topic_generator(topic,competencies,number_of_weeks,hours_per_week)
    competencies_table = course_topic_outline_parser(competencies_table)
    topics_table = competencies_to_table_parser(course_outline)

    return competencies_table

## course definitions
## generates a backwards-designed list of competencies based on a topic
def course_from_topic_generator(topic,competencies,number_of_weeks,hours_per_week):
    total_hours = hours_per_week * number_of_weeks
    prompt = f"Create the outline of a {number_of_weeks}-week, {total_hours}-hour course on {topic} that covers the following competencies: \n\n {competencies}"

    return natural_language_prompt(prompt)

## generates a course outline that is backwards-designed against competencies
def competencies_from_course_generator(course_name,target_job,number_of_weeks,hours_per_week):
    total_hours = hours_per_week * number_of_weeks
    competency_low_range = number_of_weeks
    competency_high_range = total_hours * 2
    prompt = f"After a {total_hours}-hour course in {course_name}, what {competency_low_range}-{competency_high_range} competencies should a learner who wants to become a {target_job} have learned? Do not use the words Understand, Understanding, Know, Fluency, or Using to describe the competencies, instead use a Bloom's Taxonomy Verb (e.g., Apply, Analyze, Create, etc.) \n\n"
    return discerning_natural_language_prompt(prompt)

## generate a module overview from the topic
def module_overview_from_topic(topic):
    prompt = f"Create a module overview for {topic} \n\n"
    module_overview = natural_language_prompt(prompt)

def module_from_competencies_in_week(competencies):
    prompt = f"Create a module overview for the week, where we'll cover {competencies} \n\n"
    module_overview = natural_language_prompt(prompt)



    return """
    # Module Overview 
    This week we'll be covering the following competencies:
    {competencies}

    {module_overview}


    """

def generate_short_article(topic):
    prompt = f"Write a 500-word article that describes {topic} \n\n"
    return natural_language_prompt(prompt)

def generate_scenarios_for_competency(competency):
    prompt = f"Name 3 simple scenarios in which you might need to {competency} \n\n"
    return discerning_natural_language_prompt(prompt)

def generate_concrete_examples_from_scenarios(scenarios):
    prompt = f"{scenarios} \n\n Name 3 example tasks in a real job where you might do the above scenarios?\n\n"
    return discerning_natural_language_prompt(prompt)

def generate_practice_exercise(competency):
    prompt = f"Create a short exercise to practice {competency} \n\n"
    return natural_language_prompt(prompt)

def competencies_from_learning_content(learning_content):
    prompt = f"What competencies does the above learning content cover? Do not use the words Understand, Know, Fluency, or Using to describe the competencies, instead use a Bloom's Taxonomy Verb (e.g., Apply, Analyze, Create, etc.)"
    return natural_language_prompt(prompt)


def natural_language_prompt(prompt):
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
    print("got_response", response_text)
    return response_text

def code_example_prompt(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1012,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response.get("choices", [{"text": ""}])[0].get("text","")
    return response_text

def discerning_natural_language_prompt(prompt):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0.24,
        presence_penalty=0.23
    )
    response_text = response.get("choices", [{"text": ""}])[0].get("text","")
    print(response_text)
    return response_text

### Parsers 
def parse_data_to_table(data,column_names,description):
    prompt = f"{data} \n\nCreate a table using the | character from the above text with {description}: \n\n | {column_names} |"
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
    return "| {column_names} |\n" + response_text

#### subtopic parser, gets a table of subtopics to generate module overviews with
def course_topic_outline_parser(response_text):
    return parse_data_to_table(response_text,"topic|subtopic","every subtopic associated with its topic")
    

## generate a table of competencies from generated competencies
def competencies_to_table_parser(response_text):
    return parse_table_text(parse_data_to_table(response_text,"competency|level","each competency above and its level according to Bloom's Taxonomy"))

def weekly_outline_to_table_parser(response_text):
    return parse_table_text(parse_data_to_table(response_text,"competency|week_number","each competency above and its week number"))

## parses any table with a | character
def parse_table_text(table_text):
    rows = table_text.split("\n")
    rows = [row.split("|") for row in rows]
    column_names = rows[1][1:-1]        
    rows = rows[2:]
    rows = [row[1:-1] for row in rows]
    table = []
    for row in rows:
        element = {}
        if len(row) == len(column_names):
            for i in range(len(column_names)):
                print(i,row[i],column_names[i])
                element[column_names[i]] = row[i]
                table.append(element)
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