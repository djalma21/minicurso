from django.shortcuts import render,redirect, get_object_or_404
from .models import Contato
from .forms import ContatoForm

def listar_contatos(request):
    busca = request.GET.get('pesquisa', None)

    if busca:
        contatos = Contato.objects.all()
        contatos = contatos.filter(nome__icontains=busca)

    else:
        contatos = Contato.objects.all()


    return render(request, 'lista.html',{'contatos': contatos})

def criar_contato(request):
    form = ContatoForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('listar_contatos')

    else:
        return render(request, "novo_contato.html", {'form': form})

def alterar_contato(request, id):
    contato = get_object_or_404(Contato, pk=id)
    form = ContatoForm(request.POST or None, request.FILES or None, instance=contato)

    if form.is_valid():
        form.save()
        return redirect('listar_contatos')

    return render(request, 'novo_contato.html', {'form': form})


def deletar_contato(request, id):
    contato = get_object_or_404(Contato, pk=id)

    if request.method == 'POST':
        contato.delete()
        return redirect('listar_contatos')

    return render(request, 'deletar_contato.html', {'contato': contato})