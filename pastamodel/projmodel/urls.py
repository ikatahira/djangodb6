from django.contrib import admin
from django.urls import path, include
from appmodelo import views  # Importe as views do aplicativo appmodelo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.pagina_inicial, name='pagina_inicial'),  # Página inicial
    path('clientes/cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),  # Rota para cadastrar cliente
    path('clientes/', views.listar_clientes, name='listar_clientes'),  # Rota para listar clientes
    path('produtos/cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),  # Rota para cadastrar produto
    path('produtos/', views.listar_produtos, name='listar_produtos'),  # Rota para listar produtos
    path('pedidos/cadastrar/', views.cadastrar_pedido, name='cadastrar_pedido'),
    path('pedidos', views.listar_pedido, name='listar_pedido'),
    path('listar_pedido/', views.listar_pedido, name='listar_pedido'),
    path('alterar_pedido/<int:pedido_id>/', views.alterar_pedido, name='alterar_pedido'),
    path('deletar_pedido/<int:pedido_id>/', views.deletar_pedido, name='deletar_pedido'),
    path('alterar_cliente/<int:cliente_id>/', views.alterar_cliente, name='alterar_cliente'),
    path('deletar_cliente/<int:cliente_id>/', views.deletar_cliente, name='deletar_cliente'),
    path('alterar_produto/<int:produto_id>/', views.alterar_produto, name='alterar_produto'),
    path('deletar_produto/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),


]
