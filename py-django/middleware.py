# Each middleware component is responsible for doing some specific function. 
# For example, Django includes a middleware component, AuthenticationMiddleware, 
# that associates users with requests using sessions.

# %%
# Writing your own middleware
# A middleware can be written as a function that looks like this:
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

# Or it can be written as a class whose instances are callable, like this:
class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

# The get_response callable provided by Django might be the actual view (if this is the last listed middleware) or it might be the next middleware in the chain. The current middleware doesn’t need to know or care what exactly it is, just that it represents whatever comes next.

# Activating middleware
# to activate a middleware component, add it to the MIDDLEWARE list in your Django settings.
# The order in MIDDLEWARE matters because a middleware can depend on other middleware.

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "SimpleMiddleware"
]