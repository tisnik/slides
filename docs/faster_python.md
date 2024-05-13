# How to make Python faster

AOT, JIT and noGIL technologies 

---

* Pavel Tišnovský
* tisnik@centrum.cz

![Python](images/python.png)

---

# Where's the problem?

```python
def add_two_numbers(x, y):
    return x + y


z = add_two_numbers(123, 456)
print(z)

```
---

# Solutions

* AOT compiler
   - Cython
* JIT compiler
   - Numba

