from django.shortcuts import render
from . import models
from django.shortcuts import redirect
# Create your views here.
def index(request):
    return render(request, 'index.html' )

def central(request):
    return render(request, 'centralOngs.html')

def peludos(request):
    anim = models.pet.objects.all()
    return render(request,'peludos.html', {'anim': anim})

def out(request):
    url = "https://www.instagram.com/peludosunipe/"
    return redirect(url)

