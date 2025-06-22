# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# %%
from typing import Callable
a: Callable[[int], int] = lambda a : a + 10
print(a(5))
# %%
from typing import Callable
b: Callable[[int, int], int] = lambda a, b : a * b
print(b(5, 6))
# %%
from typing import Callable
c: Callable[[int, int, int], int] = lambda a, b, c : a + b + c
print(c(5, 6, 2))
# %%
from typing import Callable
def myfunc(n: int) -> Callable[[int], int]:
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
# %%
