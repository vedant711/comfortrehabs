from django.urls import path

from . import views

urlpatterns = [
    path('',views.login1, name='login'),
    # path('super-root-user',views.login,name='super-root-user')
    path('contact',views.contact,name='contact'),
    path('products',views.product,name='product'),
    path('people',views.people,name='people'),
    path('joints',views.joints,name='joints'),
    path('products_add',views.product_add,name='product_add'),
    path('joints_add',views.joints_add,name='joints_add'),
    path('people_add',views.people_add,name='people_add'),
    path('edit-joints/<id>',views.edit_joints,name='edit_joints'),
    path('edit-products/<id>',views.product_edits,name='edit_products'),
    path('edit-people/<id>',views.people_edit,name='edit_people'),
    path('delete-joints/<id>',views.remove_joint,name='remove_joint'),
    path('delete-products/<id>',views.remove_product,name='remove_product'),
    path('delete-people/<id>',views.remove_people,name='remove_people'),
    path('delete-contact/<id>',views.remove_contact,name='remove_contact'),


    
    

    path('logout',views.logout_root,name='logout')



]

handler404 = 'rehabs.views.error404'
handler500 = 'rehabs.views.error500'