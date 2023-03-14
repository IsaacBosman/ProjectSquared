from django.shortcuts import render
from django.http import HttpResponse

from .forms import SpSheetForm

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index")

def index(request):
    return render(request, 'index.html')

def weights_page(request):
    return render(request, 'weights_table.html')