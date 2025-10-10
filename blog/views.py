from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.template import loader
#from django.contrib.auth import login_required



def home(request):
    return render(request, 'home.html')
def login_view(request):
    return render(request, 'login.html')
def logout_view(request):
    return HttpResponse("Logout bem-sucedido.")
def register(request):  
    return render(request, 'cadastro.html')
def profile(request): 
    return render(request, 'perfil.html')
def password_reset(request): 
    return render(request, 'recuperarsenha.html')
def password_change(request): 
    return render(request, 'alterarsenha.html')
def error_404(request,):
    return render(request, '404.html', status=404)
def error_500(request):
    return render(request, '500.html', status=500)
def error_403(request,):
    return render(request, '403.html', status=403)