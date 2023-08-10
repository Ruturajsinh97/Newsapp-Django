from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name="index"),
    path('spnews',views.spnews,name="spnews"),
    path('topnews', views.topnews, name="topnews"),
    path('scinews', views.scinews, name="scinews"),
    path('trendnews', views.trendnews, name="trendnews"),
    path('entnews', views.entnews, name="entnews")

     ]