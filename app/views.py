from django.shortcuts import render
from datetime import datetime


# Create your views here.
def index(request):
    products = [
        {'name': 'Laptop', 'price': 999.99},
        {'name': 'Smartphone', 'price': 499.99},
        {'name': 'Headphones', 'price': 99.99},
        {'name': 'Camera', 'price': 799.99},
    ],
    context = {
        "products": products,
    }
    return render(request, "app/index.html", context)
