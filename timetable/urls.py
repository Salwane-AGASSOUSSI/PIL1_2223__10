from django.urls import path
from . import views

urlpatterns = [

    path('creer/',views.creer, name='creer'),
    path('confirmation/', views.confirmation,name='confirmation'),
    path('accounts/profile/',views.consultation, name='consultation'),
    path('emploi/<int:pk>/modifier/',views.modification,name='modification'),
    
    
   
]