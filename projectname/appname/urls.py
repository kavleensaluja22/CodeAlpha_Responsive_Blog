from django.contrib import admin 
from django.urls import path , include 
from appname import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home',views.home, name="home"),
    path('resume',views.resume, name="resume"),
    path('final',views.final,name="final"),
    path('r',views.r,name="r"),
    path('summary',views.summary,name="summary"),
    path('co',views.co,name="co"),
    path('edu',views.edu,name="edu"),
    path('ex',views.ex,name="ex"),
    path('ho',views.ho,name="ho"),
    path('lang',views.lang,name="lang"),
    path('sk',views.sk,name="sk"),
]