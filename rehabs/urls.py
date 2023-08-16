from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('pdfs/catalog',views.pdf,name='pdf'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('products',views.products,name='products'),
    path('contact-data',views.contact_data,name='contact-data'),
    path('products/<joint>',views.products_joint,name='products-joint'),


    # path('super-root-user',views.login,name='super-root-user')


]