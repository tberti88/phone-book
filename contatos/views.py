from django.shortcuts import render, get_object_or_404
from .models import Contato
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True

    )
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render (request, 'contatos/index.html', {
        'contatos': contatos

    })

def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })

def busca (request):
    termo = request.GET.get('termo')

    contatos = Contato.objects.order_by('nome').filter(
        nome__icontains=termo, #nome parcial
        mostrar=True

    )
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render (request, 'contatos/busca.html', {
        'contatos': contatos

    })