from django.shortcuts import render, redirect,get_object_or_404
from urllib.parse import urlencode


from django.contrib import messages

from django.contrib.auth.decorators import login_required,user_passes_test

from .import forms

def is_superuser(user):
    return user.is_superuser



from .models import EmploiDuTemps
@user_passes_test(is_superuser)
def creer(request):
    emplois = None
    message = ""
    if request.method == 'POST':
        
        
        
        
          
            
        emploi_data = {
            
        'l_7_8':request.POST.get('l_7_8'),
        'l_8_9':request.POST.get('l_8_9'),
        'l_9_10':request.POST.get('l_9_10'),
        'l_10_11':request.POST.get('l_10_11'),
        'l_11_12':request.POST.get('l_11_12'),
        'l_12_13':request.POST.get('l_12_13'),
        'l_13_14':request.POST.get('l_13_14'),
        'l_14_15':request.POST.get('l_14_15'),
        'l_15_16':request.POST.get('l_15_16'),
        'l_16_17':request.POST.get('l_16_17'),
        'l_17_18':request.POST.get('l_17_18'),
        'l_18_19':request.POST.get('l_18_19'),
        
            
        
                
        'm_7_8':request.POST.get('m_7_8'),
        'm_8_9':request.POST.get('m_8_9'),
        'm_9_10':request.POST.get('m_9_10'),
        'm_10_11':request.POST.get('m_10_11'),
        'm_11_12':request.POST.get('m_11_12'),
        'm_12_13':request.POST.get('m_12_13'),
        'm_13_14':request.POST.get('m_13_14'),
        'm_14_15':request.POST.get('m_14_15'),
        'm_15_16':request.POST.get('m_15_16'),
        'm_16_17':request.POST.get('m_16_17'),
        'm_17_18':request.POST.get('m_17_18'),
        'm_18_19':request.POST.get('m_18_19'),
      
            
       
               
        'me_7_8':request.POST.get('me_7_8'),
        'me_8_9':request.POST.get('me_8_9'),
        'me_9_10':request.POST.get('me_9_10'),
        'me_10_11':request.POST.get('me_10_11'),
        'me_11_12':request.POST.get('me_11_12'),
        'me_12_13':request.POST.get('me_12_13'),
        'me_13_14':request.POST.get('me_13_14'),
        'me_14_15':request.POST.get('me_14_15'),
        'me_15_16':request.POST.get('me_15_16'),
        'me_16_17':request.POST.get('me_16_17'),
        'me_17_18':request.POST.get('me_17_18'),
        'me_18_19':request.POST.get('me_18_19'),
     
            
    
       
        'j_7_8':request.POST.get('j_7_8'),
        'j_8_9':request.POST.get('j_8_9'),
        'j_9_10':request.POST.get('j_9_10'),
        'j_10_11':request.POST.get('j_10_11'),
        'j_11_12':request.POST.get('j_11_12'),
        'j_12_13':request.POST.get('j_12_13'),
        'j_13_14':request.POST.get('j_13_14'),
        'j_14_15':request.POST.get('j_14_15'),
        'j_15_16':request.POST.get('j_15_16'),
        'j_16_17':request.POST.get('j_16_17'),
        'j_17_18':request.POST.get('j_17_18'),
        'j_18_19':request.POST.get('j_18_19'),
   
     
        'v_7_8':request.POST.get('v_7_8'),
        'v_8_9':request.POST.get('v_8_9'),
        'v_9_10':request.POST.get('v_9_10'),
        'v_10_11':request.POST.get('v_10_11'),
        'v_11_12':request.POST.get('v_11_12'),
        'v_12_13':request.POST.get('v_12_13'),
        'v_13_14':request.POST.get('v_13_14'),
        'v_14_15':request.POST.get('v_14_15'),
        'v_15_16':request.POST.get('v_15_16'),
        'v_16_17':request.POST.get('v_16_17'),
        'v_17_18':request.POST.get('v_17_18'),
        'v_18_19':request.POST.get('v_18_19'),
   
                
        's_7_8':request.POST.get('s_7_8'),
        's_8_9':request.POST.get('s_8_9'),
        's_9_10':request.POST.get('s_9_10'),
        's_10_11':request.POST.get('s_10_11'),
        's_11_12':request.POST.get('s_11_12'),
        's_12_13':request.POST.get('s_12_13'),
        's_13_14':request.POST.get('s_13_14'),
        's_14_15':request.POST.get('s_14_15'),
        's_15_16':request.POST.get('s_15_16'),
        's_16_17':request.POST.get('s_16_17'),
        's_17_18':request.POST.get('s_17_18'),
        's_18_19':request.POST.get('s_18_19'),
        'filiere':request.POST.get('filiere'),
        'description':request.POST.get('description'),
        
     
        }
        if all( value == '' or value is None for value in emploi_data.values()):
            message = "Veuillez entrer au moins un cours s'il vous plait"
            return render(request,'timetable/creer.html', {'message':message} )
        else:
            query_params = urlencode(emploi_data)
            redirect_url = f"/confirmation/?{query_params}"
            return redirect(redirect_url)
        
    
        
    
    
    return render(request, 'timetable/creer.html')
@user_passes_test(is_superuser)
def confirmation(request):
    emploi_data = request.GET.dict()
    emplois = EmploiDuTemps(emploi_data = emploi_data)
        
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == "Valider":
            emplois.publish()
            emplois.save()
            return redirect('consultation')
        elif action == "Annuler":
            return redirect('creer')
    return render(request, 'timetable/confirmation.html', {'emplois':emplois})
