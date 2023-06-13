# Static type checking for Python

---

![Mypy logo](images/mypy.png)

---

## Most popular languages

```
Dynamically typed    Statically typed
-------------------------------------
Python               C
JavaScript           C++
Ruby                 Go
Perl                 Rust
Matlab               Java
PHP                  Scala
```

---

## Popularity of dynamically typed languages

* Short edit-(compile)-run cycle
* Very easy to start using them
* Ideal for scripting
   - CLI
   - web browser (simple actions)

---

## Cons

* Not easy to use them in large projects
* Lot of unit tests needs to be written
    - and code coverage lies about real behaviour!!!
* Information about types are sometimes "hidden" in comments
* Much more work for IDEs to provide meaningful help

---

## Static types as optional language feature

```
Language       Static types provided by
---------------------------------------
JavaScript     TypeScript, Flow
Python         Mypy, Pyright, Pyre
Ruby           Sorbet
```

---

## Python

* Dynamically typed language
   - no plans to change that!
* Type annotations are fully optional
   - introduced in Python 3.5
   - named type hints (to not scary people)
* Mypy, Pyright, and Pyre are static checkers

---

## Mypy usage

```python
def add(a, b):
    return a+b
```

* `Any` type added everywhere automagically
   - its `Any`, really

---

## Type annotations

```python
def add(a:int, b:int) -> int:
    return a+b
```

---

## `bool` or `int`?

* Based on Python language specification!

```python
def add(a:int, b:int) -> int:
    return a+b

print(add(1, 2))
print(add(1, True))
print(add(1, False))
```

---

## List type

* Python 3.10

```python
l: list[int] = []
```

* Older Pythons

```python
from typing import List

l: List[int] = []
```

---

## Checking

```python
from typing import List

l: List[int] = [1, 2, 3]
```

```python
from typing import List

l: List[int] = [1, 2, None]
```

---

## Tuple data type

```python
from typing import Tuple

p: Tuple[int] = (1, 2, 3)
```

```python
from typing import Tuple

p: Tuple[int, int, int] = (1, 2, 3)
```

---

## Tuple data type

```python
from typing import Tuple

p: Tuple[int, float, bool, str] = (1, 3.14, True, "Hello")
```

```python
from typing import Tuple

p: Tuple[int, float, bool, str] = (2.0, 3.14, 1, "Hello")
```

---

## Really static type checking?

* Can't work everywhere!

```python
x = 21


def adder(a:int, b:int) -> int:
    return a+b


print(adder(x,x))
```

---

## Static checkers are ok most of time...

```python
x = "foo"


def adder(a:int, b:int) -> int:
    return a+b


print(adder(x,x))
```

---

## But sometimes it must fail...

```python
x = 21


def adder(a:int, b:int) -> int:
    return a+b


exec("x='foo'")

print(adder(x,x))
```

---

## Variance problem

* Type `T` is subtype of type `U` if we can use value of type `T` in places where type `U` is expected 

* But what about `List[T]` and `List[U]`?
    - not as clear as it might look like

---

## Variance problem

* Four types of variances
    - covariance
    - contravariance
    - invariance
    - bivariance

---

## Variance(s) example

* `Apple` is subtype of `Fruit` in all following examples

---

* Covariance
    - `List[Apple]` is subtype of `List[Fruit]`
* Contravariance
    - `List[Fruit]` is subtype of `List[Apple]`
* Invariance
    - `List[Fruit]` has no relation to `List[Apple]`
* Bivariance
    - `List[Apple]` is subtype of `List[Fruit]`
    - and at the same moment
    - `List[Fruit]` is subtype of `List[Apple]`

---

## Why to care about variance?

---

## Variance in Java

```java
class Fruit {
}

class Orange extends Fruit {
    public String toString() {
        return "Orange";
    }
}

class Apple extends Fruit {
    public String toString() {
        return "Apple";
    }
}

public class Variance1 {
    public static void mix(Fruit[] punnet) {
        punnet[0] = new Orange();
        punnet[1] = new Apple();
    }

    public static void main(String[] args) {
        Fruit[] punnet = new Fruit[2];
        mix(punnet);

        for (Fruit Fruit:punnet) {
            System.out.println(Fruit);
        }
    }
}
```

---

## Static type check ok, runtime failure!

```java
class Fruit {
}

class Orange extends Fruit {
    public String toString() {
        return "Orange";
    }
}

class Apple extends Fruit {
    public String toString() {
        return "Apple";
    }
}

public class Variance2 {
    public static void mix(Fruit[] punnet) {
        punnet[0] = new Orange();
        punnet[1] = new Apple();
    }

    public static void main(String[] args) {
        Fruit[] punnet = new Orange[2];
        mix(punnet);

        for (Fruit Fruit:punnet) {
            System.out.println(Fruit);
        }
    }
}
```

---

## Variance in Python

```python
from typing import List


class Fruit:
    pass


class Orange(Fruit):
    def __repr__(self):
        return "Orange"


class Apple(Fruit):
    def __repr__(self):
        return "Apple"


def printContent(punnet : List[Fruit]):
    for Fruit in punnet:
        print(Fruit)


punnet : List[Orange] = [Orange(), Apple(), Orange()]

printContent(punnet)
```

---

## Sequence instead of List

```python
from typing import Sequence


class Fruit:
    pass


class Orange(Fruit):
    def __repr__(self):
        return "Orange"


class Apple(Fruit):
    def __repr__(self):
        return "Apple"


def printContent(punnet : Sequence[Fruit]):
    for Fruit in punnet:
        print(Fruit)


punnet : Sequence[Orange] = [Orange(), Orange(), Orange()]

printContent(punnet)
```

