from django.http import HttpResponse, HttpRequest

# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello world, you are at the polls index.")