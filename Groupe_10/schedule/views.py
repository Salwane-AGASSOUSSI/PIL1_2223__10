from Groupe_10 import settings
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.utils.encoding import force_bytes,force_text
from django.template.loader import render_to_string
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from  django.core.mail import send_mail,EmailMessage
from .models import etudiant,key
import random


# Create your views here.
def home(request):
    return render(request,'schedule/acceuil_etudiant_page.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        password = request.POST['password']
        Repassword = request.POST['repassword']
        if User.objects.filter(username=username):
            messages.error(request,'Ce nom est déja utilisé')
            return redirect('register')
        if User.objects.filter(email=email):
            messages.error(request,'Cet email est déja utilisé')
            return redirect(register)
        if not username.isalnum():
            messages.error(request,'le nom doit être alphanumerique')
            return redirect(register)
        if password == Repassword:
            # Créer un nouvel utilisateur et définir les champs
            my_user = User.objects.create(
                username=username,
                email=email
            )
            my_user.first_name = nom
            my_user.last_name = prenom

            # Utiliser set_password() pour stocker le mot de passe sécurisé
            my_user.set_password(password)

            # Enregistrer l'utilisateur dans la base de données
            my_user.save()

            messages.success(request, 'Inscription réussie')
            return redirect('info')
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas')

    return render(request, 'schedule/form_Inscription_Stud.html')

def info(request):
    if request.method=="POST":
        matricule=request.POST['matricule']
        nom_prenoms=request.POST['nom_prenoms']
        sexe=request.POST['sexe']
        Telephone=request.POST['Telephone']
        mon_user = etudiant.objects.create(
           matricule=matricule,
           nom_prenoms=nom_prenoms ,
           sexe=sexe,
           Telephone=Telephone,
        )
        mon_user.save()
        messages.success(request,'Inscription réussi')
        
        return redirect('login')


    return render(request,'schedule/info.html')


def logIn(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            prenom=user.last_name
            return render(request,'schedule/acceuil_etudiant_page.html', {'prenom':prenom})
        else:
            messages.error(request,'Echec de connxion')
            return redirect('login')
    return render(request,'schedule/form_Login_Stud.html')

    

def logOut(request):
    logout(request)
    messages.success(request,'Déconnecté')
    return redirect ('acceuil')

def send_email(request):
    if request.method == "POST":
        email = request.POST['email']
        if not User.objects.filter(email=email).exists():
            messages.error(request, "Cet email n'est pas répertorié")
            return redirect('email')
        subject = "Bienvenue sur le gestionnaire d'emploi du temps"
        code = str(random.randint(1000, 9999))
        mon_code = key.objects.create(cle=code)
        mon_code.save()
        from_email = settings.EMAIL_HOST_USER
        to_list = [email]
        send_mail(subject, code, from_email, to_list, fail_silently=False)
        messages.success(request, 'Email envoyé avec succès')
        return redirect('code')
    return render(request, 'schedule/email.html')


def code(request):
    if request.method == "POST":
        code = request.POST["code"]
        if key.objects.filter(cle=code).exists():
            return redirect('change_password')
    return render(request, 'schedule/code.html')



def change_password(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        
        if password == repassword:
            try:
                # Récupérer l'utilisateur de la base de données
                user = User.objects.get(username=username)
                
                # Utiliser set_password() pour définir le nouveau mot de passe
                user.set_password(password)
                
                # Enregistrer les modifications dans la base de données
                user.save()
                
                messages.success(request, 'Mot de passe modifié avec succès')
                return redirect('login')
            except User.DoesNotExist:
                messages.error(request, "Cet utilisateur n'existe pas")
        else:
            messages.error(request, 'Les mots de passe ne correspondent pas')

    return render(request, 'schedule/change_password.html')

