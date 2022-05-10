from django.shortcuts import render
from .models import Contato

# Create your views here.
def index(request):
    return render(request, 'contatos/index.html')