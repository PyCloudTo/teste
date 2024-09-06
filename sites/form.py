from django import forms

class MeuFormulario(forms.Form):
    OPCAO_CHOICES = [
        ('opcao1', 'Opção 1'),
        ('opcao2', 'Opção 2'),
        ('opcao3', 'Opção 3'),
    ]
    opcoes = forms.MultipleChoiceField(
        choices=OPCAO_CHOICES,
        widget=forms.CheckboxSelectMultiple,
    )