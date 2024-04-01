from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto)
    data_pedido = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id} - Cliente: {self.cliente.nome}"

