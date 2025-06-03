# Python - Datastrukture Sets og Dictionaries

Vi fortsætter med at arbejde med datastrukturer og vil i dag have fokus på Sets og dictionaries.

## Læringsmål
---        
- Arbejde med dicts, sets, lister og tuples
- Kunne bruge pythons `ittertools` module
- Kunne arbejde med dict og set comprehensions
- kunne bruge build in fuktioner som: `enumerate`, `range`

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
#### Ex. 3: Comprehensions
---

Alfabet List Comprehensions

1. Lav en liste af store bogstaver i det engelske alfabet
2. Lav en liste af store bogstaver fra det engelske alfabet, men udelad 4 med Unicode-kodepunktet enten 70, 75, 80, 85.
3. Lav en liste af store bogstaver fra det engelske alfabet, men udelad hvert andet bogstav mellem F & O

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
**Nested for loop**    
Først skal du lave det vha. et **nested for loop**.

**List comprehension**
Herefter ved hjælp af en list **comprehension**

**Sold out**
Herefter skal du fjerne de elemeneter der er i denne liste:

soldout = [('Black', 'm'), ('White', 's')]

Så hvis tuple-parret er i **souldout** listen, skal det ikke tilføjes til den genererede list comprehension.

**Øvelsen med sets**    
Lav nu øvelsen igen, men hvor colors, sizes og soldout er **sets** i stedet for lister. `colors = {'Black', 'White'}` etc.    
Du kan i princippet lave denne øvelse meget lig den forrige, men det er mere "effektiv" at bruge set operatorer til at lave "soldout"-delen af øvelsen.

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

* [Dictionary](../materialer/datastrukturer2/dict.ipynb)
* [Set](../materialer/datastrukturer2/set.ipynb)
* [Lotto](../materialer/datastrukturer2/lotto.ipynb)

#### quizes
* [Lists and Tuples Quiz](https://realpython.com/quizzes/python-lists-tuples/)
* ["while" Loops Quiz](https://realpython.com/quizzes/python-while-loop/)
