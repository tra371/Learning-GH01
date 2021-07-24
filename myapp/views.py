from django.shortcuts import render
from .models import Feature

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    words = request.POST['words']
    word_length = len(words.split())
    return render(request, 'counter.html', {'length': word_length})