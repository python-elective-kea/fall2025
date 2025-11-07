
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

og se på, hvordan det kan gøres på en lettere læselig og brugbar måde med en generatorfunktion.

```python
def compute():
    for i in range(10):
        yield i
```

Til sidst kigger vi også på hvordan vi kan gøre det samme med et genrator expression. 

```python
(i for i in range(10))
```

Læringsmål
----------

- Forstå, hvordan funktioner er "Abstractions" af en klasse.
- Opret hukommelses- og tidsbesparende kode ved hjælp af:
  - Iterator-klasser
  - Generatorfunktioner og
  - Generatorexpressions

Forberedelse
------------
* [What Does It Take To Be An Expert At Python?](https://www.youtube.com/watch?v=7lmCu8wz8ro)
* [Introduction to Python Generators](https://realpython.com/introduction-to-python-generators/) (ekskl. Using Advanced Generator Methods & Creating Data Pipelines With Generators)

Dagen i dag
-----------
* [Kodeeksempler fra undervisningen]()

## Øvelser

### Øvelse 1: Python Students

Baseret på Student-klassen nedenfor, opret en PythonStudents-klasse, der fungerer som en samling af studerende.
Klassen skal implementere iterationsprotokollen (iter(), next() og StopIteration).
Når PythonStudents-objektet itereres, skal det returnere navnet på hver studerende i listen.

```python
class PythonStudents:
    pass

class Student:
    def __init__(self, name, cpr):
        self._name = name
        self._cpr = cpr

    def __add__(self, student):
        return Student('Anna the daugther', 1234)

    def __str__(self):
        return f'{self._name}, {self._cpr}'

    def __repr__(self):
        return f'{self.__dict__}'
```

### Øvelse 2: School of students

I denne øvelse starter du med at have en liste over navne og en liste over fag.

Din opgave er at oprette:

1. En liste af ordbøger af studerende (f.eks.: students = [{'id': 1, 'name': 'Claus', 'major': 'Math'}]), oprettet i en normal funktion, der returnerer resultatet.

2. En generator, der "returnerer" et generatorobjekt. Så den studerende yields i stedet for at returnere.

Begge funktioner skal gøre det samme, men den ene returnerer en liste, og den anden returnerer et generatorobjekt.

| **students = [{'id': 1, 'name': 'Clasu', 'major': 'Math'}]**
| ID'et kan genereres af en tæller eller i en løkke.
| Navnet skal findes ved tilfældigt at vælge et navn fra navnelisten.
| Faget skal findes ved tilfældigt at vælge et fag fra faglisten.

```python
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def students_list(num_students):
    pass

def students_generator(num_students):
    pass

people = students_list(1000000)
people = students_generator(1000000)
```

### Øvelse 3: Range Mimic
1. Opret en "klon" af den indbyggede range()-funktion ved at lave en iterator-klasse.

I dokumentationen kan du læse følgende om range-funktionen.

```python
class range(start, stop, step=1)
Rather than being a function, range is actually an immutable sequence type, as documented in Ranges and Sequence Types — list, tuple, range.
```

Så range-funktionen er faktisk ikke en funktion, det er en klasse, der implementerer iteratorprotokollen.

```
>>> r = range(1, 10, 2)
>>> i = iter(r)
>>> next(i)
1
```

2. Gør det samme, men brug en generatorfunktion i stedet.

<!--
### Øvelse 4: List Comp chal as generators

Gør `List Comprehension chalenges`_ fra sidste gang, men brug nu generatorfunktioner og generatorudtryk, hvor det er muligt.
-->





<!--
* [Code examples from teachings](https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses10)
* [Øvelser](exercises.md)
-->

























.. _List Comprehension chalenges:

.. todo::

   * dataclasses - @dataclass - decorator for fast creation of classes
     * decorator classes.
       * __call__() method implementation
         * show the add() example:q
-->
