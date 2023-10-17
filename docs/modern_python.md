# Evoluce Pythonu

---

![Python](images/python.png)

---

## Obsah kurzu

* Nové vlastnosti jazyka
* Novinky v ekosystému Pythonu
* Vylepšení výkonnosti Pythonu
* Python a vývoj webových aplikací
* Alternativní projekty a jazyky
* Testování aplikací v Pythonu

---

## Obsah kurzu
### Nové vlastnosti jazyka

* Formátovací řetězce
* Pouze poziční parametry funkcí
* Pattern matching
* "Mroží" operátor
* Podpora pro asynchronní programování
* Skupiny výjimek
* Deklarace datových typů
* Statická typová kontrola

---

## Obsah kurzu
### Novinky v ekosystému Pythonu

* Správa projektů
* Lintery

---

## Obsah kurzu
### Vylepšení výkonnosti Pythonu

* Výkonnější CPython
* Problém související s GILem
* JIT překlad

---

## Obsah kurzu
### Python a vývoj webových aplikací

* Brython
* Bokeh

---

## Obsah kurzu
### Alternativní projekty a jazyky

* Coconut
* Mojo

---

## Obsah kurzu
### Testování aplikací v Pythonu

* Jednotkové testy
* Zjištění pokrytí kódu testy
* Testy chování (BDD)
* Nástroj Hypothesis
* Fuzzy testy

---

# Nové vlastnosti jazyka

![Python](images/python.png)

---

## Nové vlastnosti jazyka

* Formátovací řetězce
* Pouze poziční parametry funkcí
* Pattern matching
* "Mroží" operátor
* Podpora pro asynchronní programování
* Skupiny výjimek
* Deklarace datových typů
* Statická typová kontrola

---

## Postupné rozšiřování možností Pythonu

```
Python 3.6    f-řetězce, async-IO
Python 3.7    klíčová slova async a await
Python 3.8    mroží operátor, poziční parametry
Python 3.9    generické typy
Python 3.10   pattern matching
Python 3.11   skupiny výjimek
Python 3.12   klíčové slovo type + sémantika
```

---

## Formátovací řetězce

* Přidáno do Pythonu 3.6
* Lze využít společně s původním formátováním
* Prefix `f""`
    - proto se nazývají f-strings

---

### Ukázka použití f-řetězců

* "Interpolace" proměnných

```python
a=1
b=2
c=a+b

print(f"{a}+{b}={c}")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-1.py)

---

### Výrazy v f-řetězci

* V řetězci lze použít i výrazy

```python
a=1
b=2

print(f"{a}+{b}={a+b}")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-2.py)

---

### Podmínka ve výrazu

* Ne vždy plně čitelné, ale pro jednoduché šablony ano

```python
a=1
b=-1

print(f"Kladné: {'ano' if a>0 else 'ne'}")
print(f"Kladné: {'ano' if b>0 else 'ne'}")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-3.py)

---

### Volání funkce v f-řetězci

```python
x = "Hello world!"

print(f"Délka '{x}' je {len(x)} znaků")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-4.py)

---

### Volání metody v f-řetězci

```python
x = "hello world!"

print(f"Zpráva pro vás: '{x.capitalize()}'")
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//f-string-5.py)

---

## Poziční parametry funkcí

* Přidáno do Pythonu 3.8
* Umožňují rozlišit funkce s parametry zapisovanými jen pozičně
* Ostatní parametry buď pozičně nebo je lze pojmenovat

---

### Poziční parametry funkcí

* Běžně deklarovaná funkce

```python
def foo(x, y, z):
    return x+y-z


print(foo(1, 2, 10))
print(foo(x=1, y=2, z=10))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-1.py)

---

### Poziční parametry funkcí

* Parametry lze pojmenovat a předat v jiném pořadí

```python
def foo(x, y, z):
    return x+y-z


print(foo(1, 2, 10))
print(foo(z=1, y=2, x=10))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-2.py)

---

### Poziční parametry funkcí

* Všechny parametry jsou čistě poziční

```python
def foo(x, y, z, /):
    return x+y-z


print(foo(1, 2, 10))
print(foo(z=1, y=2, x=10))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-3.py)

---

### Poziční parametry funkcí

* První parametr je čistě poziční

