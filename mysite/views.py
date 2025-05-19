from django.shortcuts import render
from .data import pricing, services


def index(request):
    return render(request, 'index.html', {'services': services.services, 'pricing': pricing.pricing})


