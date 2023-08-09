from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout

def index(request):
    return HttpResponse('Something Amazing Coming Soon')

def pdf(request):
    return redirect('/static/uploads/catalog/catalog.pdf')




# Create your views here.