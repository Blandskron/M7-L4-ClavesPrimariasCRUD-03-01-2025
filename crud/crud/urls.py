"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.estudiante_list, name='estudiante_list'),
    path('estudiante/create/', views.estudiante_create, name='estudiante_create'),
    #http://edutecno.com/estudiante/1/
    path('estudiante/<int:pk>/', views.estudiante_detail, name='estudiante_detail'),
    #http://edutecno.com/estudiante/2/update/
    path('estudiante/<int:pk>/update/', views.estudiante_update, name='estudiante_update'),
    #http://edutecno.com/estudiante/3/delete/
    path('estudiante/<int:pk>/delete/', views.estudiante_delete, name='estudiante_delete'),
]
