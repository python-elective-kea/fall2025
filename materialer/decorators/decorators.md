# Session 6 - Functions & Decorators

I Python bruges decorators ofte til at udvide funktionaliteten af eksisterende kode. Du har tidligere arbejdet med Spring Framework´et, og du kender derfor allerede til dette koncept. I Spring kan du tilføje ekstra funktionalitet til din eksisterende kode ved at annotere den med fx `@Controller` eller `@Autowired`. På samme måde kan du i Python tilføje ny funktionalitet til din kode ved at dekorere funktioner eller klasser med ekstra kode. Dette kan gøre din kode mere modulær og nemmere at vedligeholde, da du kan adskille forskellige hensyn i separate decorators.

Den grundlæggende syntaks for en decorator ser sådan ud:

```python
def decorator(func):
    def wrapper_decorator(*args, **kwargs):
        # Gør noget før
        value = func(*args, **kwargs)  # udfør funktionen
        # Gør noget efter
        return value

    return wrapper_decorator
```

Og hvis du vil bruge den, gør du sådan her:

```python
@decorator
def greet(name):
    return 'Hello ' + name
```

Vi starter med at bruge en ny editor, Jupyter Notebook.

## Læringsmål

Ved at læse teksterne i materialesektionen, lave de 3 øvelser og følge undervisningen, vil du kunne forklare hvad en decorator er, hvornår den skal bruges, og hvordan de indre dele af en decorator-funktion er opbygget. Du vil også kunne lave dine egne decorators og bruge andres.

Efter denne uge vil du kende til og kunne bruge og forklare:

- First class functions / Higher order functions
- Inner functions
- Decorator functions
  - forklare hvordan en decorator-funktion virker
  - forstå og kunne forklare hvad returværdier og returtyper er for de forskellige funktioner brugt i en decorator
  - forstå hvorfor vi genbruger variabelnavne i et scope

## Materialer

- [Primer on Python Decorators](https://realpython.com/primer-on-python-decorators/)
- [Python Inner Functions—What Are They Good For?](https://realpython.com/inner-functions-what-are-they-good-for/)
- [Nested functions in Python](https://www.pythonmorsels.com/nested-functions/)
- [Notebook on Decorators](notebooks/Decorators.ipynb)
- [Kode fra undervisningen](kode_fra_undervisningen.ipynb)
- [Øvelser](exercises.md)

<!--
- [Code examples from teachings](https://github.com/python-elective-kea/spring2023-code-examples-from-teachings/tree/master/ses6) 
-->