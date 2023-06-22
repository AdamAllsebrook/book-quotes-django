from django.shortcuts import render

from .models import Quote


def index(request):
    quotes = Quote.objects.order_by('-created_at')
    return render(request, 'quotes/index.html', {'quotes': quotes})
