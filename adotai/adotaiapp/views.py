from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect
# Create your views here.
def peludos(request):
    anim = models.pet.objects.all()
    return render(request,'peludos.html', {'anim': anim})

def out(request):
    return HttpResponseRedirect("Instagram.com", {'out': out})
