from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weights_tracker', views.weights_page, name='weights'),
]