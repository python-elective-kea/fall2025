# Øvelser

## Øvelse 1: Python Students

[Løsning](exercises/solution/09_generators/solutions.rst)

Baseret på Student-klassen nedenfor, opret en PythonStudents-klasse, der fungerer som en samling af studerende.
Klassen skal implementere iterationsprotokollen (iter(), next() og StopIteration).
Når PythonStudents-objektet itereres, skal det returnere navnet på hver studerende i listen.

```python
class PythonStudents:
    pass

class Student:
    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
        return Student('Anna the daugther', 1234)

    def __str__(self):
        return f'{self.name}, {self.cpr}'

    def __repr__(self):
        return f'{self.__dict__}'
```

## Øvelse 2: School of students

[Løsning](exercises/solution/09_generators/solutions.rst)

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

## Øvelse 3: Range Mimic

[Løsning](exercises/solution/09_generators/solutions.rst)

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

## Øvelse 4: List Comp chal as generators

Gør `List Comprehension chalenges`_ fra sidste gang, men brug nu generatorfunktioner og generatorudtryk, hvor det er muligt.
