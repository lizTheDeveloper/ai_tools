
    # using the `.env` package to manage environment variables
     - Let's say you have a `.env.development` file with your development database credentials: 
```
DB_USERNAME=foo
DB_PASSWORD=bar
```

 - And you want to access those credentials in a Python script: 
```python
import os

USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
```

 - If you try to run the Python script now, you'll get an error because the `.env` file hasn't been loaded yet: 
```
Traceback (most recent call last):
  File "test.py", line 4, in <module>
    USERNAME = os.getenv("DB_USERNAME")
  File "/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py", line 678, in getenv
    return map.get(key)
  File "/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7/lib/python3.7/os.py", line 725, in __getitem__
    raise KeyError(key) from None
KeyError: 'DB_USERNAME'
```

 - In order to load the `.env` file, you need to install the `python-dotenv` package: 
```
$ pip install python-dotenv
```

 - Then you can tell Python to load the `.env.development` file before accessing the environment variables: 
```python
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
```

 - Now when you run the Python script, it will load the `.env.development` file and you'll be able to access the environment variables: 
```
$ python test.py
foo
bar
```

 - You can also specify the path to the `.env` file: 
```python
load_dotenv(".env.development")
```

 - Or you can tell Python to look for the `.env` file in the current directory: 
```python
load_dotenv(override=True)
```
    ### When might you need to using the `.env` package to manage environment variables?
    
1. When developing a Node.js application that needs to use environment variables for things like API keys or passwords.
2. When deploying a Node.js application to a server where you want to be able to set environment variables.
3. When working with a Node.js application that has been packaged with webpack and you want to be able to set environment variables.

    This might look like:

    
1. When developing a Node.js application that needs to use environment variables for things like API keys or passwords, you might set environment variables in your development environment so that you can test your application with real data.
2. When deploying a Node.js application to a server, you might want to set environment variables on the server so that your application can use them.
3. When working with a Node.js application that has been packaged with webpack, you might want to set environment variables in your webpack configuration so that your application can use them.

    ### How do you practice using the `.env` package to manage environment variables?
    
1. Create a file named `.env` in the root directory of your project
2. Add the following line to your `.env` file:

```
TEST=123
```

3. Install the `.env` package:

```
$ npm install --save .env
```

4. Require the `.env` package in your project:

```
var Env = require('../.env');
```

5. Access the `TEST` environment variable:

```
console.log(Env.TEST); // 123
```

    ### How do you practice using the `.env` package to manage environment variables in Python?
    

# The contents of that `.env` file would then be loaded into the `os.environ` dictionary. If a key already exists in `os.environ`, it will be overwritten.

# With the `.env` file created and your environment variables loaded, you can then access them like normal environment variables.

# ```python
# import os
# 
# database_url = os.environ['DATABASE_URL']
# api_key = os.environ['API_KEY']
# ```

# To load environment variables from a `.env` file when running locally, you can use the `python-dotenv` package:

# ```python
# # my_script.py
# 
# import os
# from dotenv import load_dotenv
# 
# load_dotenv()
# 
# database_url = os.environ['DATABASE_URL']
# api_key = os.environ['API_KEY']
# ```
import os



















 
 
 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 
from dotenv import load_dotenv
    