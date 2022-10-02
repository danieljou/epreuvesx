from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from .models import *
from .forms import *




def users_login(request):
    context = {}
   
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username = login, password = password) 
        if user is not None:
            return  redirect('redirect_user')
        else:
            messages.warning(request,'Erreur')
            return  render(request,'login_form.html')

    return render(request,'login_form.html')


def users_logout(request):
    logout(request)
    return redirect('login')

def account_management(request):
    context = {}
    context['all_account'] = User.objects.exclude(pk = request.user.id)
    

    return render(request, 'admin_comptes.html',context)


def account_add_user(request):
    context = {}
    context['card_color'] = 'bg-primary'
    context['form_card_title'] = 'Ajouter un personnel'
    context['submit_text'] = 'Ajouter'
    context['form_title'] = 'Compte | Ajouter un compte utilisateur'

    
    # formaulaire
    form = UserForm(request.POST or None)
    context['form'] = form
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('account_management')

    return render(request, 'form_page.html',context)



def account_upadate_user(request, account_id):
    context = {}
    account_object = User.objects.get(pk = account_id)
    context['card_color'] = 'bg-primary'
    context['form_card_title'] = 'Modifier le personnel'
    context['submit_text'] = 'Mettre à jour'
    context['form_title'] = 'Compte | Modifier le  compte utilisateur'

    
    # formaulaire
    form = UserUpadateForm(request.POST or None, instance = account_object)
    context['form'] = form
    if(request.method == 'POST'):
        if(form.is_valid()):
            form.save()
            return redirect('account_management')
    return render(request, 'form_page.html',context)


def account_delete_user(request, account_id):
    account_object = User.objects.get(pk = account_id)
    account_object.delete()
    return redirect('account_management')


def profile_user(request):
    context = {}
    form = UserAccount  (request.POST or None, request.FILES or None , instance  = request.user)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'profile.html',context)