```python
def foo(x, /, y, z):
    return x+y-z


print(foo(1, 2, 10))
print(foo(1, z=1, y=2))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-4.py)

---

### Poziční parametry funkcí

* Kombinace s pojmenovanými parametry

```python
def foo(x=0, /, y=0, z=0):
    return x+y-z


print(foo())
print(foo(10))
print(foo(1, 2, 10))
print(foo(1, z=1, y=2))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//positional-params-5.py)

---

## Pattern matching

* Přidáno do Pythonu 3.10

---

## Mroží operátor

* Přidáno do Pythonu 3.8

---

## Podpora pro asynchronní programování

* Postupně přidáno v Pythonu 3.6 a 3.7
* Nová klíčová slova `async` a `await`

---

## Skupiny výjimek

---

## Deklarace datových typů

* Přidáváno postupně

---

### Nejpopulárnější jazyky

```
Dynamicky typované   Staticky typované
--------------------------------------
Python               C
JavaScript           C++
Ruby                 Go
Perl                 Rust
Matlab               Java
PHP                  Scala
```

---

### Přednosti dynamicky typovaných jazyků

* Rychlý cyklus vývoje
    - edit-(compile)-run
* Velmi snadné pro začátečníky
* Ideální pro skriptování
    - CLI
    - skripty na webových stránkách

---

### Zápory dynamicky typovaných jazyků

* Zaručení korektnosti rozsáhlých projektů
* Většinou se vyžaduje větší množství jednotkových testů
    - code coverage není dobrou metrikou!
* Informace o typech se někdy zapisují do komentářů
* IDE nemusí vždy nabízet správné funkce/metody/opravy

---

## To nejlepší z obou světů?

* Volitelné typy

```
Jazyk          Technologie pro statické typy
--------------------------------------------
JavaScript     TypeScript, Flow
Python         Mypy, Pyright, Pyre
Ruby           Sorbet
```

---

### Volitelné typy a Python

* Python je dynamicky typovaný
    - a nejsou plány to změnit!
* Typy jsou čistě volitelné
    - přidáno do Pythonu 3.5
    - nazvané "type hints"
    - (aby to vývojáře nestrašilo)
* Statické typové kontroly
    - mypy, pyright, pyre

---

### Statická typová kontrola a Mypy

---

![Mypy logo](images/mypy.png)

---

```python
def add(a, b):
    return a+b
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-1.py)

* Typ `Any` je přidán automaticky

---

### Typové anotace

* specifikují se za dvojtečkou

```python
def add(a:int, b:int) -> int:
    return a+b
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-2.py)

### `bool` nebo `int`?

* Viz specifikace Pythonu!

```python
def add(a:int, b:int) -> int:
    return a+b

print(add(1, 2))
print(add(1, True))
print(add(1, False))
```

[Zdrojový kód příkladu](https://github.com/tisnik/most-popular-python-libs/blob/master/modern_python/sources//mypy-add-3.py)

---

# Novinky v ekosystému Pythonu

![Python](images/python.png)

---

# Vylepšení výkonnosti Pythonu

![Python](images/python.png)

---

## Vylepšení výkonnosti Pythonu

* Výkonnější CPython
* Problém související s GILem
* JIT překlad

---

## Výkonnější CPython

---

## Problém související s GILem

---

## JIT překlad

---

# Python a vývoj webových aplikací

![Python](images/python.png)

---

##

---

##

---

# Testování

![Python](images/python.png)

* Základní technologie testování
* Pyramida testů
* Zmrzlinový kornout jako antipattern
* Jednotkové testy
* Modul `pytest`
* Nástroj Hypothesis
* Fuzzy testy

---

### Testovací frameworky v Pythonu

```
1                   unittest
2                   doctest
3                   pytest
4                   nose
5                   testify
6                   Trial
7                   Twisted
8                   subunit
9                   testresources
10                  reahl.tofu
11                  unit testing
12                  testtools
13                  Sancho
14                  zope.testing
15                  pry
16                  pythoscope
17                  testlib
18                  pytest
19                  dutest
```

---

### Pyramida typů testů

* Business část
    - Beta testy
    - Alfa testy
    - Akceptační testy
* Technologická část
    - UI testy
    - API testy
    - Integrační testy
    - Testy komponent
    - Unit testy
* Další typy testů
    - Benchmarky

---

