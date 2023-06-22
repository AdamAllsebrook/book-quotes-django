from django.shortcuts import render

from .models import Quote
from .forms import QuoteForm


def index(request):
    quotes = Quote.objects.order_by('-created_at')
    form = QuoteForm()
    return render(request, 'quotes/index.html', {'quotes': quotes, 'form': form})


def add_quote(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)

        if form.is_valid():
            quote = form.save()
            return render(request, 'quotes/_quote.html', {'quote': quote})
