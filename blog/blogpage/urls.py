from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = {
    path('', views.helloWorld, name='helloWorld'),
    path('page', views.index, name='index')
}