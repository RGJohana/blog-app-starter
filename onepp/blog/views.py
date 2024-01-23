from django.http import HttpResponse

# Create your views here.
def blog_home(request):
    return HttpResponse("¡Hola, esta es la página principal del blog!")

