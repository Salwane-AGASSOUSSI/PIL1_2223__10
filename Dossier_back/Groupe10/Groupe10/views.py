from .models import EmploiTemps
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

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

def generer_emploi_du_temps_pdf(request):
    # Récupérer les données des emplois du temps
    emplois_du_temps = EmploiDuTemps.objects.all()  # Exemple de récupération des emplois du temps depuis le modèle

    # Créer un objet canvas pour générer le PDF
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Logique de génération du contenu du PDF
    y = 700  # Position verticale pour commencer à ajouter les informations
    for emploi_du_temps in emplois_du_temps:
        # Ajouter les informations des emplois du temps au PDF
        p.drawString(50, y, emploi_du_temps.nom)
        # ...

        y -= 20  # Déplacer vers le haut pour ajouter la prochaine information

    # Enregistrer le contenu du PDF
    p.showPage()
    p.save()

    # Récupérer le contenu du buffer
    pdf_content = buffer.getvalue()
    buffer.close()

    # Enregistrer le fichier PDF sur le disque ou dans le modèle approprié
    with open('chemin/vers/fichier.pdf', 'wb') as f:
        f.write(pdf_content)

    # Ou enregistrer le fichier PDF dans un champ de fichier d'un modèle approprié
    emploi_du_temps = EmploiDuTemps.objects.get(id=1)
    emploi_du_temps.pdf_file.save('emploi_du_temps.pdf', ContentFile(pdf_content), save=True)

    # Retourner la réponse HTTP appropriée
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="emploi_du_temps.pdf"'
    response.write(pdf_content)
    return response


