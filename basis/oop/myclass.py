# %%
class MyClass:
    myattr = "Anderson"

firstClassRef = MyClass()

print(firstClassRef)
print(firstClassRef.myattr)

# %%
# All classes have a function called __init__(), which is always executed when the class is being initiated.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"your name is {self.name} and you have {self.age} years old"
    
    def my_func(self):
        print("it is my own func " + self.name)

p = Person("Anderson", 29)
print(p)
print(p.name, p.age)
p.my_func()
# %%
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
  pass
