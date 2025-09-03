# Intermediate Python 
By Jan Schaffranek on Udemy

---
## Repositories

[Intermediate Python: Memory, Decorator, Async, Cython & more](https://github.com/franneck94/UdemyPythonInt)

[Python: Coding Guidelines, Testing and Packaging](https://github.com/franneck94/UdemyPythonProEng)

## Notes

#### About integers and floats

```python
import sys

my_value = 42
print(f"Integer size: {sys.getsizeof(my_value)}")

# Integer size: 28
```

A simple integer variable needs 28 bytes to store because in python **everything is an object**.
So it needs to store object methods and attributes.

The same happens with **float type, needs more memory than the actual type value**. A simple float variable needs 8 bytes in memory but
uses 24 bytes, the rest of bytes is allocated to some _python class operations_

**The float equality is important;** You should never compare (`==`) two float variables.
Can be used some `math.floor` function to round some values in order to compare it or [`math.isclose` function](https://www.w3schools.com/python/ref_math_isclose.asp).

Reference [here](https://github.com/franneck94/UdemyPythonPro/tree/master/Chapter02_Basics/Numbers).

