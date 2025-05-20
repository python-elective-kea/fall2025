# Session 7 - OOP

.. note:: Homework

Before this class you should have read and understood this text `Object-Oriented Programming (OOP) in Python 3 <https://realpython.com/python3-object-oriented-programming/>`\_. These are basic OOP concepts, which you have already worked with in the first part of your education. You just need to be up to date with how this is done, and how the syntax is done in python.

I dag arbejder vi med det grundlæggende i objektorienteret programmering i Python.

## Learning goals

Efter at have arbejdet med disse emner vil du kunne:

* oprette Classes, Objects, instance- og class-variabler, metoder og initializer-metoder.
* gøre brug af single og multiple inheritance.
* forklare hvornår og hvorfor du bruger classes og objects i stedet for procedure-stil.
* relatere den pythoniske OOP-stil til andre sprog (f.eks. Java).

## Materials

* `Object-Oriented Programming (OOP) in Python 3 <https://realpython.com/python3-object-oriented-programming/>`\_
* `Python args and kwargs: Demystified <https://realpython.com/python-kwargs-and-args/>`\_
* `Notebook on classes <notebooks/class_notes.ipynb>`\_
* `Code examples from teachings <https://github.com/python-elective-kea/spring2023-code-examples-from-teachings/tree/master/ses7>`\_

## Exercises

.. raw:: html

   <hr>

---

## EX 1: Bank Exercise

`Solution <exercises/solution/04_oop/solution.rst>`\_

Create a Bank, an Account, and a Customer class.

* All classes should be in a single file.
* The bank class should be able to hold many accounts.
* You should be able to add new accounts.
* The Account class should have relevant details.
* The Customer class Should also have relevant details.

Stick to the techniques we have covered so far.

* Add the ability for your **init** method to handle different inputs (parameters).

.. raw:: html

   <hr>

---

## Ex 1a: Python skills Evaluation

Copy/paste this in "your" ChatGpt prompt.
The recursing evaluation will work best with GPT4 (the paid version) but it is also ok with gpt3 (used by the free version)

.. code::

```
    I want to get a score of how well my python programming is. The score should be from 1 to 10.

    You should give me exercises one at a time. The exercise need to be solved with code. The exercises should match the level you think i am at.

    You will provide the exercise and i will give you code. For each exercise write what level you think i am at

    When you are confident of my level generate a report. The report should contain the following
    1. The level you think i am at
    2. Feedback on the code i wrote
    3. Where i should focus to improve

    Lets start with the first question   
```

---

## Ex 2: Angry Bird

`Solution <exercises/solution/04_oop/solution.rst>`\_

In this exercises you are going to create a simple terminal version of this `Angry Bird online coding teaching tool for kids <https://studio.code.org/hoc/1>`\_.

.. image:: \_static/angry\_bird.png

You should make this as an OOP application, and your classes could be like this.

**Bird**

* Skal kende sin *current position* og hvilken *direction* den bevæger sig i.
* Den skal kunne *move forward*, *turn left* og *turn right*.
* Den skal også have en action, der invokeres når den taber, og en når den vinder.

**Pig**

* Skal kende sin *position*.
* Den skal også have en action, der invokeres når den taber, og en når den vinder.

**Board**

* Skal initialisere et Bird- og et Pig-objekt.
* Den skal *display* boardet med bird og pig i startpositioner.
* Den skal have en *run method*:

.. code::

```
   *  *  *  *  *  *  *  *  *  *
   *  *  *  *  *  *  *  *  *  *
   *  *  B  *  *  *  *  *  *  *
   *  *  *  *  *  *  *  *  *  *
   *  *  *  *  *  *  *  *  *  *
   *  *  *  *  *  *  *  *  *  *
   *  *  *  *  *  *  *  *  *  *
   *  *  *  *  *  *  P  *  *  *
   *  *  *  *  *  *  *  *  *  *
   *  *  *  *  *  *  *  *  *  *
```

**Workspace**

* Skal have en display-metode, der udskriver instruktioner for, hvad man skal gøre.
* Den skal have en metode, der er ansvarlig for at skabe en samling af commands fra brugerinput.

**Game**

* Denne class er ansvarlig for at køre applikationen. Den skal oprette objekter af Board og Workspace og kalde deres display-metoder. Den er også ansvarlig for at afgøre, om bird rammer pig eller ej.

---

Screencast

---

Du kan se en prototype af denne øvelse her. Du er selvfølgelig velkommen til at forbedre spillet, men dette kunne være en løsning.

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/n9Ths1CSCkU" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
