from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'index.html')


def predict(request):
    return render(request, 'predict.html')
