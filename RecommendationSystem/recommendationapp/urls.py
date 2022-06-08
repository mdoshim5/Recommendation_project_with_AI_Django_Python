from os import name
from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index, name='home'),
    path("about/", views.aboutUs),
    path("allpackages/", views.allpackages),
    path("aboutus/", views.aboutUs),
    path("choseoptions/", views.choseoptions),
    path("choseoptions/don't-know-my-requirements/", views.dontknowmyrequirements),
    path("choseoptions/know-my-requirements/", views.knowmyrequirements),
]