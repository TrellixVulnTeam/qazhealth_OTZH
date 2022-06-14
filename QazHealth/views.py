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
    data = pd.read_csv('media/all_data.csv')

    data_columns = data.columns
    data_values = data.values
    context = {
        'data_columns': data_columns,
        'data_values': data_values,
    }

    return render(request, 'index.html', context)

def page(request):
    return render(request, 'auth.html')

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect('signin')

    else:
        return render(request, 'auth.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'auth.html')
    else:
        return render(request, 'auth.html')


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
    # csvfile = request.FILES['csv_file']
    data = pd.read_csv('media/all_data.csv')
    data_html = data.to_html()
    context = {'loaded_data': data_html}
    return render(request, "predict.html", context)
