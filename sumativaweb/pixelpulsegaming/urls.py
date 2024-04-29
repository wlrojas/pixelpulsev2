from django.urls import path
from pixelpulsegaming import views

urlpatterns = [
    path('', views.categoria, name='categorias'),
    path('monitores', views.monitores, name='monitores'),
    path('notebooks', views.notebooks, name='notebooks'),
    path('perifericos', views.perifericos, name='perifericos'),
    path('procesadores', views.procesadores, name='procesadores'),
    path('sillasgamer', views.sillasGamer, name='sillasgamer'),
    path('tarjetasvideo', views.tarjetasDeVideo, name='tarjetasvideo'),
    path('carrito', views.carrito, name='carrito'),
    path('logout', views.logout, name='logout'),
]
