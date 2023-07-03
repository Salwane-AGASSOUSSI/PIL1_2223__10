from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required,user_passes_test
from .import forms
from django.contrib.auth import get_user_model
from django.contrib import messages
from .models import Account_Request

 #Create your views here.

def is_superuser(user):
    return user.is_superuser

def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message =f'Bonjour {user.username} ! Vous etes connecté'
                return redirect('consultation')
                
            else:
                message = f'Identifiants Invalides'
    return render(request,'authentification/connexion.html', {'form':form}) 

def logout_page(request):
    logout(request)
    return redirect('login')
def succes(request):
    return render(request, 'authentification/success.html',{})
def signup_page(request):
    form = forms.SignupForm()
    if request.method == "POST":
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            num_id = form.cleaned_data['num_id']
            password = form.cleaned_data['password']
            c_password = form.cleaned_data['c_password']
            if password == c_password:
                account_request = Account_Request(username=username,email=email, num_id=num_id, password=password)
                account_request.save()
            else:
                return messages.error("vous n'avez pas taper les memes mot de passes")
            
            
            
            return redirect('success')
    return render(request,'authentification/inscription.html',{'form':form})

def account_requests(request):
    account_requests = Account_Request.objects.filter(is_approved=False)
    return render(request, 'authentification/account_request_list.html', {'account_requests':account_requests})

def approve_account_request(request,pk):
    account_request = Account_Request.objects.get(pk=pk)
    username = account_request.username
    email = account_request.email
    num_id = account_request.num_id
    password = account_request.password
    user = User.objects.create_user(username=username, email=email, num_id=num_id, password=password)
    
    user.save()
    account_request.is_approved=True
    account_request.save()

    # Envoi de l'e-mail au demandeur
    subject = 'Votre demande à été approuvée'
    message = f'Bonjour {account_request.username},\n\nVotre demande de compte a été approuvée. Vous pouvez maintenant vous connecter à notre site avec le mot de passe que vous avez fourni lors de la demande de compte.\n\nCordialement,\nL\'équipe du site'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [account_request.email]
    send_mail(subject,message,from_email,recipient_list)
    messages.success(request, 'Demande de compte approuvée. Un e-mail a été envoyé au demandeur.')
    return redirect('account_requests')

def refus(request,pk):
    
    try:
        account_request = Account_Request.objects.get(pk=pk)
    except Account_Request.DoesNotExist:
        # Gérer le cas où l'objet Account_Request avec le pk spécifié n'existe pas
        messages.error(request, "La demande de compte n'existe pas.")
        return redirect('account_requests')  # Remplacez 'account_requests' par le nom de l'URL pour afficher la liste des demandes de compte

    subject = 'Votre demande à été rejeter'
    message = f"Bonjour {account_request.username},\n\nVotre demande de compte a été rejeter. Vous pouvez toujours retenter et vous rapprochez de l'ecole si vous pensez que c'est une erreur .\n\nCordialement,\nL\'équipe du site"
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [account_request.email]
    send_mail(subject,message,from_email,recipient_list)
    messages.success(request, 'Demande de compte rejeté. Un e-mail a été envoyé au demandeur.')
    
    account_request.delete()
    return redirect('account_requests')



@user_passes_test(is_superuser)
def add_superuser(request):
    form = forms.SignuppForm()
    if request.method == 'POST':
        form = forms.SignuppForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_superuser = True
            user.save()
            messages.success(request, 'Superutilisateur ajouté avec succès.')
            return redirect('gestions')  # Remplacez 'success' par le nom de votre page de succès
    else:
        form = forms.SignuppForm()   
    return render(request, 'authentification/add_superuser.html',{'form':form})  
@user_passes_test(is_superuser)
def delete_superuser(request, pk):
    
    user = get_object_or_404(User, pk=pk)
    
    if user.is_superuser and user != request.user:
        user.delete()
        messages.success(request, 'Superutilisateur supprimé avec succès.')
    else:
        messages.error(request, "Vous ne pouvez pas supprimer cet utilisateur.")
    
    return redirect('gestions')  


User = get_user_model()
@user_passes_test(is_superuser)
def superuser_list(request):
    superusers = User.objects.filter(is_superuser=True).exclude(id=request.user.id)
    return render(request, 'authentification/gestion_user.html', {'superusers': superusers})


