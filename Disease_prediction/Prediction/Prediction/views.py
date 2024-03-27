
from django.http import HttpResponse, JsonResponse

def home_page(request):
    print("Home page requested")
    return HttpResponse("This is home")