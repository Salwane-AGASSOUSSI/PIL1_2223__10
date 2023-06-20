from django.shortcuts import render
from .models import EmploiTemps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage

def emploi_temps_view(request):
    emplois_temps = EmploiTemps.objects.all()
    return render(request, 'emploi_temps/emploi_temps.html', {'emplois_temps': emplois_temps})

def modify_timetable(request):
    if request.method == 'POST':
        # Récupérer les informations de modification depuis la requête POST
        new_timetable_data = request.POST.get('new_timetable_data')
        student_email = request.POST.get('student_email')

        # Rechercher l'emploi du temps de l'étudiant
        timetable = Timetable.objects.get(student_email=student_email)

        # Mettre à jour les données de l'emploi du temps
        timetable.data = new_timetable_data
        timetable.save()

        # Envoyer une notification par courrier électronique
        subject = "Changement d'horaire"
        message = "Votre emploi du temps a été modifié. Veuillez vérifier les nouvelles informations."
        email = EmailMessage(subject, message, to=[student_email])
        email.send()

        # Afficher un message de succès
        messages.success(request, "L'emploi du temps a été modifié avec succès.")
        return redirect('success')  # Rediriger vers une page de succès
    else:
        # Gérer les requêtes GET ou autres méthodes non autorisées
        return redirect('error')  # Rediriger vers une page d'erreur

