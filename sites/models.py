from django.db import models

# Create your models here.


class OpcaoSelecionada(models.Model):
    opcoes = models.JSONField()  # JSONField para armazenar a lista de opções selecionadas

    def __str__(self):
        return str(self.opcoes)
    
    
    


class opcao(models.Model):
    opcao = models.JSONField()
    
    def __str__(self):
        return self.opcao