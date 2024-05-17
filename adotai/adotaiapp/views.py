from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    anim = models.pet.objects.all()
    return render(request,'index.html', {'anim': anim})