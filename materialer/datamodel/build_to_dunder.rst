Build in functions & top level syntax
=====================================

and their corosponding data model methods.



Build in functions and their data model methods
-----------------------------------------------



.. list-table:: Build in functions and their data model methods
   :widths: 25 25
   :header-rows: 1
   :class: full-width

   * - Build in function
     - Data model method
   * - len()
     - `__len__(self)`
   * - str()
     - `__str__(self)`
   * - repr()
     - `__repr__(self)`
   * - abs()
     - `__abs__(self)`
   * - bool()
     - `__bool__(self)`
   * - int()
     - `__int__(self)`
   * - float()
     - `__float__(self)`
   * - round()
     - `__round__(self)`
   * - iter()
     - `__iter__(self)`
   * - next()
     - `__next__(self)`
   * - getitem()
     - `__getitem__(self, index)`
   * - setitem()
     - `__setitem__(self, index, value)`
   * - delitem()
     - `__delitem__(self, index)`
   * - contains()
     - `__contains__(self, item)`
   * - enter()
     - `__enter__(self)`
   * - exit()
     - `__exit__(self, exc_type, exc_val, exc_tb)`

Example:
--------

So when you use the len() build in function, you are calling the __len__() method of the object.


.. code:: python
   :linenos:

   class Person:
     def __init__(self, name, height):
        self.name = name
        self.height = height 

     def __len__(self):
        return self.height

   x = Person('Claus', 180)
   len(x)    # this is calling/executing the __len__() method.


Top level syntax and their corosonding datamodel methods
--------------------------------------------------------

.. list-table:: Top-level syntaks og Dundermetoder
   :widths: 50 50
   :header-rows: 1
   :class: full-width

   * - Top-level syntaks
     - Dundermetode
   * - x + y
     - `__add__(self, other)`
   * - x - y
     - `__sub__(self, other)`
   * - x * y
     - `__mul__(self, other)`
   * - x / y
     - `__truediv__(self, other)`
   * - x // y
     - `__floordiv__(self, other)`
   * - x % y
     - `__mod__(self, other)`
   * - x ** y
     - `__pow__(self, other)`
   * - x == y
     - `__eq__(self, other)`
   * - x != y
     - `__ne__(self, other)`
   * - x > y
     - `__gt__(self, other)`
   * - x < y
     - `__lt__(self, other)`
   * - x >= y
     - `__ge__(self, other)`
   * - x <= y
     - `__le__(self, other)`
   * - x(x1, x2)
     - `__call__(self, *args, **kwargs)`
   * - x[index]
     - `__getitem__(self, index)`
   * - x[index] = value
     - `__setitem__(self, index, value)`
   * - del x[index]
     - `__delitem__(self, index)`
   * - x in y
     - `__contains__(self, item)`
   * - with x as y:
     - `__enter__(self)` and `__exit__(self, exc_type, exc_val, exc_tb)`
 




Example:
--------

So when you use the + sign, you are calling the __add__() method of the object.


.. code:: python
   :linenos:

   class Person:
        def __init__(self, height):
          self.height = height
        def __add__(self, other):
          return Person(self.height/2 + other.height/2)

   x = Person(180)
   y = Person(162)
   x + y    # the + sign is calling/executing the __add__() method.
