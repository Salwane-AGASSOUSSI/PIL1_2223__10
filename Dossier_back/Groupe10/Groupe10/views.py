from django.shortcuts import render
from .models import EmploiTemps

def emploi_temps_view(request):
    emplois_temps = EmploiTemps.objects.all()
    return render(request, 'emploi_temps/emploi_temps.html', {'emplois_temps': emplois_temps})
