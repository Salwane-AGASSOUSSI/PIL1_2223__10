
from django.shortcuts import render, redirect
from .models import EmploiTemps
from .forms import InscriptionForm

def login_view(request):
    return render(request, 'connexion.html')

def recuperation_view(request):
    return render(request, 'recuperation.html')


def acceuil_view(request):
    return render(request, 'acceuil.html')

def acceuil_admin_view(request):
    return render (request, 'acceuil_administrateur.html')
def modif_edt_view(request):
    return render(request, 'modifier_edt.html')
def creation_edt_view(request):
    return render (request, 'creation_edt.html')
def entrer_notif_view (request):
    return render (request, 'entrer_notification_admin.html')
def emploi_previews_view(request):
    return render(request, 'emploi_previews.html')
def emploi_previews_etu_view(request):
    return render (request, 'emplois_previews_etu.html')
def notif_etu_view(request):
    return render(request, 'notif_etu.html')
def comfirm_view(request):
    return render(request, 'confirm_message.html')


def inscription_view(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ins_reussie')
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})

def inscription_reussie(request):
    return render(request, 'cool.html')




def add_emploi_temps(request):
    if request.method == 'POST':
        specialite = request.POST.get('specialite')
        niveau_etude = request.POST.get('niveau')
        semaine = request.POST.get('semaine')
        jour = request.POST.getlist('jour[]')
        intitule_cours = request.POST.getlist('intitule[]')
        nom_professeur = request.POST.getlist('professeur[]')
        materiel_necessaire = request.POST.getlist('materiel[]')
        creneau_horaire = request.POST.getlist('creneau[]')
        infos_supplementaires = request.POST.getlist('infos[]')

        for i in range(len(jour)):
            emploi_temps = EmploiTemps(
                specialite=specialite,
                niveau_etude=niveau_etude,
                semaine=semaine,
                jour=jour[i],
                intitule_cours=intitule_cours[i],
                nom_professeur=nom_professeur[i],
                materiel_necessaire=materiel_necessaire[i],
                creneau_horaire=creneau_horaire[i],
                infos_supplementaires=infos_supplementaires[i]
            )
            emploi_temps.save()

    return render(request, 'creation_edt.html')
