from django.shortcuts import redirect, render
from django.contrib.auth import logout as auth_logout

def login(request):
    return render(request, 'vandoxyapp/login.html',{'name':'rabi'})

def signup(request):
    return render(request, 'vandoxyapp/signup.html')

def homepage(request):
    return render(request, 'vandoxyapp/home.html')



def search_page(request):
    return render(request, 'vandoxyapp/search.html')

def depot_page(request):
    return render(request, 'vandoxyapp/depot.html')

def favorite_page(request):
    return render(request, 'vandoxyapp/favorite.html')

def menssage_page(request):
    return render(request, 'vandoxyapp/message.html')


def logout_function(request):
    #clean all social sessions
    auth_logout(request)
    return redirect('login')
