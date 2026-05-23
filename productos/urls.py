from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),

    path('agregar/', views.agregar_producto, name='agregar_producto'),

    path('editar/<int:id>/', views.editar_producto, name='editar_producto'),

    path('eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),
]