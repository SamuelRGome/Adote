from django.shortcuts import render
from . import models
from django.shortcuts import redirect
# Create your views here.
def peludos(request):
    anim = models.pet.objects.all()
    return render(request,'peludos.html', {'anim': anim})

def out(request):
    url = "https://www.instagram.com/peludosunipe/"
    return redirect(url)

