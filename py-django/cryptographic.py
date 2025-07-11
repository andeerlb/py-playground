# Django provides a low-level API for signing values 
# and a high-level API for setting and reading signed cookies, 
# one of the most common uses of signing in web applications.

# %%

# low-level API
from django.conf import settings

if not settings.configured:
    settings.configure(SECRET_KEY='safe-example')

from django.core.signing import Signer

signer = Signer()
value = signer.sign("My string")
print(value)

# You can retrieve the original value using the unsign method:
print(signer.unsign(value))

# If you pass a non-string value to sign, the value will be forced to string before being signed, and the unsign result will give you that string value
signed = signer.sign(2.5)
print(signed)
print(signer.unsign(signed))

# If you wish to protect a list, tuple, or dictionary you can do so using the sign_object() and unsign_object() methods
signed_obj = signer.sign_object({"message": "Hello!"})
print(signed_obj)
print(signer.unsign_object(signed_obj))
# %%
