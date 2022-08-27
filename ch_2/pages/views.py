from django.http import HttpResponse


# Create your views here.
def home(request):
    # the home page view
    return HttpResponse("Hello, World!")
