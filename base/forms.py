from django import forms
from base.models import Contato,Reserva

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome','email','mensagem']

        widgets = {
            'nome': forms.TextInput(
                attrs= {
                    'placeholder': 'Insira o seu nome aqui !'
                }
            ),

             'email': forms.TextInput(
                attrs= {
                    'placeholder': 'Insira o seu e-mail aqui !'
                }
            ),

             'mensagem': forms.TextInput(
                attrs= {
                    'placeholder': 'Insira a sua mensagem aqui !'
                }
            )
        }
        labels = {
            'nome': 'Nome:',
            'email': 'E-mail:',
            'mensagem': 'Mensagem:'
        }

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nome_pet','telefone','dia_reserva','observacao']

        widgets = {
            'nome_pet': forms.TextInput(
                attrs= {
                    'placeholder': 'Insira o nome do seu pet aqui !'
                }
            ),

             'telefone': forms.TextInput(
                attrs= {
                    'placeholder': 'Insira seu telefone aqui !'
                }
            ),

            'data_reserva': forms.DateInput(),

             'observacao': forms.TextInput(
                attrs= {
                    'placeholder': 'Insira a sua observação aqui !'
                }
            )
        }

        labels = {
    'nome_pet': 'Nome do Pet:',
    'telefone': 'Telefone:',
    'dia_reserva': 'Dia da Reserva:',
    'observacao': 'Observação:'
}