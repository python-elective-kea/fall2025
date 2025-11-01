
# Pythons Datamodel

I dag vil vi se på Pythons datamodel.

Python har en protokolorienteret datamodel.

Efter dette vil du være i stand til at implementere kode i dine egne klasser, der gør det muligt at bruge Pythons indbyggede funktioner eller topniveau-syntaks til at interagere med disse objekter.

**Eksempel:**

Hvis du vil kunne bruge den indbyggede funktion `len()` på dit objekt, skal du implementere `__len__` metoden i din klasse.

Hvis du vil kunne bruge `==` operatøren på dit objekt, skal du implementere `__eq__` metoden i din klasse.

Hvis du vil kunne bruge `in` nøgleordet på dit objekt, skal du implementere `__contains__` metoden i din klasse.


## Læringsmål

* Opret dine egne klasser, der opfører sig som ethvert andet Python-objekt og er i stand til at interagere med Pythons buildin functions eller top level syntaks.

## Forberedelse
I dag har i lidt forskellige muligheder som i kan vælge at dykke ned i, i forbindelse med forberedelsen til undervisning. 

I skal alle se 18 mnutter af denne video: 
* [What Does It Take To Be An Expert At Python?](https://www.youtube.com/watch?v=7lmCu8wz8ro)
   * Dette er et foredrag om ekspert Python-programmering, og dette er det, vi vil dække resten af dette semester. (Dagens emne er fra starten til 18:43)

Hvis den forrige video var lidt abstrakt og svær at forstå kan i med fodel kigge denne video igennem.
* [Expert Python Tutorial #2 - Dunder/Magic Methods & The Python Data Model](https://www.youtube.com/watch?v=z11P9sojHuM)

Den næste giver et godt overblik over en del magic methods of forklarer hvordan man invokerer dem. 
* [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/)

Og til dig der vil have en grundig introduktion til emnet kan i læse kapitlet herunder
* [The Python Data Model](The_Python_Data_Model.pdf)

## Dagen i dag

* [Notebook on Datamodel](notes_OOP_datamodel.ipynb#Datamodel)
* [Money datamodel demo](money.ipynb)
* [Build in functions to Datamodel methods relation table](build_to_dunder.md)

## Øvelser

# Øvelser

## Ex1: Deck of cards

[Solution](exercises/solution/06_datamodel/solutions.rst)

Fortsæt med deck-eksemplet og implementer

* `__len__` metoden
* `__add__` metoden
* `__repr__` metoden
* `__str__` metoden
* `__setitem__` metoden
* `__delitem__` metoden

Vi ser på dette sammen om et øjeblik.

Når du er færdig, så kig på øvelsen nedenfor og stil dine spørgsmål.

## Ex2: Number Class

```python
class Number:
    def __init__(self, num, obj_name):
        self.num = num
        self.obj = obj_name

a = Number(5, 'a')
b = Number(-4, 'b')
```

Baseret på denne klasse, opret en Number, der opfører sig som en int klasse, men med den ekstra parameter at indsætte et variabelnavn.
Klassen skal mindst kunne lægges sammen, trækkes fra, ganges og divideres.

## Linked List

[Linked List](protocol_linked_list.md)

## Point class
Med denne kode som udgangspunkt
````
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
````
Gør objectet i stand til at bruge +,-,* operatorene.
Feks. med denne brug af objektet:

````
    v1 = Point(1,2)
    v2 = Point(2,3)
    v3 = v1 + v2
    >>>
````

<!--
* [Notebook demo Value class in teachings](notebooks/oop_lecture_value_graphviz.ipynb)
-->