from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('pdfs/catalog',views.pdf,name='pdf'),
]