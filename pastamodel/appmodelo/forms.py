from django import forms
from .models import Cliente, Produto, Pedido

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'endereco']

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'produtos']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adiciona um widget personalizado para o campo cliente
        self.fields['cliente'].widget = forms.Select(choices=Cliente.objects.values_list('id', 'nome'))
