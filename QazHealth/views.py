import os

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from allauth.account import views
import pandas as pd
import streamlit as st
from django.contrib.auth.models import User, auth


# Create your views here.
def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['repeatPassword']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('login')

    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        request.user.is_authenticated
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'register.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def is_verified(request):
    return views.EmailView.get_ajax_data(self=request.user.email)


def readFile(filename):
    file = pd.read_csv(filename, sep=',', engine='python')
    data = pd.DataFrame(data=file, index=None,
                        columns=['Аллергия, отдышка, сердце', 'Голова, Давление и Высокая Температура',
                                 'Общие вызовы, охлождения, ожоги', 'Психические, отравления и опьянения',
                                 'Рвота, Пена изо рта, Даабет', 'кровотечение', 'перевозки',
                                 'травмы внутрених органов, рук, ног и позвоночника'])
    return data


def predict(request):
    return render(request, 'predict.html')
