"""
URL configuration for show_delete_exos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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

from members.views import *
from cars.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homeMembers, name="homeMembers"),
    path("members/men/", homeMen, name="men"),
    path("members/women/", homeWomen, name="women"),
    path("members/create/", createMember, name="create"),
    path("members/destroy/<int:id>", destroy, name="destroy"),
    path("cars/", homeCars, name="homeCars"),
    path("cars/create/", createCar, name="createCar"),
    path("cars/cars/destroy/<int:id>", destroyCar),
]
