from django.shortcuts import render
from . import models
# Create your views here.
def peludos(request):
    anim = models.pet.objects.all()
    return render(request,'peludos.html', {'anim': anim})