# %% 
x = 10
y = 15
print(x)
print(y)

# %%
x = 4
x = "Sally" 
print(x)

# %%
## casting
x = str(3) 
y = int(3)
z = float(3)
print(x, type(x))
print(y, type(y))
print(z, type(z))

# %%
## case-sensitive for variables
a = 4
A = "Sally"
print(a)
print(A) # A will not override a

# %%
## ilegal variables names
## variables names are case sensitive
2var = "And"
-var = "And"
my-var = "And"
my var = "And"

# %%
## acceptable patterns to use variables names with multiple words
### camel case -> each word, except the first, starts with a capital letter
andersonVariableCamelCase = "Value"
### pascal case -> each word starts with a capital letter
AndersonVariablePascalCase = "Value"
### scanke case -> each word is separated by an underscore character
anderson_variable_snake_case = "Value"

# %%
## define multiple variables
### to assign values to multiple variables in one line
x, y, z = "Anderson", "Diego", "Lucas"
print(x, ";", y, ";", z)

# %%
## global variables
### variables that are created ouside of a func scope are known as global variables
### global variables can be used by everyone, both inside of functions and ouside.
x = "i'm glad for you"

def my_func():
    print("showing my global variable", x)

my_func()

# %%
## constants -> python doesn't have constants, perhaps, we have alternatives to do this.
## to indicate to programmers that a variable is a constant, one usually writes it in snake case in upper case:
CONST_NAME = "Name"
print(CONST_NAME)

## define a function
def MY_CONSTANT():
    return 42
print(MY_CONSTANT())

## As of Python 3.8, there's a typing.Final
from typing import Final
a: Final[int] = 1
# Executes fine, but mypy will report an error
a = 2

MAX_SIZE: Final = 9000
MAX_SIZE += 1  # Error reported by type checker

# %%
