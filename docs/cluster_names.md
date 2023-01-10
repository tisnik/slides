# Cluster names benchmark (in progress)

--

## Cluster name

* represented as UUID
    - in format `123e4567-e89b-12d3-a456-426614174000`
* how to store it in PostgreSQL?
    - `char(36)`
    - `varchar(36)`
    - `bytea`
    - `uuid`

--

## Why bother?

* DB size
    - `char`: 36 bytes per record
    - `varchar`: 1 byte + 36 bytes per record
    - `bytea`: 1 byte + 36/2 bytes per record
    - `uuid`: 36/2 bytes per record (automatically converted to/from char)
* Performance
    - `column_name` is used in indices
    - so it's stored separately in B-tree or similar structure
    - and size matters there
    - (number of blocks stored in memory, number of block read for each query)

--

## Theory

* `uuid` might be the best option 
* `bytea` might be a bit worse
* `char` on third place
* `varchar` on the last place

--

## Don't trust theory...until proven

--

### Small tables with 100 records

```
```

--

### Medium tables with 1000 records

```
```

--

### Larger tables with 10000 records

```
```

--

### Huge tables with 100000 records

```
```

--

## Links

* [Character Types in PostgreSQL](https://www.postgresql.org/docs/current/datatype-character.html)
* [Binary Data Types in PostgreSQL](https://www.postgresql.org/docs/current/datatype-binary.html)
* [UUID Type](https://www.postgresql.org/docs/current/datatype-uuid.html)
