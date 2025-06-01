# Python - Datastrukture

I dag skal vi arbejde med pythons datastrukturer. Python har som udgangspunkt kun fire indbyggede datastrukture. Det er Lister, Tuples, Sets og Dictionaries.     
Efter i dag vil i være i stand til at oprette  Listes og Tupler, tilgå deres elementer vha. deres index, bruge pythons slicing værktøj på lister og tupler, bruge arethmetikske operatore på lister og tupler, bruge pythons indbyggede functioner på lister og tupler, arbejde med metoderne tilknyttet list og tuple objekterne, og i vil have en grundlæggende forståelse for forskellen i brugen af disse 2.     
I vil kunne bruge Sets til at finde unikke værdier i en collection, og i vil arbejde med Dictionaries og forstå dens key : Value struktur.

## Læringsmål
---        
- Arbejde med lister, tuples, dicts og sets
    - Arbejde med deres indeks
    - Bruge slicing syntaksen
- Kende til de vigtigste forskelle mellem lister, tuples, sets og dictionaries
- Kunne oprette lister vha. list comprehensions

## Forberedelse
---
Før vi mødes i klassen skal du have set følgende videoer og løst de tilhørende forståelses opgaver vha. ChatGpt Prompten under linkene:

* [Python Lists || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=ohCDWZgNIU0) (5:43)
   
> PROMPT: "I would like to have exercises in Python that focus on lists. Each exercise should cover one of the following topics: creating a list, accessing list elements, slicing, list methods, and using help() and dir(). Please give me one exercise at a time, evaluate my answer, and assign a grade from 1 to 10. Based on the evaluation and grade, provide me with another exercise that is either more challenging or easier. You should let me do the exercise before you provide me with any code solution." 

* [Python Tuples || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=NI26dqhs2Rk&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=16) (7:43)

> PROMPT: "I would like to have exercises in Python that focus on tuples. Each exercise should cover one of the following topics: Creating a tuple, getting tuple elements, unpacking tuples, help() and dir(). Please give me one exercise at a time, evaluate my answer, and assign a grade from 1 to 10. Based on the evaluation and grade, provide me with another exercise that is either more challenging or easier. You should let me do the exercise before you provide me with any code solution."

* [10 Python Comprehensions You SHOULD Be Using](https://www.youtube.com/watch?v=twxE0dEp3qQ)

> PROMPT: "I would like to have some exercises in python covering List Comprehensions. Each exercise should include one of the following topics: basic comprehension, if conditions, if/else conditions, nested loops, caling functions inside a comprehension. All exercises should make a relation between the for loop approch vs the comprehesion approach. You should give me one exercise at the time, and then evaluate my answer and grade it with a grade from 1 to 10. Then give me another exercise that is either harder or easier based on the evaluation and grade you gave me. You should let me do the exercise before you provide me with any code solution."

## Dagens indhold
---
Vi starter med en opsumering af emnerne for i dag, og kommer til at have fokus på:
* Hvad de forskellige datastrukturer bruges til. 
* Slicing og manipulation
* list comprehensions. 

Herefter arbejder vi ping pong med øvelerne til i dag.

* [list1](../materialer/datastrukturer1/list1.ipynb)
* [list2](../materialer/datastrukturer1/list2.ipynb)

## Materialer
---

* [Kodeeksempler og øvelser fra undervisningen](../materialer/datastrukturer1/)
* [Python Course at Kaggle](https://www.kaggle.com/code/colinmorris/hello-python)

### Øvelser

---
### 1: Is it a tuple or a list?
---
The following data should be presented as either a list or a tuple, or as a combination of both.      
Your job is to choose the right one.     
Hint: A list is a collection of the same type of data, a tuple is a record (e.g. in a database a **record** is called a **row**)     

1. Claus, 51, male, clbo@kea.dk, 31011970-1313
2. Bmw, Toyota, Hyundai, Skoda, Fiat, Volvo
3. Claus, Henning, Torben, Carl, Tine
4. 'Hello', 'World', 'Huston', 'we', 'are', 'here'
5. Rolling Stones, Goats Head Soup, 31 August 1973, 46:56
6. 40.730610, -73.935242, New York City, NY, USA; 31.739847, 65.755920, Kandahar, Kandahar Province, Afghanistan;

<hr>

---
#### Ex 2: Slicing
---
By using the slicing syntax change the following collections.

After slicing:

```
['Hello', 'World', 'Huston', 'we', 'are', 'here'] should become -> ['World', 'Huston', 'we', 'are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'World']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are', 'here']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['Hello', 'Huston', 'are']
['Hello', 'World', 'Huston', 'we', 'are', 'here'] -> ['here', 'are', 'we', 'Huston', 'World', 'Hello']
('Hello', 'World', 'Huston', 'we', 'are', 'here') should become -> ['World', 'Huston', 'we', 'are']
'Hello World Huston we are here' -> 'World Huston we'
``` 

Figure out more on your own and practice this a lot!    

<hr>

---
#### Ex. 3: Comprehensions
---

Alfabet List Comprehensions

Lav en liste af store bogstaver i det engelske alfabet

Lav en liste af store bogstaver fra det engelske alfabet, men udelad 4 med Unicode-kodepunktet enten 70, 75, 80, 85.

Lav en liste af store bogstaver fra det engelske alfabet, men udelad hvert andet bogstav mellem F & O

---
#### Ex 4: Tøjliste Comprehension
---

Udfra disse 2 lister:

````
colors = ['Black', 'White']
sizes = ['s', 'm', 'l', 'xl']
````
Skal du finde det der hedder 'Cartesian Product' hvilket vil sige du skal lave en liste der ser sådan ud:

```
    [(‘Black’, ‘s’), (‘Black’, ‘m’), (‘Black’, ‘l’), (‘Black’, ‘xl’), (‘White’, ‘s’), (‘White’, ‘m’), (‘White’, ‘l’), (‘White’, ‘xl’)]
```

Først skal du lave det vha. et **nested for loop**.

Herefter ved hjælp af en list **comprehension**

Herefter skal du fjerne de elemeneter der er i denne liste:

soldout = [('Black', 'm'), ('White', 's')]

Så hvis tuple-parret er i **souldout** listen, skal det ikke tilføjes til den genererede list comprehension.

**Øvelsen med sets**    
Lav nu øvelsen igen, men hvor colors, sizes og soldout er **sets** i stedet for lister. `colors = {'Black', 'White'}` etc.    
Du kan i princippet lave denne øvelse meget lig den forrige, men det kan være mere "effektiv" at bruge set operatorer til at lave "soldout"-delen af øvelsen.

**Øvelsen med brug af itertools**
Du kan også løse dette ved at importere modulet **itertools** og fra det modul bruge `product` functionen.
Prøv det og lig mærke til forskellen fra dine tidligere løsninger. 

---
#### Ex 5: List Comprehension øvelser
---
* Lav en liste af lige tal fra 0 til 20.
* Lav en liste af kvadrater af tal fra 1 til 10.
* Lav en liste af alle vokaler i en given streng.
* Lav en liste af fælles elementer i to givne lister.
* Lav en liste af ord fra en given streng, der har mere end 4 bogstaver.

### List & Tuples, Set, Dict øvelser
---
* [list1](../materialer/ses2/list1.ipynb)
* [list2](../materialer/ses2/list2.ipynb)
* [Dictionary](../materialer/ses2/dict.ipynb)
* [Set](../materialer/ses2/set.ipynb)

#### quizes
* [Lists and Tuples Quiz](https://realpython.com/quizzes/python-lists-tuples/)
* ["while" Loops Quiz](https://realpython.com/quizzes/python-while-loop/)
