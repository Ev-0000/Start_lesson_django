from django.urls import path
from . import views

app_name = 'advertisement'

urlpatterns = [
    path('', views.index, name='index'),
    path('course', views.cours, name='cours'),
    path('shop', views.shop, name='shop'),
    path('newspaper', views.newspaper, name='newspaper'),
    path('works', views.works, name='works'),
    ]