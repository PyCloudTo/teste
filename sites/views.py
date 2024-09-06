from django.shortcuts import render
from django.http import HttpResponse
from .form import MeuFormulario
from .models import OpcaoSelecionada

def meu_view(request):
    if request.method == 'POST':
        form = MeuFormulario(request.POST)
        if form.is_valid():
            opcoes_selecionadas = form.cleaned_data.get('opcoes')
            
            # Cria um novo registro no banco de dados
            OpcaoSelecionada.objects.create(opcoes=opcoes_selecionadas)

            # Retorna uma resposta com as opções selecionadas
            return HttpResponse(f'Você selecionou: {", ".join(opcoes_selecionadas)}')
    else:
        form = MeuFormulario()

    return render(request, 'sites.html', {'form': form})



def opcao_view(request):
    if request.method == 'POST':
        form2 = MeuFormulario(request.POST)
        if form2.is_valid():
            Opcao_Selecionada2 = form2.cleaned_data.get('opcoes')
            
            OpcaoSelecionada.objects.create(opcoes=Opcao_Selecionada2)
            
            return HttpResponse(f'Você selecionou: {",".join(Opcao_Selecionada2)}')
    else:
        form2 = MeuFormulario()
    return render(request, 'site.html', {'form2':form2})