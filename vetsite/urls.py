"""vetsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vet import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('findowners.html',views.findowners, name='findowners'),
    path('ownerinfo/<ownerid>/',views.ownerinfo, name='ownerinfo'),
    path('ownereditor/<ownerid>/',views.ownereditor, name='ownereditor'),
    path('addowner.html',views.addowner, name='addowner'),
    path('addpets/<ownerid>/',views.addpets, name='addpets'),
    path('editpet/<petid>/',views.editpet, name='editpet'),
    path('addvisit/<petid>/',views.addvisit, name='addvisit'),
]
