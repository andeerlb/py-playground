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
## tuples vs lists -> The fundamental difference between a tuple and a list in Python lies in their mutability
## Lists: are mutable, meaning their elements can be changed (added, removed, or modified) after the list is created.
## Tuples: are immutable, meaning their elements cannot be changed after the tuple is created.
### Performance:
## Tuples are generally slightly faster and use less memory than lists for storing the same data because their fixed size allows for certain optimizations.
maintuple = ("apple", "android", "microsoft")
print(type(maintuple), len(maintuple), maintuple)
## Ordered
## When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
## Unchangeable
## Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

## allow duplicates values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

## Create Tuple With One Item

thistuple = ("apple",)
print(type(thistuple))

## NOT a tuple
thistuple = ("apple")
print(type(thistuple))

## tuple with multiples data types
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
# %%
## unpack tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# %% 
# If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red) # ['cherry', 'strawberry', 'raspberry'] as list

# %%
# If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic) # ['mango', 'papaya', 'pineapple']
print(red) # cherry
print(type(green), type(tropic), type(red))
# %%
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

# %%
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
# %%
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
# %%
# Return the number of times the value appears in the tuple
thistuple = (1, 3, 7, 8, "Anderson", "Anderson", "anderson", 6, 8, 5)

print(thistuple.count("Anderson"))
print(thistuple.index("Anderson")) # find the first occurrence of the specified value.
print(thistuple.index("not")) # raise an exception if the value is not found.

# %%
# updat tuple
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# %%
# set is a collection which is unordered, unchangeable, and unindexed
thisset = {"apple", "banana", "cherry"}
print(thisset)

# %%
# duplicates values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset, len(thisset), type(thisset))

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

# %%
# dictionaries are used to store data in key:value
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
# When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
# Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

cardict = {
  "brand": "Byd",
  "model": "Song Plus",
  "year": 2025
}

print(cardict)
print(cardict["brand"])
print(len(cardict))
print(type(cardict))

# %%
# use dict constructor
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
print(thisdict.get("name"), ";", thisdict["name"])
print(thisdict.keys())
# %%
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change
print(car)

# %%
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.update({"year": 2020})
print(thisdict)
thisdict.update([('year', 3), ('model', 4), ('brand', 5)])
print(thisdict)
thisdict.update([('b', 3), ('c', 4), ('d', 5)])
print(thisdict)
# %%
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

del thisdict["brand"] # removes the last inserted item (in versions before 3.7, a random item is removed instead)
print(thisdict)
del thisdict # delete the dictionary completely

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict.clear()
print(thisdict)
# %%

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
   print(x, thisdict[x])

print() 

for x in thisdict.values():
   print(x)

print()

for x in thisdict.keys():
  print(x)

print()

for key, value in thisdict.items():
   print(key, value)

# %%
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

mydict = dict(thisdict)
print(mydict)
# %%
nesteddict = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(nesteddict)
print(len(nesteddict), type(nesteddict))
print(nesteddict["child3"]["name"])

# %%
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)
print(len(myfamily), type(myfamily))
print(myfamily["child2"]["name"])
# %%
