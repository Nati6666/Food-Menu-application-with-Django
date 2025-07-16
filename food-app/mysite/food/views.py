from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("🍽️ Hello, this is the Food App index page!")


def item(reduest):
    return HttpResponse("<h1>🍕 This is a specific food item page!</h1>")