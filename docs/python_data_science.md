# Data science s využitím Pythonu

---

* Pavel Tišnovský
* kurzy.python@centrum.cz

![Python](images/python.png)

---

## Obsah

* Nástroje pro datovou analýzu
* Transformace dat na informace
* Jupyter Notebook
* Knihovny používané v této oblasti: NumPy, Pandas, Polars, Seaborn, scikit-learn, Dask
* Vizualizace dat: Matplotlib
* Zpracování obrazů a přirozeného jazyka v Pythonu
* Strojové učení

---

## Python

* Dnes jeden z nejpopulárnějších programovacích jazyků
    - viz například TIOBE programming community index
    - <https://www.tiobe.com/tiobe-index/>
    - popř. statistika dostupná na OpenHubu
    - <https://www.openhub.net/languages/compare>
* Dostupnost na většině platforem
    - na některých MCU jako MicroPython

---

## Typické použití Pythonu

* Nástroje a utility ovládané z příkazového řádku
* Aplikace s grafickým uživatelským rozhraním
* Client-server
    - serverová část (Flask, Django, CherryPy, ...)
    - klient (Brython, spíše technologické demo)
* Numerické výpočty, symbolické výpočty
    - NumPy
    - SciPy
    - Matplotlib

---

## Typické použití Pythonu

* Moderní způsoby využití Pythonu
    - AI
    - Machine Learning (Deep Learning)
    - PyTorch
    - Big data
    - aplikace v prohlížeči
* Tzv. „glue“ jazyk
* Vestavitelný interpret Pythonu

---

## Nástroje pro datovou analýzu

* Data mining
* Data procesing a modelování
    - klasifikace
    - predikce
    - výběr modelu
    - redukce počtu dimenzí
    - pre-processing
    - modelování
* Vizualizace

---

## Jupyter Notebook

* Typický centrální prvek, v němž se odehrává vývoj
* Lze sdílet
* Podporuje různá jádra (kernels)
* Podpora vizualizace přímo na ploše notebooku

---

## Data mining

* Scrapy
* BeautifulSoup

---

## Data processing a modelování

* NumPy
* SciPy
* Xarray
* Pandas
* Polars
* SciKit-learn

---

## Vizualizace dat

* Matplotlib
* Seaborn
* Bokeh
* Plotly
* pydot
* plotnine

---

## Strojové učení

* PyCaret
* H2O
* TPOT
* Auto-sklearn
* Keras
* SciKit-Learn
* PyTorch
* TensorFlow

---

## Zpracování přirozeného jazyka

* NLTK
* spaCy

---

## HPC

* Dask

---

## NumPy

![numpy_arrays.png](images/numpy_logo.png)

---

## NumPy

* výslovnosti
    - [nəmpᴧɪ]
    - [nəmpi]
* historie
    - matrix package
    - Numeric
    - NumPy
* Kooperace s dalšími knihovnami a frameworky
    - SciPy
    - Matplotlib
    - OpenCV

---

### NumPy

* n-dimenzionální pole jako základní datový typ
    - ideově vychází z APL
    - nové funkce
    - nové (přetížené) operátory
* mnoho typů konstruktorů
* broadcsting
* (re)shaping
    - změna tvaru pole (počet dimenzí, tvar)

---

### Nativní (skalární) datové typy

```
╔════════════╤═══════════════════════════╤═══════════════════════════════╗
║ Formát     │ Popis                     │ Rozsah                        ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ bool       │ uloženo po bajtech        │  True/False                   ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ int8       │ celočíselný se znaménkem  │ -128..127                     ║
║ int16      │ celočíselný se znaménkem  │ -32768..32767                 ║
║ int32      │ celočíselný se znaménkem  │ -2147483648..2147483647       ║
║ int64      │ celočíselný se znaménkem  │ -9223372036854775808..        ║
║            │                           │  9223372036854775807          ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ uint8      │ celočíselný bez znaménka  │  0..255                       ║
║ uint16     │ celočíselný bez znaménka  │  0..65535                     ║
║ uint32     │ celočíselný bez znaménka  │  0..4294967295                ║
║ uint64     │ celočíselný bez znaménka  │  0..18446744073709551615      ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ float16    │ plovoucí řádová čárka     │  poloviční přesnost (half)    ║
║ float32    │ plovoucí řádová čárka     │  jednoduchá přesnost (single) ║
║ float64    │ plovoucí řádová čárka     │  dvojitá přesnost (double)    ║
╟────────────┼───────────────────────────┼───────────────────────────────╢
║ complex64  │ komplexní číslo (dvojice) │  2×float32                    ║
║ complex128 │ komplexní číslo (dvojice) │  2×float64                    ║
╚════════════╧═══════════════════════════╧═══════════════════════════════╝
```

