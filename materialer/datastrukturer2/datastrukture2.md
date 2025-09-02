# Datastrukture \{sets og dictionaries\}

Vi fortsætter legen med datastrukturer og vil i dag have fokus på Sets og Dictionaries.

## Læringsmål
     
- Arbejde med dicts, sets, lister og tupler
- Kunne arbejde med dict og set comprehensions
- Kunne bruge pythons `ittertools` module

## Forberedelse

* [Se de første 7 videoer i denne playliste](https://youtube.com/playlist?list=PLDDGPdw7e6Ag1EIznZ-m-qXu4XX3A0cIz&si=ZvB5iD6OeP284C5-) (1 time 15 min)
    * Dette er ikke pythonkodevideoer, men baggrundsstof. I skal ikke kunne dette til perfektion, men i skal i første omgang have set videoerne (ligesom hvis i skimmer en tekst) og så kan i bruge dem som opslagsværk senere.

Herefter se disse 2 videoer om "Sets og Dicts in python"

* [Sets in Python || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=sBvaPopWOmQ&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=13) (6:33)

<!--
Til sidst skal du gennemgå sektion 5.1, 5.2 og 5.3 om set teori og python i det følgende

* [Discrete Math - GeoigiaSet Theory](https://ggc-discrete-math.github.io/set_theory.html)
-->
* [Python Dictionaries || Python Tutorial || Learn Python Programming](https://www.youtube.com/watch?v=XCcpzWs-CI4&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-&index=15) (6:08)

## Dagens indhold

Vi starter med en opsumering af Set teori, og forbinder det til python sets.    
Herefter arbejder vi med øvelerne herunder til i dag.

* [Kodeeksempler og øvelser fra undervisningen](kode_fra_undervisningen.ipynb)


<!--
## Materialer
* [Efficient Use of Python Data Structures](https://blog.appsignal.com/2025/05/28/ways-to-optimize-your-code-in-python.html#efficient-use-of-python-data-structures) (læs kun afsnittet, ikke hele artiklen)
* [Utilize List Comprehensions and Generator Expressions](https://blog.appsignal.com/2025/05/28/ways-to-optimize-your-code-in-python.html#utilize-list-comprehensions-and-generator-expressions) (læs kun afsnittet, ikke hele artiklen)
* [Leveraging Built-in Functions and Libraries](https://blog.appsignal.com/2025/05/28/ways-to-optimize-your-code-in-python.html#leveraging-built-in-functions-and-libraries) (læs kun afsnittet, ikke hele artiklen)
-->

### Øvelser

#### Øv 1: subset ($\subset$) og perfect subset ($\subseteq$)

På baggrund af disse 2 sets kan du finde ud af om de er ens ved hjælp af `==` opratoren.

````
    p = {1, 2, 3, 4, 5}
    q = {1, 2, 3, 4, 5}

````
Du vil også kunne finde ud af om de er ens ved hjælp af subset ($\subset$) og perfect subset ($\subseteq$). 

**Lav dette med python kode.**

(lav det først med set **metoderne** og derefter med set **opratorene**).

#### Ex 4: Tøjliste Comprehension
Den første del af denne øvelse har du lavet sidste uge (hvis ikke skal du lave den nu).

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

### Set, Dict øvelser

* [Dictionary](exercises/dict.ipynb)
* [Set](exercises/set.ipynb)
* [Lotto](exercises/lotto.ipynb)
* [Word count](https://github.com/python-elective-kea/fall2020/tree/master/sphinx/source/exercises/dict_exercises/count_words_in_file)

<!--
#### quizes
* [Lists and Tuples Quiz](https://realpython.com/quizzes/python-lists-tuples/)
* ["while" Loops Quiz](https://realpython.com/quizzes/python-while-loop/)
-->