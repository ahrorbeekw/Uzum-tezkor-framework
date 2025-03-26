from django.shortcuts import render, get_object_or_404
from .models import Restorantlar, Mahsulotlar

def index(request):
    res = Restorantlar.objects.all().order_by('-created_time')
    context = {  
        'Restorantlar': res
    }
    return render(request, 'index.html', context)

def TaomView(request, restorant_id):
    restorant = get_object_or_404(Restorantlar, id=restorant_id)
    taomlar = Mahsulotlar.objects.filter(restorant_id=restorant)
    
    context = {  
        'restorant': restorant,
        'taomlar': taomlar
    }
    return render(request, 'Taomlar.html', context)


def savat(request):
    return render(request, 'savat.html',)