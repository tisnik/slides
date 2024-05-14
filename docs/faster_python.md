# How to make Python faster

AOT, JIT and noGIL technologies 

---

* Pavel Tišnovský
* tisnik@centrum.cz

![Python](images/python.png)

---

## Where's the problem?

```python
def add_two_numbers(x, y):
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

---

## Where's the problem?

```python
def worker():
    """Some task that takes time."""

# let's try multithreading
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
threading.Thread(target=worker).start()
# oh no
```

---

### Goal

---

![C](images/c.png)

---

# Solutions

* AOT compilers
* JIT compilers
* "no GIL" variants

---

## AOT

* Ahead-of-time compilation
* Performed before execution
    - or part of startup
* More aggressive
    - can be time consuming
* Can be made part of CI/CI
* Can not perform PGO (Profile Guided Optimization)
* Can not fully perform speculative optimizations

---

## JIT

* Just-in-time compilation
* Performed during execution
* Need to be a bit picky
    - too aggressive optimizations lower performance
* Is able to perform PGO (Profile Guided Optimization)
* Is able to perform speculative optimizations
    - can backtrack if things go wrong

---

## Cython

* Superset of Python programming language
* Compiled language
    - in fact it is transpiller to C
    - .pyx -> .c -> .so -> launch.py
* Explicit data types are optional
    - type hints
* `nogil`
* Ability to call native functions

---

### Compilation into C

```python
cdef add_two_numbers(x, y):
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

---

### Explicit parameter types

```python
cdef add_two_numbers(int x, int y):
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

---

### Explicit return type

```python
cdef int add_two_numbers(int x, int y):
    return x + y


z = add_two_numbers(123, 456)
print(z)
```