---

### N-dimenzionální pole

![numpy_arrays.png](images/numpy_arrays.png)

---

### N-dimenzionální pole

* Představuje obecné n-dimenzionální pole
* Interní způsob uložení dat zcela odlišný od Pythonovských seznamů či n-tic
    - „pohled“ na kontinuální blok hodnot
* Homogenní datová struktura
    - menší flexibilita
    - menší paměťové nároky
    - vyšší výpočetní rychlost díky použití nativního kódu
    - obecně lepší využití cache a rychlejší přístup k prvkům
* Základní strukturovaný datový typ knihovny NumPy

---

### N-dimenzionální pole

* Volitelný typ prvků
* Volitelný počet dimenzí
    - vektory
    - matice
    - pole s větším počtem dimenzí
* Volitelné uspořádání prvků
    - podle zvyklostí jazyka Fortran
    - podle zvyklostí jazyka C

---

## Xarray

![xarray](images/xarray1.png)

---

### Xarray

* n-dimensionální pole s metadaty
    - jméno
    - dimenze (osy)
    - koordináty na osách
    - uživatelské atributy

---

### Přednosti použití Xarray

* intuitivní práce s poli
* založeno na metadatech, ne na kódu
* stručnost
* dnes de facto standardní řešení
* méně chyb při zpracování dat
    - operace nad nekorektními osami
* broadcasting založený na jménu osy
* velmi jednoduchá operace typu `groupby`

---

### Množina polí

![xarray](images/xarray2.png)

---

## Pandas

![pandas](images/pandas.png)

---

## Pandas

* Načtení dat z různých datových zdrojů do datových rámců
    - CSV
    - TSV
    - databáze
    - tabulkové procesory
* Programová konstrukce datových rámců
* Prohlížení obsahu datových rámců

---

## Pandas

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

### Zpracování souborů s nestandardním formátem

* https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
* Evidentně se jedná o tabulková a velmi dobře strukturovaná data, která by bylo vhodné umět automaticky zpracovat

---

### Zpracování souborů s nestandardním formátem

```
13.11.2023 #219
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,683
Brazílie|real|1|BRL|4,672
Bulharsko|lev|1|BGN|12,573
Čína|žen-min-pi|1|CNY|3,162
Dánsko|koruna|1|DKK|3,296
EMU|euro|1|EUR|24,590
Filipíny|peso|100|PHP|41,117
Hongkong|dolar|1|HKD|2,952
Indie|rupie|100|INR|27,682
Indonesie|rupie|1000|IDR|1,468
Island|koruna|100|ISK|16,040
Izrael|nový šekel|1|ILS|5,964
Japonsko|jen|100|JPY|15,186
Jižní Afrika|rand|1|ZAR|1,228
Kanada|dolar|1|CAD|16,664
Korejská republika|won|100|KRW|1,740
Maďarsko|forint|100|HUF|6,514
Malajsie|ringgit|1|MYR|4,896
Mexiko|peso|1|MXN|1,303
MMF|ZPČ|1|XDR|30,319
Norsko|koruna|1|NOK|2,069
Nový Zéland|dolar|1|NZD|13,550
Polsko|zlotý|1|PLN|5,552
Rumunsko|leu|1|RON|4,947
Singapur|dolar|1|SGD|16,936
Švédsko|koruna|1|SEK|2,118
Švýcarsko|frank|1|CHF|25,471
Thajsko|baht|100|THB|64,040
Turecko|lira|1|TRY|0,806
USA|dolar|1|USD|23,050
Velká Británie|libra|1|GBP|28,230
```

