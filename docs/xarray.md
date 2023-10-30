# Xarray: labelled multi-dimensional arrays in Python

---

![xarray](images/xarray1.png)

---

## Xarray

* nd-array with labels
    - name
    - dimensions
    - coordinates
    - user attributes

---

## Xarray

* pros
    - much more intuitive
    - metadata approach
    - concise
    - standard
    - less errors (no operations on wrong arrays/axes)
    - broadcasting based on dimension names (not shape)
    - super easy `groupby`

---

### Dimension

* "named axis"
* can be used as selector
* some "intelligent" `groupby` operations provided

---

### Coordinates

* logical "ticks" on each axis/dimension
* 0-index approach is w/o semantic
    - and thus error prone

---

### Array name, user metadata

* everything stored in one data structure
* possible to load/save it in standard netCDF format
    - based on HDF
    - used by NASA, NCSA etc.

---

## DataSet

* multi-dimensional, in-memory array database

![xarray](images/xarray2.png)

---

## Practical part

* see live demo!

