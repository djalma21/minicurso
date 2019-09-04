from django.forms import ModelForm
from .models import Contato

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ['foto', 'nome', 'telefone1', 'email1', 'endereco', 'grupo']