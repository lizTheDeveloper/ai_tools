
    # Install `pipenv` globally to manage our virtual environments
    

## Install pipenv

```
# Install pipenv to manage virtual environments
$ pip install pipenv

# Create a virtual environment
$ pipenv --python 3

# Activate the virtual environment
$ pipenv shell
```

## Install packages

```
# Install packages inside a virtual environment
$ pipenv install requests
```

## Deactivating

```
# Deactivate the virtual environment
$ exit
```

## Deleting

```
# Delete the virtual environment
$ pipenv --rm
```
    ### When might you need to Install `pipenv` globally to manage our virtual environments?
    
1. You are working on a project that requires multiple virtual environments.
2. You are working on a project that requires virtual environments with different versions of Python.
3. You are working on a project that requires virtual environments with different packages.

    This might look like:

    1. Working on a project that uses different versions of Django.
2. Working on a project that uses different versions of flask.
3. Working on a project that uses different versions of React.

    ### How do you practice Install `pipenv` globally to manage our virtual environments?
    
1. Install pipenv globally:

```
$ pip install pipenv
```

2. Create a new virtual environment with pipenv:

```
$ pipenv --python 3.7
```

3. Activate the virtual environment:

```
$ pipenv shell
```

4. Install a package in the virtual environment:

```
(my-env)$ pip install flask
```

    ### How do you practice Install `pipenv` globally to manage our virtual environments in Python?
    

# The pipenv can be used to create a new environment and install Django in it. The following command will create a virtualenv and install the given package (here, Django) in it:

$ pipenv install django

# To activate the virtualenv, we can use the following command:

$ pipenv shell

# To deactivate the virtualenv, we can use the following command:

$ exit

# To create a new Django project using pipenv , we can use the following command:

$ django-admin startproject test_project .

# To run a Django project using pipenv , we can use the following command:

$ python manage.py runserver
    