from django.urls import path
from . import views
from .views import home, login_view, logout_view, register, profile, password_reset, password_change, error_404, error_500, error_403

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
    path('cadastro/', views.register, name='cadastro'),
    path('perfil/', views.profile, name='perfil'),
    path('recuperar_senha/', views.password_reset, name='recuperarsenha'),
    path('alterar_senha/', views.password_change, name='alterarsenha'),
    path('404/', views.error_404, name='404'),
    path('500/', views.error_500, name='500'),
    path('403/', views.error_403, name='403'),
]