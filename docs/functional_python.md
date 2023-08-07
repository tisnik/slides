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

### Lambdas

- anonymous functions
- not fully true in Python
    - it's basically just an expression

---

### Lambdas

```python
(lambda x,y:x+y)(1, 2)

foo=lambda x,y:x+y
foo(1,2)
```

---

### Higher order functions

- must exist by definition
- standard functions
    - `map`
    - `filter`
    - `reduce` from functools

---

#### Higher order functions

```python
def foo():
    def bar():
        print("BAR")
    return bar

x = foo()
x()
```

---

#### Higher order functions

```python
def add(x, y):
    return x + y


def mul(x, y):
    return x * y


def less_than(x, y):
    return x < y


def get_operator(symbol):
    operators = {
            "+": add,
            "*": mul,
            "<": less_than,
    }
    return operators[symbol]


def calc(operator, x, y):
    return operator(x, y)


z = calc(get_operator("+"), 10, 20)
print(z)

z = calc(get_operator("*"), 10, 20)
print(z)

z = calc(get_operator("<"), 10, 20)
print(z)
```

---

#### `map`

```python
values = range(-10, 11)

converted = map(abs, values)
print(list(converted))
```

---

#### `filter`

```python
message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

filtered = filter(lambda word: len(word) > 4, words)
print(list(filtered))
```

---

#### `reduce`

```python
from functools import reduce


def multiply(x, y):
    return x * y


x = range(1, 11)
print(x)

y = reduce(multiply, x)
print(y)
```

---

### Factorial computation

```python
n = range(0, 11)

factorials = map(lambda n: reduce(lambda a, b: a*b, range(1, n+1), 1), n)

print(list(factorials))
```

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

```python
def createCounter():
    counter = 0
    def next():
        counter += 1
        return counter
    return next

counter1 = createCounter()
counter2 = createCounter()
for i in range(1,11):
    result1 = counter1()
    result2 = counter2()
    print("Iteration #%d" % i)
    print("    Counter1: %d" % result1)
    print("    Counter2: %d" % result2)
```

---

#### Counter (correct for Python 2.x)

```python
def createCounter():
    counter = [0]
    def next():
        counter[0] += 1
        return counter[0]
    return next
```

---

#### Counter (correct for Python 3.x)

```python
def createCounter():
    counter = 0
    def next():
        nonlocal counter
        counter += 1
        return counter
    return next
```

---

### Generator expressions

- pretty nice way how to rewrite `map` and `filter`
    - tuple comprehension
    - list comprehension
    - set comprehension
    - dict comprehension

---

#### Tuple comprehension

```python
```

---

#### List comprehension

```python
message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"
words = message.split()

lengths = [len(word) for word in words]
```

---

#### Set comprehension

```python
```

---

#### Dict comprehension

```python
```

---

### Partial functions

---

#### `partial` usage

```python
from functools import partial


def mul(x, y):
    return x * y


print(mul(6, 7))

print()

doubler = partial(mul, 2)


for i in range(11):
    print(i, doubler(i))
```

---

### `partialmethod` usage

```python
class Foo:
    def __init__(self):
        self._enabled = False

    def set_enabled(self, state):
        self._enabled = state

    enable = partialmethod(set_enabled, True)
    disable = partialmethod(set_enabled, False)

    def __str__(self):
        return "Foo that is " + ("enabled" if self._enabled else "disabled")
```

---

### Caching

- pure functions
     - return values depends only on parameters
     - it is a mapping, nothing else
     - can be cached

---

#### `lru_cache` usage

```python
from time import time
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 300

for _ in range(10):
    start = time()
    result = fib(max_n)
    end = time()
    print(result, end - start)
```

---

#### `lru_cache` usage #2

```python
from time import time
from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 300

for i in range(20):
    if i % 5 == 0:
        fib.cache_clear()
    print(fib.cache_info())
    start = time()
    result = fib(max_n)
    end = time()
    print(result, end - start)
```

---

#### `cache` usage

```python
from time import time
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


max_n = 300

for i in range(20):
    if i % 5 == 0:
        fib.cache_clear()
    print(fib.cache_info())
    start = time()
    result = fib(max_n)
    end = time()
    print(result, end - start)
```