---

## Polars

![polars](images/polars.png)

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

### Načtení z SQL

```python
import polars

connection_string = "postgresql://postgres:postgres@localhost:5432/testdb"

query = """
    SELECT org_id, cluster_id, rule_fqdn
      FROM rule_hit
     ORDER by org_id, cluster_id
"""

df = polars.read_sql(query, connection_string)

print(df)
print()
```

---

### Klíč k úspěchu: být líný!

* FP programování
* Architektura založená na Kafce atd.
* Dask atd.
* Líné datové rámce v Polars

---

### Líné datové rámce

```python
import polars

df = polars.read_csv("hall_of_fame.csv").lazy()

df2 = df.groupby("Winner", maintain_order=True).agg([polars.col("Year").len()]). \
      sort("Year"). \
      reverse(). \
      head(5)

print(df2.describe_plan())
print(df2.describe_optimized_plan())
```

---

## Matplotlib

![Matplotlib](images/matplotlib.png)

---

## Matplotlib

* zaměřena explicitně na tvorbu grafů
* právě vzájemnou kombinací obou knihoven NumPy+matplotlib lze relativně
* snadno dosáhnout velmi pěkných výsledků plně porovnatelných s výsledky
  vytvořenými komerčními balíky.

---

### Možnosti knihovny Matplotlib

* grafy funkcí typu y = f(x)
* parametrické zadání 2D průběhu x, y = f(t)
* grafy funkcí typu z = f(x,y)
* parametrické zadání 3D průběhu x, y, z = f(t)

---

### Zobrazení grafů

* na obrazovce
* do plochy Jupyter Notebooku
* do rastrových obrázků
* do vektorových kreseb
* do PDF

---

## Plotnine

* Kombinace možností ggplot2 a Pythonu
* ggplot2 - populární balíček z ekosystému jazyka R
* Vyšší úroveň abstrakce v porovnání s Matplotlibem

---

### Konstrukce grafů s využitím grammar of graphics

![grammar of graphics](images/gog.png)

---

### Korelační diagram

![plotnine1](images/plotnine1.png)

---

### Rozdělení grafu

![plotnine2](images/plotnine2.png)

---

### Aproximace

![plotnine3](images/plotnine3.png)

---

### Regresní přímka

![plotnine4](images/plotnine4.png)

---

## Scikit-learn

![scikit-learn](images/scikit-learn.png)

---

## Scikit-learn

* Součást konceptu data procesingu a modelování
    - klasifikace
    - predikce
    - výběr modelu
    - redukce počtu dimenzí
    - pre-processing
    - modelování

---

### Fáze data procesingu a modelování

* Klasifikace
    - "rozpoznani" objektu
* Prefikce (regrese)
* Clustering
    - objekty seskupené do množin
    - (různý typ zákazníků atd.)
* Model selection
    - porovnání a validace parametrů modelu
    - vylepšení modelu (parameter tuning)
* Redukce počtu dimenzí
    - méně "náhodných" proměnných
* Pre-processing
    - extrakce
    - normalizace (!!!)

---

## Zpracování obrazů a přirozeného jazyka v Pythonu

* TensorFlow 
* Keras

---

## Strojové učení

* TensorFlow
* Keras

---

## Užitečné odkazy

* 15 Python Libraries for Data Science You Should Know
    - https://www.dataquest.io/blog/15-python-libraries-for-data-science/
* Top Python Libraries for Data Science in 2022
    - https://www.datacamp.com/blog/top-python-libraries-for-data-science
* Image Recognition Tutorial in Python for Beginners
    - https://howtocreateapps.com/image-recognition-python/
* Image Recognition and Classification in Python with TensorFlow and Keras
    - https://stackabuse.com/image-recognition-in-python-with-tensorflow-and-keras/
* The CIFAR-10 dataset
    - https://www.cs.toronto.edu/~kriz/cifar.html

---

