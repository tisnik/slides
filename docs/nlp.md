# Zpracování přirozeného jazyka

Pavel Tišnovský
tisnik@centrum.cz

---

## Obsah kurzu (1/2)

* Úvod
    - Umělá inteligence
    - Vývoj umělé inteligence
    - Strojové učení
    - Vztah strojového učení a umělé inteligence
* Základní pojmy
* Techniky strojového učení

---

## Obsah kurzu (2/2)

* Používané nástroje a knihovny
    - scikit-learn
    - tiktoken
    - NLTK
* Pomocné nástroje a knihovny
    - NumPy
    - Pandas
    - Polars
    - Matplotlib

---

# Úvod

* Umělá inteligence
* Vývoj umělé inteligence
* Strojové učení
* Vztah strojového učení a umělé inteligence

---

### Umělá inteligence

* Definice
    - konstrukce strojů, které dokážou provádět činnosti vyžadující inteligenci, pokud by byly prováděny lidmi (Marvin Minsky, 1967)
    - existují i alternativní definice
* Modelování lidské mysli
    - shora dolů (psychologie)
    - zdola nahoru (neurověda)
    - zprostředka (informatika)
* Inteligentní chování může vzniknout ze spojení velkého množství jednoduchých systémů
    - koncept neuronových sítí

---

## Vývoj umělé inteligence

* 1943-1955
    - první myšlenky, že něco podobného může reálně vzniknout
    - booleovský model neuronu
    - A. Turing
        - Computing Machinery and Intelligence

---

## Vývoj umělé inteligence

* 1956
    - McCarthy (LISP)
    - (pravděpodobně) poprvé použil termín AI
    - Newel a Simon: Logic theorist
* velké očekávání pokroku v dalších letech
    - dařilo se částečné řešení různých problémů
    - prakticky každý měsíc nový objev

---

## Vývoj umělé inteligence

* cca 1965
    - vystřízlivění
    - existovala sice spousta vyřešených problémů, ale ty byly triviální
    - nalezeny limity, které se nedařilo překonat
    - první "AI zima"
* sedmdesátá léta
    - systémy založené na znalostech
    - vývoj v mnoha oblastech (hledání ropy atd.)

---

## Vývoj umělé inteligence

* začátek osmdesátých let
    - velké investice do AI
    - očekávání se nenaplnila
    - potom nastává druhá "AI zima"
* druhá polovina osmdesátých let
    - rozvoj neuronových sítí (což nebyla novinka)
* 1995
    - systémy SOAR (State, Operator and Result)

---

## Vývoj umělé inteligence

* 2000
    - big data (v tom pokračujeme i dnes)
    - ale prozatím žádné větší objemy
    - "wow" efekt na úrovni AI
* 2010
    - deep learning
* 2020
    - LLM (prompt engineering, ne fine tuning)
* současnost
    - LLM
    - generativní AI

---

## Strojové učení

* podoblast umělé inteligence
* změna interního stavu systému při tréninku
* několik způsobů realizace strojového učení
* "statistické učení"
* typicky se nejedná o plně automatizovanou činnost
    - vyžaduje chytrá (strategická) rozhodnutí
    - výběr modelu
    - výběr hyperparametrů modelu
    - rozdělení vstupních dat
    - filtrace dat
* nalézají se skryté vzorky a vazby v datech

---

## Vztah strojového učení a umělé inteligence

