# Session 7 - OOP

Før denne lektion bør du have læst og forstået denne tekst [Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/). Dette er grundlæggende OOP koncepter, som du allerede har arbejdet med i den første del af din uddannelse. Du skal bare være opdateret med, hvordan dette gøres, og hvordan syntaksen er i Python.

I dag arbejder vi med det grundlæggende i objektorienteret programmering i Python.

## Læringsmål

Efter at have arbejdet med disse emner vil du kunne:

* oprette Classes, Objects, instance- og class-variabler, metoder og initializer-metoder.
* gøre brug af single og multiple inheritance.
* forklare hvornår og hvorfor du bruger classes og objects i stedet for procedure-stil.
* relatere den pythoniske OOP-stil til andre sprog (f.eks. Java).

## Dagen i dag
- [Notebook on classes](class_notes.ipynb)
- [Kodeeksempler fra undervisningen](kodeeksempler_fra_undervisningen.ipynb)
- [Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args/)

## Øvelser

## ØV 1: Bank Øvelse

Opret en Bank, en Konto, og en Kunde klasse.

* Alle klasser skal være i en enkelt fil.
* Bank klassen skal kunne indeholde mange konti.
* Du skal kunne tilføje nye konti.
* Konto klassen skal have relevante detaljer.
* Kunde klassen skal også have relevante detaljer.

Hold dig til de teknikker, vi har dækket indtil nu.

* Tilføj evnen for din **init** metode til at håndtere forskellige inputs (parametre).

## ØV 1a: Python færdigheder Evaluering

Kopier/ind sæt dette i "din" ChatGpt prompt.

```
    Jeg vil gerne have en score for, hvor godt min Python programmering er. Scoren skal være fra 1 til 10.

    Du skal give mig øvelser en ad gangen. Øvelsen skal løses med kode. Øvelserne skal matche det niveau, du tror, jeg er på.

    Du vil give øvelsen, og jeg vil give dig koden. For hver øvelse, skriv hvilket niveau du tror, jeg er på.

    Når du er sikker på mit niveau, generer en rapport. Rapporten skal indeholde følgende:
    1. Det niveau, du tror, jeg er på.
    2. Feedback på den kode, jeg skrev.
    3. Hvor jeg skal fokusere for at forbedre mig.

    Lad os starte med det første spørgsmål.
```


## ØV 2: Angry Bird

I denne øvelse skal du lave en simpel terminalversion af dette [Angry Bird online coding teaching tool for kids](https://studio.code.org/hoc/1>).

![assets/bird.png](angry_bird.png)

Du skal lave dette som en OOP applikation, og dine klasser kunne se sådan ud.

**Bird**

* Skal kende sin *current position* og hvilken *direction* den bevæger sig i.
* Den skal kunne *move forward*, *turn left* og *turn right*.
* Den skal også have en handling, der udføres når den taber, og en når den vinder.

**Pig**

* Skal kende sin *position*.
* Den skal også kunne udføre en handling, der udføres når den taber, og en når den vinder.

**Board**

* Skal initialisere et Bird- og et Pig-objekt.
* Den skal *display* boardet med bird og pig i startpositioner.
* Den skal have en *run method*:

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
* Den skal have en metode, der er ansvarlig for at skabe en samling af kommandoer fra brugerinput.

**Game**

* Denne klasse er ansvarlig for at køre applikationen. Den skal oprette objekter af Board og Workspace og kalde deres display-metoder. Den er også ansvarlig for at afgøre, om bird rammer pig eller ej.

---

Du kan se en prototype af denne øvelse her. Du er selvfølgelig velkommen til at forbedre spillet, men dette kunne være en løsning.

* [Angry Bird terminal](https://www.youtube.com/embed/n9Ths1CSCkU)