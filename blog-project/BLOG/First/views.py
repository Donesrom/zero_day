from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    psts=Posts.objects.all()
    context = {'psts':psts}
    return render(request, "index.html",context)