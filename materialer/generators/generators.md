
Session 10 - Generators
=======================

I dag vil du lære, hvordan du gør dine klasser iterable. Du vil lære, hvordan du opretter en generatorfunktion og hvordan du skriver dette på en lettere læselig måde ved hjælp af et generatorexpression. Du vil også få indsigt i, hvorfor en funktion i Python er et objekt, og hvordan du gør dit eget objekt callable.

Vi vil se på Iterator-klasser

```python
class Compute:
    def __iter__(self):
        self.last = 0
        return self

    def __next__(self):
        rv = self.last
        self.last += 1
        if self.last > 10:
            raise StopIteration()
        sleep(.5)
        return rv

for i in Compute():
    print(i)
```

Og se, hvordan det kan gøres på en lettere læselig og brugbar måde med en generatorfunktion

```python
def compute():
    for i in range(10):
        yield i
```

Og skriv et generatorudtryk.

```python
(i for i in range(10))
```

Læringsmål
----------

- Forstå, hvordan funktioner er abstrakteringer af en klasse.
- Opret hukommelses- og tidsbesparende kode ved hjælp af:
  - Iterator-klasser
  - Generatorfunktioner og
  - Generatorudtryk.

Materialer
---------
* [Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/) (ekskl. Using Advanced Generator Methods & Creating Data Pipelines With Generators)
* [Code examples from teachings](https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses10)
* [Øvelser](exercises.md)


























.. _List Comprehension chalenges:

.. todo::

   * dataclasses - @dataclass - decorator for fast creation of classes
     * decorator classes.
       * __call__() method implementation
         * show the add() example:q
-->
