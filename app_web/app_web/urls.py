"""app_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from manage.views import login_view, recuperation_view, inscription_view, acceuil_view, acceuil_admin_view, modif_edt_view, creation_edt_view, entrer_notif_view, emploi_previews_view, emploi_previews_etu_view, notif_etu_view,comfirm_view, inscription_reussie
urlpatterns = [
   path('admin/', admin.site.urls),
   path ('connect/', login_view, name='login'),
   path('recuperation/', recuperation_view, name='recuperation'),
   path('inscription/', inscription_view, name='inscription'),
   path('acceuil/', acceuil_view, name='acceuil'),
   path('acceuil_admin/', acceuil_admin_view, name='acceuil_admin'),
   path('modifier/', modif_edt_view, name='modifier_edt'),
   path('creation/', creation_edt_view, name='creation_edt'),
   path('notif_admin/', entrer_notif_view, name='notif_admin'),
   path('emploi_previews/', emploi_previews_view, name = 'emploi_previews'),
   path('emploi_previews_etu/', emploi_previews_etu_view, name='emplois_previews_etu'),
   path('notif_etu/', notif_etu_view, name='notif_etu'),
   path('confirm/', comfirm_view, name='confirm'),
  
    path('ins/reussie/',inscription_reussie, name='ins_reussie'),
]
