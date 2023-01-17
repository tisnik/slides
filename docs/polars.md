# Polars: Blazingly fast DataFrames in Rust, Python & Node.js

--

![Polars](images/polars.png)

--

## Polars

* Alternative to Pandas
* Multi threaded (concurrent)
* SIMD
* Query optimization
* Lazy execution

--

## Polars

* Datasents larger than RAM
* Written in Rust
* Cooperate with other libraries
    - pyarrow, NumPy, Pandas etc.
* Interface to Python and NodeJS
    - we'll ignore NodeJS, of course :)

--

## Data series and data frames

* Similar to Pandas
    - very similar functions and methods
    - (not fully compatible)

--

## Data frames loading

```python
df = polars.read_csv("hall_of_fame.csv")

print(df)
print()

print("Column types")
print(df.dtypes)
print()

```

--

## Multiple input formats (TSV)

```python
import polars

df = polars.read_csv("hall_of_fame.tsv", sep="\t")

print(df)
print()

print("Column types")
print(df.dtypes)
print()
```

--

## Loading directly from database

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

--

## Processing/querying data - source

```
Year,Winner
2022,C++
2021,Python
2020,Python
2019,C
2018,Python
2017,C
2016,Go
2015,Java
2014,JavaScript
2013,Transact-SQL
2012,Objective-C
2011,Objective-C
2010,Python
2009,Go
2008,C
2007,Python
2006,Ruby
2005,Java
2004,PHP
2003,C++
```

--

## Processing/querying data

```python
import polars

df = polars.read_csv("hall_of_fame.csv")

polars.Config.set_tbl_rows(100)

df = df.sort("Winner")
```

--

## Processing data

```python
import polars

df = polars.read_csv("tiobe.tsv", sep="\t")

df2 = df.with_column(
    polars.col("Ratings").apply(lambda x: x / 100.0).alias("Ratings as ratio")
)

print(df)
print()
```

--

## Groupby + aggregation

```python
import polars

df = polars.read_csv("hall_of_fame.csv")

df = df.groupby("Winner", maintain_order=True).agg([polars.col("Year").sort()])

print(df)
```

--

## Groupby + aggregation + sort

```python
import polars

df = polars.read_csv("hall_of_fame.csv")

df = df.groupby("Winner", maintain_order=True).agg([polars.col("Year").len()]). \
     sort("Year"). \
     reverse(). \
     head(5)

print(df)
```

--

## The key to success in IT: be lazy!

* Laziness in FP
* All those Kafka-based architectures postpone execution
* Lazy data frames in Polars

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

--

## Plans for lazy evaluation

```
  SLICE[offset: 0, len: 5]
     LOCAL SELECT [col("Winner").reverse(), col("Year").reverse()] FROM
      SORT BY [col("Year")]
        Aggregate
                [col("Year").count()] BY [col("Winner")] FROM
                  DF ["Year", "Winner"]; PROJECT */2 COLUMNS; SELECTION: "None"


  SLICE[offset: 0, len: 5]
     LOCAL SELECT [col("Winner").reverse(), col("Year").reverse()] FROM
      SORT BY [col("Year")]
        Aggregate
                [col("Year").count()] BY [col("Winner")] FROM
                  DF ["Year", "Winner"]; PROJECT 2/2 COLUMNS; SELECTION: "None"
```
