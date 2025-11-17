Session 11 - Context Managers
=============================

Today we will work with **Context Managers**.

Context managers can in short be described as something that takes care of the related tasks of a specific task. An example of this could be when opening a file, the context manager takes care of automatically closing the file when we are finished using it.

You will make your own context managers and use already created ones.

Learning goals
--------------

- Being able to use a Context Manager
- Creating your own Context Managers
- Using a context manager in relation to Working with JSON, Pickles and CSV files.
- Using a context manager in relation to working with a SQLite database.

Materials
---------

* [What Does It Take To Be An Expert At Python?](https://www.youtube.com/watch?v=7lmCu8wz8ro&t=4962s) *(good and advanced recap of what we covered in the teachings. Skip the Meta Classes part in the start of the video)*
* [Context Managers notebook](notebooks/Context-managers.ipynb)
* [JSON notebook](JSON.ipynb)
* [CSV notebook](csv.ipynb)
* [Sqlite notebook](Sqlite.ipynb)
* [Code examples from teachings](/materialer/context_managers/kode_fra_undervisningen.ipynb)

## Exercises

### 1. Coroutine to Compute a Running Average

Change the function below into a coroutine (generator) that calculates a running average. So instead of returning an average based on the parameter it should calculate an average based on the values inserted into the coroutine with the `.send()` method.

```python
def averager(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)
```

### 2. Context manager class

Create a class "Makeparagraph" that "decorates" a text with an HTML `<p>` tag.

### 3. contextlib

In the code example below we can see that the `connect()` function is a context manager. It has `__enter__` and `__exit__` methods, and therefore works together with the "with" keyword.

```python
from sqlite3 import connect

with connect('testfiles/school.db') as conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE students(id int PRIMARY KEY, name text, cpr text)')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (1, "Claus", "223344-5566")')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (2, "Julie", "111111-1111")')
    cur.execute('INSERT INTO students(id, name, cpr) VALUES (3, "Hannah", "222222-2222")')

    for i in cur.execute('SELECT * FROM students'):
        print(i)

    cur.execute('DROP TABLE students')
```

The "CREATE TABLE" and the "DROP TABLE" have also some `__enter__` / `__exit__` logic behind it.
Put this logic into its own context manager and use it. This should be done by using the `contextmanager` decorator from the `contextlib` library.

### JSON 10 minutes exercise

[JSON 10 minutes exercise](notebooks/JSON.html#10-minutes-exercise)

### SQLite 10 minutes exercise

[SQLite 10 minutes exercise](notebooks/Sqlite.html#10-minutes-exercise)

### ConvertCSVtoJSON

[ConvertCSVtoJSON](notebooks/ConvertCSVtoJSON.ipynb) ([Solution](exercises/solution/10_context_managers/SolutionConvertCSVtoJSON.ipynb))

### Decorator / Context Manager

[Decorator / Context Manager](notebooks/Assignment_Decorator_Context_Manager.ipynb) ([Solution](exercises/solution/10_context_managers/Assignment_Decorator_Context_Manager.ipynb))
