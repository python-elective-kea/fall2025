# Øvelser

## Opvarmningsøvelser

Tænk over hver af følgende funktioner og afgør hvad der er deres:

- returværdi
- returtype
- parametertype
- parameterværdi

**eksempel1**

```python
def add():
    pass
```

**eksempel2**

```python
def add(num):
    return num + num
```

**eksempel3**

```python
def add(*args):
    return sum(args)
```

**eksempel4**

```python
def add(*args):
    if all(type(element) == type(args[0]) for element in args):
        return sum(args)
    return None
```

## Små Øvelser


Med denne funktion som udgangspunkt:

```python
def add(*args):
    return sum(args)
```

1. Skriv en decorator der skriver tidspunktet for hver gang denne funktion kaldes til en logfil.
2. Ændr log-decoratoren til også at udskrive værdierne af argumenterne sammen med timestamp.
3. Udskriv også resultatet af den dekorerede funktion til logfilen.
4. Lav en ny funktion kaldet `printer(text)` der tager en tekst som parameter og returnerer teksten. Dekorér den med din logfunktion. Virker det?

## Ex1: Time it!


Næste uge skal vi arbejde med *generators*, *generator expressions* og *list comprehensions*. Disse emner handler meget om programmets effektivitet.

I den forbindelse skal vi måle vores kode på forskellige måder, og især skal vi *"time det"* og *"måle memory usage"*.

Hvis du vil måle hvor lang tid det tager at køre et stykke kode, kan du gøre følgende:

```python
import time

start = time.time()
# gør noget du vil måle her
end = time.time()
print(end - start)
```

I stedet for at skrive dette hver gang du skal time noget, kan du skrive en decorator-funktion, der gør det for dig.

**Opgave:**

Din opgave er at skrive en decorator-funktion, der kan time ethvert stykke kode.

Du kan læse om `time` ved at starte din interpreter og skrive:

```python
import time
help(time)
```

## Ex3: Slow down code


Koden nedenfor tæller ned fra n -> 0. Hvis du kalder `countdown(5)` udskriver den: 5 4 3 2 1 Liftoff!

```python
def countdown(n):
    if not n:  # 0 er false, not false er true
        return n
    else:
        print(n, end=' ')
        return countdown(n-1)  # kald funktionen med n én mindre
```

**Opgave:**

Lav en decorator-funktion der sænker hastigheden på din kode med 1 sekund for hvert trin. Kald denne funktion `slowdown()`.

Til dette skal du bruge `time`-modulet.

Når du har fået `slowdown` til at virke på den rekursive funktion, så prøv at lave en mere (for dig) almindelig funktion, der laver nedtællingen med en løkke, og se hvad der sker hvis du dekorerer den med din `slowdown()`-funktion.

## Ex4: Decorating Game Characters

### Baggrund

I computerspil har hver karakter en unik evne eller færdighed, der gør dem specielle. For eksempel kan en karakter have evnen til at skyde præcist, bevæge sig lydløst eller hacke computere.

Vi skal bruge Python decorators til at tilføje unikke færdigheder eller evner til spilkarakterer.

### Opgave

Lav en Python-decorator, der tilføjer en unik færdighed eller evne til en spilkarakter. Decoratoren skal være genbrugelig, så vi kan tilføje flere færdigheder eller evner til en karakter.

### Eksempel

```python
@sharpshooter
@stealthy
def player():
    return "I'm the player character"

print(player())
```

**Output:**

```
I'm the player character, the sharpshooter and stealthy character.
```

### Trin

1. Lav en decorator-funktion, der tager en funktion som argument og returnerer en ny funktion, der tilføjer en unik færdighed eller evne til karakterens beskrivelse.
2. Tilføj decoratoren til funktionen `player()` for at tilføje "sharpshooter" og "stealthy" evner til spillerkarakteren.
3. Test din kode for at sikre, at den virker som forventet.

### Bonus

1. Lav flere decorators for andre færdigheder eller evner, som man kunne finde i et computerspil.
2. Tilføj flere færdigheder eller evner til en enkelt karakter ved at stable flere decorators ovenpå hinanden.
