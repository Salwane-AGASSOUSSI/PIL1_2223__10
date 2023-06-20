from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('emploi_temps.urls')),
    path('emploi-temps/', views.emploi_temps_view, name='emploi_temps'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
