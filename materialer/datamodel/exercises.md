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

[Linked List](exercises/protocol_linked_list.rst)

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

