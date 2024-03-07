from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from accounts.forms import UserRegistrationForm, UserUpdateForm, CustomLoginForm
from .forms import SearchForm
from django.conf import settings
from datetime import date

current_date = date.today()


def base_data(request):

    data = {}
    date = current_date.strftime("%d/%m/%Y")
    data["registration_form"] = UserRegistrationForm()
    data["login_form"] = CustomLoginForm()
    data["search_form"] = SearchForm()
    if request.user.is_authenticated:
        data["edit_form"] = UserUpdateForm(instance=request.user)
    
    data['date'] = date
    return data

