from django.http import HttpResponse
from .models import Item
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    items = Item.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'food/index.html', context)


def item(reduest):
    return HttpResponse("<h1>🍕 This is a specific food item page!</h1>")


def item_detail(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'item': item,
    }
    return render(request, 'food/detail.html', context)
    # template = loader.get_template('food/detail.html')