from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    return render(request,'index.html')

def pets(request):
    return render(request,'models.pet')