# Functional Python

---

![Python](images/python.png)

---


## Functional programming

- Functions are first-class citizens
- Pure functions (w/o side effects)
- Immutable values are preffered
    - purely functional data structures

---

## Why?

- Pure functions are super easy to test
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
- Immutable data types?
   - sort of

---