![vztah.png](https://tisnik.github.io/slides/images/ai_ml_dl.png)

---

## Vztah strojového učení a umělé inteligence

* Umělá inteligence (AI)
    - strojové učení (machine learning, ML)
    - hluboké učení (deep learning, DL)
    - robotika
    - neuronové sítě (NN)
    - zpracování přirozeného jazyka (NLP)
* AI > ML > NN > DL

---

## Vztah strojového učení a umělé inteligence

* Umělá inteligence
    - objevování
    - odvozování
    - odůvodnění
* Strojové učení
    - (sofistikovaná) analýza
    - predikce (!)
    - rozhodování (klasifikace, regrese)

---

### Proč strojové učení?

* Chceme, aby se stroj naučil řešit zadaný problém na základě vzorových řešení:
    - řešení je příliš komplikované
    - problém se často mění, vyvíjí
    - lidská práce je drahá (v porovnání se strojovou)
    - máme k dispozici tolik dat, že je není možné zpracovat "ručně"

---

### Typické aplikace strojového učení

* Rozpoznávání vzorů
    - věci/osoby/výrazy tváře na fotkách
    - mluvená slova
    - spam
    - medicínská diagnóza
* Rozpoznávání anomálií
    - netypické sekvence finančních transakcí
    - netypická data přicházející ze senzorů v atomové elektrárně

---

### Typické aplikace strojového učení

* Předpovídání
    - vývoj ceny akcií na burze / vývoj měnového kurzu
    - jaké filmy bude mít daný člověk rád
    - věk osoby na fotografii
* Shlukování
    - vyhledávání zpráv s podobným obsahem
    - vyhledání skupin zákazníků s podobnými vlastnostmi

---

## Základní pojmy

* Datová sada
    - trénovací data
    - testovací data

![dataset.png](https://tisnik.github.io/slides/images/dataset.png)

---

### Techniky strojového učení

* Supervised learning
    - také se nazývá "predictive modeling"
    - známe takzvané "kategorie" neboli odpovědi
* Unsupervised learning
    - neznáme odpovědi
    - model musí najít struktury/vzory v datech
    - typicky různé varianty clusteringu

---

### Techniky strojového učení

![ml.png](https://tisnik.github.io/slides/images/ml.png)

---

### Supervised learning

1. trénink na základě vstupních dat
    - model se naučí vztahy mezi daty a očekávanou odpovědí
2. predikce na základě jiných(!) dat
    - problematika rozdělení dat
3. výsledky
    - klasifikace: koupí si A, B nebo C?
    - regrese: vektor příznaků, numerická hodnota nebo hodnoty

---

### Unsupervised learning

1. trénink modelu na základě vstupních dat
    - ovšem bez znalosti správných odpovědí
2. shluková analýza
3. latentní a faktorová analýza

---

### Další možnosti

1. kombinace obou metod (bez/s učitelem)
2. učení se zpětnou vazbou
    - pasivní
    - aktivní

---

### ML modely

* ANN
* Desicion trees
* Support-vector machine
* Regresní analýza
* Bayesovské sítě
* Genetické algoritmy
* NN

---

### Redukce dat

![reduction.png](https://tisnik.github.io/slides/images/reduction.png)

---

### Redukce dat

![reduction_supervised.png](https://tisnik.github.io/slides/images/reduction_supervised.png)

---

### Nedoučení a přeučení

* Nedoučení
    - malá sada dat, na kterých je model trénován
    - příliš složitý model
    - data reprezentují pouze malý vzorek celého spektra hodnot
* Přeučení
    - velká vazba na trénovací data
    - menší flexibilita práce s daty, která model nezná
    - použití polynomu vyššího stupně, když by stačila lineární regrese

---

### Přeučení

![overtrain.png](https://tisnik.github.io/slides/images/overtraining.png)

---

### Úspěšnost modelu

* Pro zcela nová (neznámá) data!
    - ne pro trénovací množinu
    - častá chyba

---

### Křížová validace (cross validation)

* rozdělení dat do bloků
    - například na 1/10
    - 9/10 pro trénink
    - 1/10 pro otestování

---

## Zpracování přirozeného jazyka (NLP)

* na pomezí (počítačové) lingvistiky a umělé inteligence
    - strojový překlad
    - generování odpovědí na otázky
    - dolování informací z textu
    - automatické korektury
    - porovnání textů
    - klasifikace textů (odhady nálady, ...)
    - chatboti

---

## Vývoj NLP

* symbolické NLP (1950-1990)
* statistické NLP (1990-2000)
* neuronové NLP (počátky 2003)
    - český vědec Tomáš Mikolov!

---

## Získání vstupních dat, procesing, analýza

* Typicky se v ekosystému Pythonu používá
    - Pandas (Polars)
    - NumPy
    - Matplotlib

---

### Pandas

![pandas](https://tisnik.github.io/slides/images/pandas.png)

---

### Pandas

* Načtení dat z různých datových zdrojů do datových rámců
    - CSV
    - TSV
    - databáze
    - tabulkové procesory
* Programová konstrukce datových rámců
* Prohlížení obsahu datových rámců

---

### Pandas

* Iterace nad daty, řazení a další podobné operace
* Spojování, seskupování a změna tvaru dat
* Práce s takzvanými sériemi
    - většinou získanými z datových rámců
* Vykreslování grafů z údajů získaných z datových rámců

---

### Práce s datovými rámci

* Knihovna Pandas podporuje využití různých datových zdrojů, především pak:
  - Souborů CSV (Comma-Separated Values)
  - Souborů TSV (Tab-Separated Values)
  - Textových souborů s volitelným oddělovačem a formátem sloupců
  - Tabulek z tabulkových procesorů (xls, xlsx, xlsm, xlsb, odf, ods, odt)
  - Souborů JSON se strukturovanými daty
  - Načítání z relačních databází s využitím SQL
  - Načítání z Parquet souborů

---

### Polars

![polars](https://tisnik.github.io/slides/images/polars.png)

---

### Polars

* Alternativa ke knihovně Pandas
* Podporuje multithreading
* SIMD operace (ne vždy)
* Optimalizace dotazů
* Líné vyhodnocování

---

### Polars

* Datové rámce rozsáhlejší než dostupná RAM
* Naprogramováno v Rustu
* Vazby s dalšími knihovnami
    - pyarrow, NumPy, Pandas etc.
* Rozhraní pro Python a NodeJS

---

### Datové řady a datové rámce

* Podobné těm v Pandas
    - funkce a metody se stejnými jmény
    - ovšem ne zcela kompatibilní

---

## NumPy

![numpy_arrays.png](https://tisnik.github.io/slides/images/numpy_logo.png)

---

## NumPy

* n-rozměrná pole
    - (tenzor - v tomto kontextu ne zcela přesné)
* základ pro Matplotlib, scikit-learn atd.
* výpočty prováděné nativním kódem

---

## Matplotlib

![Matplotlib](https://tisnik.github.io/slides/images/matplotlib.png)

---

## Matplotlib

* Vizualizace dat
    - dovoluje nám zjistit základní vlastnosti
    - vizualizace kvality modelu atd.

---

## Praktická část

* tiktoken
* scikit-learn
    - stejné rozhraní pro různé ML modely
    - dobře zvolené výchozí parametry modelu
    - možnost doladění parametrů modelu
    - poměrně dobra dokumentace
        - (i když chybí různé howto...)
* další pomocné knihovny

---

## Scikit-learn

* Vstupem pro trénink modelů je:
    - matice vstupních hodnot
    - vektor očekávaných výsledků
* Ovšem text nemá tyto vlastnosti!
* Řešení:
    - vektorizace
    - tokenizace (pro LLM)

---

### Tokenizace

* knihovna `tiktoken`

```python
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

tokens = encoder.encode("Hello world")
print(tokens)
```

---

### Složená slova

```python
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

compound_words = (
        "bird",
        "black",
        "blue",
        "blackbird",
        "bluebird",
)

for word in compound_words:
    tokens = encoder.encode(word)
    print(f"{word:12}", tokens)
```

---

### Složená slova

```python
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

compound_words = (
        "unprofessionally",
        "internationalization",
        "counterrevolutionaries",
)

for word in compound_words:
    tokens = encoder.encode(word)
    print(f"{word:22}", tokens)
```

---

### Různé algoritmy tokenizace

```python
import tiktoken


def compare_encodings(example_string: str) -> None:
    print(f'\nExample string: "{example_string}"')

    for encoding_name in ["r50k_base", "p50k_base", "cl100k_base"]:
        encoding = tiktoken.get_encoding(encoding_name)
        tokens = encoding.encode(example_string)
        num_tokens = len(tokens)
        bytes = [encoding.decode_single_token_bytes(token) for token in tokens]

        print()
        print(f"{encoding_name}: {num_tokens} tokens")
        print(f"token integers: {tokens}")
        print(f"token bytes: {bytes}")

    print()


compare_encodings("The quick brown fox jumps over the lazy dog.")

compare_encodings("firefox")

```

---

### Zpětný převod tokenů na text

```python
import tiktoken

encoder = tiktoken.get_encoding("cl100k_base")

tokens = [9906, 1917]
text = encoder.decode(tokens)
print(text)

tokens = [9906, 11, 1917, 0]
text = encoder.decode(tokens)
print(text)

tokens = [9906, 11, 1917, 0, 0, 0, 0]
text = encoder.decode(tokens)
print(text)

tokens = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
text = encoder.decode(tokens)
print(text)

tokens = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010]
text = encoder.decode(tokens)
print(text)
```

---

### Vektorizace

```python
# Vektorizace sady textů (korpusu)

from sklearn.feature_extraction.text import CountVectorizer

# sada textů (korpus)
corpus = [
    "I'd like an apple",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(vectorized)
print()

# převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
print(as_array)
```

---

## Zpětný převod na slova (1)

```python
# Nalezení textu, který se nejvíce blíží hledanému vzorku

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

# sada textů (korpus)
corpus = [
    "I'd like an apple",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(vectorized)
print()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print()

# tabulka indexů slov a vlastních slov
print("Index Feature")
for i, feature_name in enumerate(feature_names):
    print(f"{i:2}    {feature_name}")

print()

# převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
print(as_array)
```

---

## Zpětný převod na slova (2)

```python
from sklearn.feature_extraction.text import CountVectorizer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1)
vectorized = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(vectorized)
print()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print()

# tabulka indexů slov a vlastních slov
print("Index Feature")
for i, feature_name in enumerate(feature_names):
    print(f"{i:2}    {feature_name}")

print()

# převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
print(as_array)
print()


def array_to_words(feature_names, as_array):
    """Převod matice s frekvencemi slov zpět na slova."""
    return list(
        feature_names[index]
        for index, included in enumerate(as_array[i])
        if included == 1
    )


# zpětný převod vět
for i in range(len(corpus)):
    print("Original: ", corpus[i])
    print("Vectors:  ", as_array[i])
    print("As words: ", array_to_words(feature_names, as_array))
    print()
```

---

## Stopslova

* V jazyce se často vyskytují
* Nenesou žádnou významovou informaci
    - spojky
    - předložky
    - členy
* Například
    - a, –dnes, cz, timto, budes, budem, byli
    - jses, muj, svym, ta, tomto, tohle, tuto
    - tyto, jej, zda, prave, ji, nad, nejsou
    - ci, pod, tema, mezi, jsem, tento

---

## Získání slovníku se stopslovy

```python
import nltk

# tento příkaz zajistí stažení příslušných datových souborů
nltk.download("stopwords")
```

---

## Odstranění stopslov

```python
from sklearn.feature_extraction.text import CountVectorizer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(vectorized)
print()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print()

# tabulka indexů slov a vlastních slov
print("Index Feature")
for i, feature_name in enumerate(feature_names):
    print(f"{i:2}    {feature_name}")

print()

# převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
print(as_array)
print()


def array_to_words(feature_names, as_array):
    """Převod matice s frekvencemi slov zpět na slova."""
    return list(
        feature_names[index]
        for index, included in enumerate(as_array[i])
        if included == 1
    )


# zpětný převod vět
for i in range(len(corpus)):
    print("Original: ", corpus[i])
    print("Vectors:  ", as_array[i])
    print("As words: ", array_to_words(feature_names, as_array))
    print()
```

---

## Opakující se slova

```python
from sklearn.feature_extraction.text import CountVectorizer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(vectorized)
print()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print()

# tabulka indexů slov a vlastních slov
print("Index Feature")
for i, feature_name in enumerate(feature_names):
    print(f"{i:2}    {feature_name}")

print()

# převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
print(as_array)
print()


def array_to_words(feature_names, as_array):
    """Převod matice s frekvencemi slov zpět na slova."""
    return list(
        feature_names[index]
        for index, included in enumerate(as_array[i])
        if included >= 1
    )


# zpětný převod vět
for i in range(len(corpus)):
    print("Original: ", corpus[i])
    print("Vectors:  ", as_array[i])
    print("As words: ", array_to_words(feature_names, as_array))
    print()
```


---

### Vyhledání textů podle podobnosti

* Opět se používá vektorizace
* Různé možnosti porovnání textů
    - cos
    - skalární součin
    - sofistikovanější metody

---

### Výpočet relevance jednotlivých slov

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()

# převod na běžnou matici
as_array = vectorized.toarray()

# výpočet IDF - převrácené četnosti slov
transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
transformer.fit(vectorized)

# zobrazení tabulky s převrácenými četnostmi jednotlivých slov
for feature_name, idf in zip(feature_names, transformer.idf_):
    print(f"{feature_name:9} {idf:5.2}")
```

---

## Přidání dalších vět do korpusu

```python
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# věty pro vyšší četnosti vybraných slov
for i in range(20):
    corpus.append("blue day")

# provedení vektorizace korpusu
vectorizer = CountVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()

# převod na běžnou matici
as_array = vectorized.toarray()

# výpočet IDF - převrácené četnosti slov
transformer = TfidfTransformer(smooth_idf=True, use_idf=True)
transformer.fit(vectorized)

# zobrazení tabulky s převrácenými četnostmi jednotlivých slov
for feature_name, idf in zip(feature_names, transformer.idf_):
    print(f"{feature_name:9} {idf:5.2}")
```

---

## Využití třídy `TfidVectorizer`

```python
# Přímý výpočet relevance jednotlivých slov

from sklearn.feature_extraction.text import TfidfVectorizer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = TfidfVectorizer(min_df=1, stop_words="english")
vectorized = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(vectorized)
print()

# převod na běžnou matici
as_array = vectorized.toarray()

# zobrazení výsledku v novém formátu
print(as_array)
```

---

## Nalezení nejbližšího textu podle vzorku

```python
# Nalezení textu, který se nejvíce blíží hledanému vzorku

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# sada textů (korpus)
corpus = [
    "I'd like an apple or an apple pie",
    "An apple a day keeps the doctor away",
    "Never compare an apple to an orange",
    "I prefer scikit-learn to orange",
    "The scikit-learn docs are orange and blue",
    "New apple logo will be orange and blue",
]

# provedení vektorizace korpusu
vectorizer = TfidfVectorizer(min_df=1, stop_words="english")
tfidf = vectorizer.fit_transform(corpus)

# výsledek vektorizace - řídká matice
print(tfidf)
print()

# matice s převrácenými četnostmi
pairwise_similarity = tfidf * tfidf.T

print(pairwise_similarity)
print()

print(pairwise_similarity.toarray())
print()

arr = pairwise_similarity.toarray()

# odstranění jedniček na hlavní diagonále
np.fill_diagonal(arr, np.nan)
print(arr)
print()

# hledaná věta
input_doc = "New apple logo will be orange and blue"
input_idx = corpus.index(input_doc)
print(input_idx, input_doc)

result_idx = np.nanargmax(arr[input_idx])
print(result_idx, corpus[result_idx])
```

---

### Vyhodnocení nálady u hodnotících textů

* Většinou musíme natrénovat model na základě znalostí (některých) hodnocení
    - klasický postup: trénink+test+vyhodnocení
* Lze ovšem použít i shlukovou analýzu
    - obecně méně přesná

---

### Vyhodnocení nálady u hodnotících textů

* Postup
    - vektorizace
    - natrénování modelu pro klasifikaci
    - ověření modelu
    - výpočet přesnosti odpovědí
    - výpočet a zobrazení matice záměn

---

## Praktický příklad

* Model rozpoznávající, zda je hodnocení dopravce
    - pozitivní
    - negativní
    - neutrální
* Model je zapotřebí natrénovat
    - s učitelem (supervised learning)

---

## Získání datové sady

```python
import requests

url = "https://raw.githubusercontent.com/satyajeetkrjha/kaggle-Twitter-US-Airline-Sentiment-/refs/heads/master/Tweets.csv"

response = requests.get(url)

with open("Tweets_airlines.csv", "wb") as fout:
    fout.write(response.content)
```

---

## Náhled na datovou sadu

```python
# Načtení datové sady a zjištění základních informací o v ní uložených datech.

import pandas as pd 

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# zobrazení základních informací o datovém rámci
print(airline_tweets.info())
```

---

## Informace o jednotlivých sloupcích

```python
# Načtení datové sady a zjištění základních informací o v ní uložených datech.

import pandas as pd 

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# zobrazení základních statistických informací o datovém rámci
print(airline_tweets.describe())
```

---

## Tweety o jednotlivých dopravcích (rozdělení do skupin)

```python
# Zjištění počtu tweetů o jednotlivých dopravcích

import pandas as pd

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# počet tweetů o jednotlivých dopravcích
print(airline_tweets.airline.value_counts())
```

---

## Vykreslení sloupcového diagramu s počty tweetů o jednotlivých dopravcích

```python
import pandas as pd
import matplotlib.pyplot as plt

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# specifikace plochy grafu
fig = plt.figure(1, figsize=(6, 6), dpi=150)

# vykreslení sloupcového diagramu s počty tweetů o jednotlivých dopravcích
airline_tweets.airline.value_counts().plot(
    kind="bar",
)

# zajištění místa pro popisky os
fig.tight_layout()

# uložení sloupcového diagramu do souboru
plt.savefig("178.png")

# zobrazení diagramu na obrazovce
plt.show()
```

---

## Vykreslení koláčového diagramu s počty tweetů o jednotlivých dopravcích

```python
import pandas as pd
import matplotlib.pyplot as plt

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# specifikace plochy grafu
fig = plt.figure(1, figsize=(6, 6), dpi=150)

# vykreslení koláčového diagramu s počty tweetů o jednotlivých dopravcích
airline_tweets.airline.value_counts().plot(
    kind="pie",
    autopct="%1.0f%%",
    startangle=90,
    wedgeprops={"edgecolor": "black", "linewidth": 2, "antialiased": True},
)

# uložení sloupcového diagramu do souboru
plt.savefig("179.png")

# zobrazení diagramu na obrazovce
plt.show()
```

---

### Načtení datové sady a zjištění celkové nálady.

```python
import pandas as pd 

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# celková nálada: počty pozitivních, negativních a neutrálních reakcí
print(airline_tweets.airline_sentiment.value_counts())
```

---

### Načtení datové sady a vizualizace celkové nálady

```python
import pandas as pd
import matplotlib.pyplot as plt

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# plocha grafu
fig = plt.figure(1, figsize=(6, 6), dpi=150)

# vykreslení koláčového diagramu s hodnoceními
airline_tweets.airline_sentiment.value_counts().plot(
    kind="pie",
    autopct="%1.0f%%",
    colors=["#ff8080", "yellow", "#80ff80"],
    wedgeprops={"edgecolor": "black", "linewidth": 2, "antialiased": True},
)

# uložení koláčového diagramu do souboru
plt.savefig("181.png")

# zobrazení koláčového diagramu na obrazovce
plt.show()
```

---

## Výpočet hodnocení podle dopravce

```python
import pandas as pd

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# rozdělení hodnocení podle dopravce
airline_sentiment = (
    airline_tweets
    .groupby(["airline", "airline_sentiment"])
    .airline_sentiment.count()
)

# výsledný datový rámec (hierarchický)
print(airline_sentiment)

print()

# pivot tabulka
airline_sentiment = airline_sentiment.unstack()

# výsledný datový rámec
print(airline_sentiment)
```

---

## Vizualizace hodnocení podle dopravce

```python
import pandas as pd
import matplotlib.pyplot as plt

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# rozdělení hodnocení podle dopravce
airline_sentiment = (
    airline_tweets
    .groupby(["airline", "airline_sentiment"])
    .airline_sentiment.count()
    .unstack()
)

# zobrazení hodnocení podle dopravce
airline_sentiment.plot(
    kind="bar",
    color=["#ff8080", "yellow", "#80ff80"],
    edgecolor="black",
    figsize=(6, 6),
).legend(loc='best')

plt.tight_layout()

# uložení koláčového diagramu do souboru
plt.savefig("183.png")

# zobrazení koláčového diagramu na obrazovce
plt.show()
```

---

## Získání vlastních tweetů a hodnocení

```python
import pandas as pd 

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# hodnocení (pozitivní, negativní, neutrální)
labels = airline_tweets["airline_sentiment"].values

# vlastní text hodnocení
features = airline_tweets["text"].values

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(features)
print("Number of features:", len(features))
```

---

## Preprocesing textových dat

```python
import numpy as np
import pandas as pd
import re

# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# hodnocení (pozitivní, negativní, neutrální)
labels = airline_tweets["airline_sentiment"].values

# vlastní text hodnocení
features = airline_tweets["text"].values


def process_feature(feature):
    """Preprocesing textových dat."""
    # odstranění speciálních znaků a dalšího smetí
    processed_feature = re.sub(r"\W", " ", feature)

    # odstranění samostatných znaků (oddělených bílými znaky)
    processed_feature = re.sub(r"\s+[a-zA-Z]\s+", " ", processed_feature)

    # odstranění samostatných znaků na začátku vět
    processed_feature = re.sub(r"\^[a-zA-Z]\s+", " ", processed_feature)

    # náhrada více mezer (nebo jiných bílých znaků) za jedinou mezeru
    processed_feature = re.sub(r"\s+", " ", processed_feature, flags=re.I)

    # odstranění prefixů ^b
    processed_feature = re.sub(r"^b\s+", "", processed_feature)

    # konverze výsledku na malá písmena
    return processed_feature.lower()


# preprocesing všech hodnocení
processed_features = [process_feature(feature) for feature in features]

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(processed_features)
print("Number of features:", len(processed_features))
print()

# porovnání výsledků preprocesingu
for i in range(10):
    print(features[i], " | ", processed_features[i])
```

---

## Vektorizace textových dat

```python
import numpy as np
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer



# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# hodnocení (pozitivní, negativní, neutrální)
labels = airline_tweets["airline_sentiment"].values

# vlastní text hodnocení
features = airline_tweets["text"].values


def process_feature(feature):
    """Preprocesing textových dat."""
    # odstranění speciálních znaků a dalšího smetí
    processed_feature = re.sub(r"\W", " ", feature)

    # odstranění samostatných znaků (oddělených bílými znaky)
    processed_feature = re.sub(r"\s+[a-zA-Z]\s+", " ", processed_feature)

    # odstranění samostatných znaků na začátku vět
    processed_feature = re.sub(r"\^[a-zA-Z]\s+", " ", processed_feature)

    # náhrada více mezer (nebo jiných bílých znaků) za jedinou mezeru
    processed_feature = re.sub(r"\s+", " ", processed_feature, flags=re.I)

    # odstranění prefixů ^b
    processed_feature = re.sub(r"^b\s+", "", processed_feature)

    # konverze výsledku na malá písmena
    return processed_feature.lower()


# preprocesing všech hodnocení
processed_features = [process_feature(feature) for feature in features]

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(processed_features)
print("Number of features:", len(processed_features))
print()

# vektorizace textu
vectorizer = CountVectorizer(
    max_features=2500,
    min_df=7, max_df=0.8, stop_words=stopwords.words("english")
)
vectorized_features = vectorizer.fit_transform(processed_features).toarray()

# slova pro dekódování vah
feature_names = vectorizer.get_feature_names_out()
print("Feature names count:", len(feature_names))
print("Feature names:")
for feature_name in feature_names:
    print(feature_name)

print()

# vlastní výsledek vektorizace
print("Sparse matrix of size", vectorized_features.shape, ":")
print(vectorized_features)
print()

# ukázka způsobu zakódování
print("Selected tweet:")
print("Original:     ", features[2])
print("Preprocessed: ", processed_features[2])
print("Vectorized:   ", vectorized_features[2])
print()

print("word# weight meaning")
for i, f in enumerate(vectorized_features[2]):
    if f > 0:
        print(f"{i:4}  {f:5}  {feature_names[i]}")
```

---

## Trénink a predikce modelu nad vektorizovanými daty

```python
import numpy as np
import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.neighbors import KNeighborsClassifier



# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# hodnocení (pozitivní, negativní, neutrální)
labels = airline_tweets["airline_sentiment"].values

# vlastní text hodnocení
features = airline_tweets["text"].values


def process_feature(feature):
    """Preprocesing textových dat."""
    # odstranění speciálních znaků a dalšího smetí
    processed_feature = re.sub(r"\W", " ", feature)

    # odstranění samostatných znaků (oddělených bílými znaky)
    processed_feature = re.sub(r"\s+[a-zA-Z]\s+", " ", processed_feature)

    # odstranění samostatných znaků na začátku vět
    processed_feature = re.sub(r"\^[a-zA-Z]\s+", " ", processed_feature)

    # náhrada více mezer (nebo jiných bílých znaků) za jedinou mezeru
    processed_feature = re.sub(r"\s+", " ", processed_feature, flags=re.I)

    # odstranění prefixů ^b
    processed_feature = re.sub(r"^b\s+", "", processed_feature)

    # konverze výsledku na malá písmena
    return processed_feature.lower()


# preprocesing všech hodnocení
processed_features = [process_feature(feature) for feature in features]

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(processed_features)
print("Number of features:", len(processed_features))
print()

# vektorizace textu
vectorizer = TfidfVectorizer(
    max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words("english")
)
vectorized_features = vectorizer.fit_transform(processed_features).toarray()

# klasické rozdělení datové sady na trénovací a testovací část
trainX, testX, trainY, testY = train_test_split(
    vectorized_features, labels, test_size=0.2, random_state=0
)

# konstrukce vybraného modelu s předáním hyperparametrů
classifier = KNeighborsClassifier(n_neighbors=1)

# trénink modelu
classifier.fit(trainX, trainY)

# predikce modelu pro testovací vstupy (ne pro trénovací data)
predictions = classifier.predict(testX)

# vyhodnocení kvality modelu
print(classification_report(testY, predictions))
print(accuracy_score(testY, predictions))

# matice záměn - absolutní hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    cmap=plt.cm.Blues,
    normalize=None,
)

# zobrazení matice v textové podobě
print(disp.confusion_matrix)

# uložení výsledků ve formě rastrového obrázku
plt.savefig("188_1.png")

# vizualizace matice
plt.show()

# matice záměn - relativní hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    cmap=plt.cm.Blues,
    normalize="true",
)

# zobrazení matice v textové podobě
print(disp.confusion_matrix)

# uložení výsledků ve formě rastrového obrázku
plt.savefig("188_2.png")

# vizualizace matice
plt.show()
```
---

## NLP a deep learning

* Neuronové sítě
* Propojení takzvaných neuronů
    - Model neuronu
    - Způsob propojení neuronů
    - Vstupy a výstupy

---

### Model neuronu

![neuron.png](https://tisnik.github.io/slides/images/neuron.png)

* libovolný počet vstupů
* typicky jeden výstup
* váhy vstupů
* aktivační funkce

y = f(w_1x_1 + w_2x_2 + … + w_nx_n)

---

### Bias

![bias.png](https://tisnik.github.io/slides/images/bias.png)

y = f(w_0 + w_1x_1 + w_2x_2 + … + w_nx_n)

---

### Aktivační funkce

* Jediná nelinearita v modelu
* Mnoho typů aktivačních funkcí

---

### Aktivační funkce

![akt1.png](https://tisnik.github.io/slides/images/akt_1.png)

---

### Aktivační funkce

![akt2.png](https://tisnik.github.io/slides/images/akt_2.png)

---

### Feed-forward síť

* Vstupní vrstva
* Skryté vrstvy
* Výstupní vrstva

---

### Feed-forward síť

![ff.png](https://tisnik.github.io/slides/images/ff.png)

---

### Příliš mnoho vrstev

* Model se přestane učit nebo se učí velmi pomalu
    - vanishing gradient problem
    - "méně je někdy více"

---

### Použití NN ve formě modelu

```python
# Trénink a predikce modelu nad vektorizovanými daty

import numpy as np
import pandas as pd
import re
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# model zalozeny na neuronove siti
from sklearn.neural_network import MLPClassifier



# načtení tabulky do datového rámce s předzpracováním numerických dat
airline_tweets = pd.read_csv("Tweets_airlines.csv")

# hodnocení (pozitivní, negativní, neutrální)
labels = airline_tweets["airline_sentiment"].values

# vlastní text hodnocení
features = airline_tweets["text"].values


def process_feature(feature):
    """Preprocesing textových dat."""
    # odstranění speciálních znaků a dalšího smetí
    processed_feature = re.sub(r"\W", " ", feature)

    # odstranění samostatných znaků (oddělených bílými znaky)
    processed_feature = re.sub(r"\s+[a-zA-Z]\s+", " ", processed_feature)

    # odstranění samostatných znaků na začátku vět
    processed_feature = re.sub(r"\^[a-zA-Z]\s+", " ", processed_feature)

    # náhrada více mezer (nebo jiných bílých znaků) za jedinou mezeru
    processed_feature = re.sub(r"\s+", " ", processed_feature, flags=re.I)

    # odstranění prefixů ^b
    processed_feature = re.sub(r"^b\s+", "", processed_feature)

    # konverze výsledku na malá písmena
    return processed_feature.lower()


# preprocesing všech hodnocení
processed_features = [process_feature(feature) for feature in features]

# hodnoty použité později pro trénink modelu
print("Labels:")
print(labels)
print("Number of labels:", len(labels))
print()

print("Features:")
print(processed_features)
print("Number of features:", len(processed_features))
print()

# vektorizace textu
vectorizer = TfidfVectorizer(
    max_features=2500, min_df=7, max_df=0.8, stop_words=stopwords.words("english")
)
vectorized_features = vectorizer.fit_transform(processed_features).toarray()

# klasické rozdělení datové sady na trénovací a testovací část
trainX, testX, trainY, testY = train_test_split(
    vectorized_features, labels, test_size=0.2, random_state=0
)

# konstrukce vybraného modelu s předáním hyperparametrů
classifier =  MLPClassifier(max_iter=5000)

# trénink modelu
classifier.fit(trainX, trainY)

# predikce modelu pro testovací vstupy (ne pro trénovací data)
predictions = classifier.predict(testX)

# vyhodnocení kvality modelu
print(classification_report(testY, predictions))
print(accuracy_score(testY, predictions))

# matice záměn - absolutní hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    cmap=plt.cm.Blues,
    normalize=None,
)

# zobrazení matice v textové podobě
print(disp.confusion_matrix)

# uložení výsledků ve formě rastrového obrázku
plt.savefig("189_1.png")

# vizualizace matice
plt.show()

# matice záměn - relativní hodnoty
disp = ConfusionMatrixDisplay.from_estimator(
    classifier,
    testX,
    testY,
    cmap=plt.cm.Blues,
    normalize="true",
)

# zobrazení matice v textové podobě
print(disp.confusion_matrix)

# uložení výsledků ve formě rastrového obrázku
plt.savefig("189_2.png")

# vizualizace matice
plt.show()
```
