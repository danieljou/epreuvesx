from functools import wraps
from django.http import HttpResponseRedirect
from .models import *
from django.shortcuts import render,redirect



# def is_admin_required(function):
#     @wraps(function)
#     def wrap(request, *args, **kwargs):
#         profile = request.user
#         account = Custum_user.objects.get(user = profile.id)
#         user_type = account.role
#         if(user_type == 'Administrateur'):
#             return function(request, *args, **kwargs)
#         else:
#             return HttpResponseRedirect('/')
#     return wrap


def is_admin_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if(request.user.is_admin):
            return function(request, *args, **kwargs)
        else:
            return redirect('redirect_user')
    return wrap


def id_professeur_required(function):
    @wraps(function)
    def wrap(request, *args, **kwargs):
        if(requets.user.Professeur or requets.user.is_admin):
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('redirect_user')
    return wrap
