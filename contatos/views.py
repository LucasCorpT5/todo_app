from django.shortcuts import render
from .models import Contato

# Create your views here.
def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def ver_contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, "contatos/ver_contato.html", {
        'contato': contato
    })
