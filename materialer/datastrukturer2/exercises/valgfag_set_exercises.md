# Valgfag Set Øvelser
## Analyse af studerende tilmeldinger

I denne øvelse skal I arbejde med rigtige data om studerende tilmeldinger til KEA's valgfag. Vi har 7 forskellige valgfag med forskellige antal studerende.

**Målet**: Bruge Python sets til at besvare praktiske spørgsmål om studerende tilmeldinger.

**Vigtige pointer**:
- Fokuser på **set operationer**, ikke på input/output
- Tænk i **Venn diagrammer** når I løser opgaverne
- Brug Python's set operatorer: `|` `&` `-` `^` `<=` `<`

## Forberedelse - Indlæs data

Først skal vi indlæse alle valgfag-tilmeldingerne. Koden herunder opretter sets med fulde navne for hver valgfag.


```python
import csv      # csv modulet bruges til at arbejde med csv filer og data

def indlaes_valgfag(filnavn):
    """Indlæser studerende navne fra CSV fil og returnerer et set med fulde navne"""
    f = open(filnavn, 'r', encoding='utf-8')
    navne = csv.reader(f)
    next(navne)  # Spring header over
    return {f"{fornavn} {efternavn}" for fornavn, efternavn in navne}
            # {'Laura,Christensen', 'Helle,Christensen'} -> SET COMPREHENSION
# Indlæs alle valgfag
python_studerende = indlaes_valgfag('introduction_to_python.csv')
ai_studerende = indlaes_valgfag('ai_agenter.csv')
sikkerhed_studerende = indlaes_valgfag('it_sikkerhed.csv')
c_studerende = indlaes_valgfag('low_level_c.csv')
datastruktur_studerende = indlaes_valgfag('datastrukturer_algoritmer.csv')
devops_studerende = indlaes_valgfag('devops.csv')
nodejs_studerende = indlaes_valgfag('nodejs.csv')

print(f"Python: {len(python_studerende)} studerende")
print(f"AI-agenter: {len(ai_studerende)} studerende")
print(f"IT-sikkerhed: {len(sikkerhed_studerende)} studerende")
print(f"Low level C: {len(c_studerende)} studerende")
print(f"Datastrukturer: {len(datastruktur_studerende)} studerende")
print(f"DevOps: {len(devops_studerende)} studerende")
print(f"NodeJs: {len(nodejs_studerende)} studerende")
```

    Python: 31 studerende
    AI-agenter: 35 studerende
    IT-sikkerhed: 41 studerende
    Low level C: 16 studerende
    Datastrukturer: 18 studerende
    DevOps: 38 studerende
    NodeJs: 34 studerende


---

## Opgave 1: Fælles interesser

Vi skal holde et fælles study group event og vil gerne finde ud af, hvilke to valgfag der har flest studerende til fælles.

**Spørgsmål**: Sammenlign Python og AI-agenter - hvor mange studerende tager begge fag?


```python
# Din kode her - find studerende der tager både Python OG AI-agenter

```

---

## Opgave 2: Dedikerede studerende

Vi vil gerne finde de studerende, der har valgt Python, men som IKKE også har valgt IT-sikkerhed (måske fordi de vil fokusere 100% på programmering).

**Spørgsmål**: Hvor mange studerende tager kun Python og ikke IT-sikkerhed?


```python
# Din kode her - find studerende der tager Python men IKKE IT-sikkerhed


```

---

## Opgave 3: Alle studerende fra ...

Skolen overvejer at lave en fælles workshop om "Moderne teknologi". Vi vil invitere alle studerende fra enten Python eller NodeJs fagene (eller begge).

**Spørgsmål**: Hvor mange forskellige studerende ville blive inviteret hvis vi inviterer alle fra Python ELLER NodeJs?


```python
# Din kode her - find alle studerende der tager Python ELLER NodeJs (eller begge) 


```

---

## Opgave 4: Eksklusive valg

Vi vil gerne forstå studerende, der har valgt enten Python eller IT-sikkerhed, men ikke begge. Dette kan hjælpe os med at forstå, om fagene tiltrækker forskellige typer studerende.

**Spørgsmål**: Hvilke studerende tager enten Python eller IT-sikkerhed, men ikke begge fag?


```python
# Din kode her - find studerende der tager ENTEN Python ELLER IT-sikkerhed (men ikke begge)


```

---

## Opgave 5: Subset analyse

Low level C er et meget specialiseret fag. Vi vil gerne finde ud af, om alle C-studerende også tager et mere praktisk fag som DevOps.

**Spørgsmål**: Er alle Low level C studerende også tilmeldt DevOps? (Med andre ord: er C-studerende et subset af DevOps-studerende?)


```python
# Din kode her - tjek om alle C-studerende også tager DevOps


```

---

## Opgave 6: Kompleks analyse

Vi vil gerne finde studerende med en specifik profil: De skal være interesserede i både Python og AI (fremtidsorienterede), men ikke i IT-sikkerhed (måske fordi de fokuserer på udvikling frem for sikkerhed).

**Spørgsmål**: Hvilke studerende tager både Python OG AI-agenter, men IKKE IT-sikkerhed?


```python
# Din kode her - find studerende der opfylder alle tre kriterier


```

---

## Opgave 7: Multi-kurs analyse (Avanceret)

Vi vil gerne identificere de mest engagerede studerende inden for "praktisk programmering". Disse studerende skulle tage mindst 3 af følgende 4 fag: Python, IT-sikkerhed, DevOps, NodeJs.

**Spørgsmål**: Hvor mange studerende tager mindst 3 af disse 4 fag?


```python
# Din kode her - find studerende der tager mindst 3 af de 4 "praktiske" fag
# Tip: Du skal muligvis bruge flere set operationer og måske en løkke


```

---

## Opgave 8: Strategisk planlægning (Meget avanceret)

Skolen vil holde et stort netværksarrangement og har plads til maksimalt 100 studerende. Vi vil vælge 3 valgfag, hvor kombinationen giver os flest mulige unikke deltagere.

**Spørgsmål**: 
1. Prøv kombinationen Python + IT-sikkerhed + DevOps - hvor mange unikke studerende?
2. Prøv kombinationen AI-agenter + NodeJs + IT-sikkerhed - hvor mange unikke studerende?
3. Hvilken kombination er bedst?


```python
# Din kode her - sammenlign forskellige 3-fags kombinationer
# Kombination 1: Python + IT-sikkerhed + DevOps

# Kombination 2: AI-agenter + NodeJs + IT-sikkerhed

# Sammenligning

```

---

## Bonus opgave: Komplet oversigt

Lav en komplet analyse af alle studerende:

1. Hvor mange unikke studerende er der i alt på tværs af alle valgfag?
2. Hvor mange studerende tager kun ét valgfag?
3. Hvilke studerende tager flest valgfag?


```python
# Din kode her - komplet analyse


```
