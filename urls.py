from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('taomlar/<int:restorant_id>/',views.TaomView, name='TaomView'),
    path('savat/', views.savat, name='savat'), 
]
