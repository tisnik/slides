# Functional Python

---

![Python](images/python.png)

# λ

---


## Functional programming

- Functions are first-class citizens
- Pure functions (w/o side effects)
- Immutable values are preffered
    - purely functional data structures

---

## Why?

- Pure functions are super easy to test
    - mock? super trivial
- Alse much easier to debug
- Functional code have state isolated
    - easier to comprehend
    - easier to test
- Concurrency can be made safe(r)
- Immutable variables lead to fewer side-effects 

---

## "Functions are first-class citizens"

- It has huge consequences!
    - higher order functions must be supported
    - closures must be usually supported too
    - non-local changes in mutable state

---

## "Functions are first-class citizens"

- Functions can be composed
- Functions can be transformed
    - (curryfication in some languages)
- Functions can be "cached"
    - pure function is like mapping

---

## So ... functional Python?

- Functions are first-class citizens?
    - yes (with all the consequences)
    - function literal - messy!
- Immutable data types?
   - sort of

---

## Functional concepts in Python

- Higer order functions
- Lambdas (very limited)
- Closures
- Generator expression
    - list & set & dict & tuple comprehensions
- Partial functions
    - transformation
- Caching functions

--- 

## Practical part

---

### Higher order functions

- must exist by definition
- standard functions
    - `map`
    - `filter`
    - `reduce` from functools

---

#### `map`

---

#### `filter`

---

#### `reduce`

---

### Lambdas

- anonymous functions
- not fully true in Python
    - it's basically just an expression

---

#### Lambdas

---

### Closures

- must exist because:
    - functions are first class citizens
    - variables outside current block are accessible
- problems in Python
    - not global, not local variables
    - mutable access

---

#### Counter (incorrect)

---

#### Counter (correct)

---

### Generator expressions

- pretty nice way how to rewrite `map` and `filter`
    - tuple comprehension
    - list comprehension
    - set comprehension
    - dict comprehension

---

#### Tuple comprehension

---

#### List comprehension

---

#### Set comprehension

---

#### Dict comprehension

---

### Partial functions

---

#### `partial` usage

---

### `partialmethod` usage

---

### Caching

- pure functions
     - return values depends only on parameters
     - it is a mapping, nothing else
     - can be cached

---

#### `lru_cache` usage
