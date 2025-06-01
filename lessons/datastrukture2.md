# Python - Datastrukture Sets og Dictionaries

Vi fortsætter med at arbejde med datastrukturer og vil i dag have fokus på Sets og dictionaries.

## Læringsmål
---        
- Arbejde med dicts, sets, lister og tuples
    - Arbejde med deres indeks
    - Bruge slicing syntaksen
- Kunne arbejde med dict og set comprehensions

## Forberedelse
---
Før vi mødes i klassen skal du have set følgende videoer og løst de tilhørende forståelses opgaver vha. ChatGpt Prompten under linkene:

* [Se de første 7 videoer i denne playliste](https://youtube.com/playlist?list=PLDDGPdw7e6Ag1EIznZ-m-qXu4XX3A0cIz&si=ZvB5iD6OeP284C5-) (1 time 15 min)

Herefter se disse 2 videoer om sets og dicts i python

* [Sets in Python || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=sBvaPopWOmQ&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=13) (6:33)

* [Python Dictionaries || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=XCcpzWs-CI4&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=15) (6:08)


## Dagens indhold
---
Vi starter med en opsumering af emnerne for i dag, og kommer til at have fokus på:
* Hvad de forskellige datastrukturer bruges til. 
* Slicing og manipulation
* list comprehensions. 

Herefter arbejder vi ping pong med øvelerne til i dag.

* [Dictionary](../materialer/datastrukturer2/dict.ipynb)
* [Set](../materialer/datastrukturer2/set.ipynb)
* [Lotto](../materialer/datastrukturer2/lotto.ipynb)

## Materialer
---

* [Kodeeksempler og øvelser fra undervisningen](../materialer/ses2/)
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
