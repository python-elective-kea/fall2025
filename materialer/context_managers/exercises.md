# Exercises

## 1. Coroutine to Compute a Running Average

Change the function below into a coroutine (generator) that calculates a running average. So instead of returning an average based on the parameter it should calculate an average based on the values inserted into the coroutine with the `.send()` method.

```python
def averager(*args):
    sum = 0
    for i in args:
        sum += i
    return sum / len(args)
```

## 2. Context manager class

Create a class "Makeparagraph" that "decorates" a text with an HTML `<p>` tag.

## 3. contextlib

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

## JSON 10 minutes exercise

[JSON 10 minutes exercise](notebooks/JSON.html#10-minutes-exercise)

## SQLite 10 minutes exercise

[SQLite 10 minutes exercise](notebooks/Sqlite.html#10-minutes-exercise)

## ConvertCSVtoJSON

[ConvertCSVtoJSON](notebooks/ConvertCSVtoJSON.ipynb) ([Solution](exercises/solution/10_context_managers/SolutionConvertCSVtoJSON.ipynb))

## Decorator / Context Manager

[Decorator / Context Manager](notebooks/Assignment_Decorator_Context_Manager.ipynb) ([Solution](exercises/solution/10_context_managers/Assignment_Decorator_Context_Manager.ipynb))
