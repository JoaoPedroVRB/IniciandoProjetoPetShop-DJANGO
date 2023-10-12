from django import forms
from base.models import contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = contato
        fields = ['nome','email','mensagem']

class ReservaForm(forms.Form):
    nome_do_pet = forms.CharField(max_length=50)
    telefone = forms.CharField(max_length=12)
    dia_da_reserva = forms.DateField()
    observacoes = forms.CharField(required=False, widget=forms.Textarea)