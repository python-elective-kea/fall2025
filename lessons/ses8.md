
Session 9 - The Python Datamodel
================================

I dag vil vi se på Python datamodellen.

Python har en protokolorienteret datamodel.

Efter dette vil du være i stand til at implementere kode i dine egne klasser, der gør det muligt at bruge Pythons indbyggede funktioner eller topniveau-syntaks til at interagere med disse objekter.

**Eksempel:**

Hvis du vil kunne bruge den indbyggede funktion :code:`len()` på dit objekt, skal du implementere :code:`__len__` metoden i din klasse.

Hvis du vil kunne bruge :code:`==` operatøren på dit objekt, skal du implementere :code:`__eq__` metoden i din klasse.

Hvis du vil kunne bruge :code:`in` nøgleordet på dit objekt, skal du implementere :code:`__contains__` metoden i din klasse.


Læringsmål
--------------

    * Opret dine egne klasser, der opfører sig som ethvert andet Python-objekt og er i stand til at interagere med Pythons indbyggede funktioner eller topniveau-syntaks.

Materialer
---------

* [What Does It Take To Be An Expert At Python?](https://www.youtube.com/watch?v=7lmCu8wz8ro)
   * Dette er et foredrag om ekspert Python-programmering, og dette er det, vi vil dække resten af dette semester. (Dagens emne er fra starten til 18:43)
* [The Python Data Model](_static/The_Python_Data_Model.pdf)
* [A Guide to Python's Magic Methods](https://rszalski.github.io/magicmethods/)
* [Expert Python Tutorial #2 - Dunder/Magic Methods & The Python Data Model](https://www.youtube.com/watch?v=z11P9sojHuM)
* [Build in functions to Datamodel methods relation table](notebooks/build_to_dunder.rst)
* [Notebook on Datamodel](notebooks/OOP_Encapsulation_Propeties.ipynb#Datamodel)
* [Code examples from teachings](https://github.com/python-elective-kea/fall2023-code-examples-from-teachings/tree/master/ses9)
.. * [Notebook demo Value class in teachings](notebooks/oop_lecture_value_graphviz.ipynb)

Øvelser
---------

------------------
Ex1: Deck of cards
------------------

[Solution](exercises/solution/06_datamodel/solutions.rst)

Fortsæt med deck-eksemplet og implementer

* :code:`__len__` metoden
* :code:`__add__` metoden
* :code:`__repr__` metoden
* :code:`__str__` metoden
* :code:`__setitem__` metoden
* :code:`__delitem__` metoden

Vi ser på dette sammen om et øjeblik.

Når du er færdig, så kig på øvelsen nedenfor og stil dine spørgsmål.


-----------------
Ex2: Number Class
-----------------

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


---

* [Linked List](exercises/protocol_linked_list.rst)
..
   * [Jelly Beans](exercises/JellyBeans.rst)

