from django.shortcuts import render
from app.models import Produto
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    conteudos = {
        'curso' : 'Programação em python - Django Framework',
        'produto' : produtos
    }
    return render(request, 'index.html', conteudos)

def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    prod = get_object_or_404(Produto, id=id)
    conteudos = {
        'produto': prod
    }
    return render(request, 'produtos.html', conteudos)

def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)