@login_required
def consultation(request):
    emplois = EmploiDuTemps.objects.all()
    filieres = set()

    for emploi in emplois:
        filiere = emploi.emploi_data.get('filiere')
        if filiere:
            filieres.add(filiere.lower())

    filiere = request.POST.get('filiere')  # Récupère la filière sélectionnée dans le formulaire
    if filiere:
        emplois = EmploiDuTemps.objects.filter(emploi_data__filiere__iexact=filiere)
    else:
        emplois = EmploiDuTemps.objects.all()

    return render(request, 'timetable/consultation.html', {'emplois': emplois, 'filieres': filieres})



@user_passes_test(is_superuser)
def modification(request,pk):
    emploi = get_object_or_404(EmploiDuTemps, pk=pk)
    
    emploi_data = emploi.emploi_data

    if request.method == 'POST':
        emploi_data = {
            
        'l_7_8':request.POST.get('l_7_8'),
        'l_8_9':request.POST.get('l_8_9'),
        'l_9_10':request.POST.get('l_9_10'),
        'l_10_11':request.POST.get('l_10_11'),
        'l_11_12':request.POST.get('l_11_12'),
        'l_12_13':request.POST.get('l_12_13'),
        'l_13_14':request.POST.get('l_13_14'),
        'l_14_15':request.POST.get('l_14_15'),
        'l_15_16':request.POST.get('l_15_16'),
        'l_16_17':request.POST.get('l_16_17'),
        'l_17_18':request.POST.get('l_17_18'),
        'l_18_19':request.POST.get('l_18_19'),
        
            
        
                
        'm_7_8':request.POST.get('m_7_8'),
        'm_8_9':request.POST.get('m_8_9'),
        'm_9_10':request.POST.get('m_9_10'),
        'm_10_11':request.POST.get('m_10_11'),
        'm_11_12':request.POST.get('m_11_12'),
        'm_12_13':request.POST.get('m_12_13'),
        'm_13_14':request.POST.get('m_13_14'),
        'm_14_15':request.POST.get('m_14_15'),
        'm_15_16':request.POST.get('m_15_16'),
        'm_16_17':request.POST.get('m_16_17'),
        'm_17_18':request.POST.get('m_17_18'),
        'm_18_19':request.POST.get('m_18_19'),
      
            
       
               
        'me_7_8':request.POST.get('me_7_8'),
        'me_8_9':request.POST.get('me_8_9'),
        'me_9_10':request.POST.get('me_9_10'),
        'me_10_11':request.POST.get('me_10_11'),
        'me_11_12':request.POST.get('me_11_12'),
        'me_12_13':request.POST.get('me_12_13'),
        'me_13_14':request.POST.get('me_13_14'),
        'me_14_15':request.POST.get('me_14_15'),
        'me_15_16':request.POST.get('me_15_16'),
        'me_16_17':request.POST.get('me_16_17'),
        'me_17_18':request.POST.get('me_17_18'),
        'me_18_19':request.POST.get('me_18_19'),
     
            
    
       
        'j_7_8':request.POST.get('j_7_8'),
        'j_8_9':request.POST.get('j_8_9'),
        'j_9_10':request.POST.get('j_9_10'),
        'j_10_11':request.POST.get('j_10_11'),
        'j_11_12':request.POST.get('j_11_12'),
        'j_12_13':request.POST.get('j_12_13'),
        'j_13_14':request.POST.get('j_13_14'),
        'j_14_15':request.POST.get('j_14_15'),
        'j_15_16':request.POST.get('j_15_16'),
        'j_16_17':request.POST.get('j_16_17'),
        'j_17_18':request.POST.get('j_17_18'),
        'j_18_19':request.POST.get('j_18_19'),
   
     
        'v_7_8':request.POST.get('v_7_8'),
        'v_8_9':request.POST.get('v_8_9'),
        'v_9_10':request.POST.get('v_9_10'),
        'v_10_11':request.POST.get('v_10_11'),
        'v_11_12':request.POST.get('v_11_12'),
        'v_12_13':request.POST.get('v_12_13'),
        'v_13_14':request.POST.get('v_13_14'),
        'v_14_15':request.POST.get('v_14_15'),
        'v_15_16':request.POST.get('v_15_16'),
        'v_16_17':request.POST.get('v_16_17'),
        'v_17_18':request.POST.get('v_17_18'),
        'v_18_19':request.POST.get('v_18_19'),
   
                
        's_7_8':request.POST.get('s_7_8'),
        's_8_9':request.POST.get('s_8_9'),
        's_9_10':request.POST.get('s_9_10'),
        's_10_11':request.POST.get('s_10_11'),
        's_11_12':request.POST.get('s_11_12'),
        's_12_13':request.POST.get('s_12_13'),
        's_13_14':request.POST.get('s_13_14'),
        's_14_15':request.POST.get('s_14_15'),
        's_15_16':request.POST.get('s_15_16'),
        's_16_17':request.POST.get('s_16_17'),
        's_17_18':request.POST.get('s_17_18'),
        's_18_19':request.POST.get('s_18_19'),
        'filiere':request.POST.get('filiere'),
        'description':request.POST.get('description'),
        
     
        }
        

       
        # Enregistrer les modifications dans la base de données
        
        emploi.emploi_data = emploi_data

        emploi.save()
        return redirect('consultation')
        
       
        # Rediriger vers une autre vue ou effectuer d'autres opérations

    context = {'emploi_data': emploi_data,'pk':pk}
    return render(request, 'timetable/modification.html', context)







    
    
    
