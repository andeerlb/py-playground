# %%
print("double quotes")
print('simple quotes')

# %%
'a' + 'b'

# %%
'ab' * 4

# %%
'a' - 'b'

# %%
print('It\'s an escaped quote!')
print("I'm a so-called \"script kiddie\"")

# %%
print("""This is line 1,
... this is line 2,
... this is line 3."""
'This is line 1,\nthis is line 2,\nthis is line 3.')
# %%
price = 59
txt = f"The price is {price} dollars"
print(txt)

txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

# %%
