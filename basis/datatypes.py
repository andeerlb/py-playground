# %%
## common types
a = "Hello world" # str
b = 20 # int
c = True # bool
d = 20.6 # float
e = b"Hello" # bytes
f = None # None
print(type(a),",",type(b),",",type(c),",",type(d),",",type(e),",",type(f))

# %%
## Lists are used to store multiple items in a single variable.
a = ["anderso", "ediane", "payment"]
print(type(a), len(a))
print(a)
a.append("marcelo")
a.append("marcelo")
print(a, len(a))

a.append(True) # type: ignore
a.append(2.56) # type: ignore
print(a, len(a))
print(type(a))

# %%
# Using the list() constructor to make a List:
b = list(("teste", "teste2", "teste3", 5, "The last item")) # note the double round-brackets
print(b, len(b), type(b))

print(b[0], b[len(b)-1], b[-1], b[-2])
print(b[0:-1])
print(b[0:3])
print(b[2:])
print(b[:4])
# This example returns the items from "teste2" (-4) to, but NOT including "The last item" (-1):
print(b[-4:-1])
# Check if Item Exists
if "teste2" in b:
    print("testes2 exists in b")

# %%
# join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# %%
# copy lists
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# %% 
# sort lists
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# %%

