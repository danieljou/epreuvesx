from django.shortcuts import render,redirect
from users.models import User
from .forms import *
from django.contrib import messages
from random import randint
from django.contrib.auth.decorators import login_required
from users.decorators import *

from django.template.loader import get_template

from io   import BytesIO

from xhtml2pdf import pisa 

from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def redirect_user(request):

    if not request.user.is_authenticated:
        return redirect('login')
    else:
        if request.user.is_admin:
            return redirect('admin_home')
        else:
            return redirect('prof_home')


def prof_home(request):
    context = {}
    context['all_exercice'] = Exercice.objects.filter(Auteur__id = request.user.id).count()
    context['exercice_count'] = Exercice.objects.all().count()
    context['epreuve_count'] = Epreuve.objects.all().count()
    return render(request, 'prof_home.html', context)

@login_required
@is_admin_required
def admin_home(request):
    context = {}
    context['account_count'] = User.objects.exclude(pk = request.user.id).count()
    context['account_enseigant'] = User.objects.exclude(pk = request.user.id).filter(is_professeur = True).count()
    context['matiere_count'] = Matiere.objects.all().count()
    context['exercice_count'] = Exercice.objects.all().count()
    context['epreuve_count'] = Epreuve.objects.all().count()

    return render(request, 'admin/admin_home.html', context)


#  gestion des exercices 

def exercices_homes(request):
    context = {}
    context['all_exercice'] = Exercice.objects.all()

    if request.user.is_admin == False:
        context['all_exercice'] = Exercice.objects.filter(Auteur__id = request.user.id)
    return render(request, 'exercices/exercice_home.html', context)

def add_exercice(request):

    context = {}
    context['card_color'] = 'bg-success'
    context['form_card_title'] = 'Ajouter un Exercice'
    context['submit_text'] = 'Ajouter'
    context['form_title'] = 'Exercices | Ajouter un exercice'
    form = ExerciceForm(request.POST or None)
    context['form'] = form
    if request.method == 'POST':
        if(form.is_valid()):
            exercice  = form.save(commit = False)
            exercice.Auteur = request.user
            exercice.save()
            return redirect('exercices_homes')

    return render(request, 'form_page.html', context)


def update_exercice(request, exercice_id):

    context = {}
    context['card_color'] = 'bg-primary'
    context['form_card_title'] = 'Modifier l \'exercice '
    context['submit_text'] = 'Modifier'
    context['form_title'] = 'Exercices | Modifier'

   
    
    exercice = Exercice.objects.get(pk = exercice_id)
    form = ExerciceForm(request.POST or None, instance = exercice)
    context['form'] = form
    if request.method == 'POST':
        if(form.is_valid()):
            form.save()
            return redirect('exercices_homes')

    return render(request, 'form_page.html', context)


def delete_exercice(request, exercice_id):
    exercice = Exercice.objects.get(pk = exercice_id)
    exercice.delete()

    return redirect('exercices_homes')




# gestion des matieres


def matieres_homes(request):
    context = {}
    context['all_matiere'] = Matiere.objects.all()
    return render(request, 'matieres/matiere_home.html', context)

def add_matiere(request):

    context = {}
    context['card_color'] = 'bg-primary'
    context['form_card_title'] = 'Ajouter un matiere'
    context['submit_text'] = 'Ajouter'
    context['form_title'] = 'matieres | Ajouter un matiere'
    form = MatiereForm(request.POST or None)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('matieres_homes')
    return render(request, 'form_page.html', context)


def update_matiere(request, matiere_id):

    context = {}
    context['card_color'] = 'bg-primary'
    context['form_card_title'] = 'Modifier l \'matiere '
    context['submit_text'] = 'Modifier'
    context['form_title'] = 'matieres | Modifier'
    matiere = Matiere.objects.get(pk = matiere_id)
    form = MatiereForm(request.POST or None, instance = matiere)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('matieres_homes')
    return render(request, 'form_page.html', context)
    return render(request, 'form_page.html', context)


def delete_matiere(request, matiere_id):
    matiere = Matiere.objects.get(pk = matiere_id)
    matiere.delete()    
    return redirect('matieres_homes')

#  gestion des epreuves


def epreuves_homes(request):
    context = {}
    context['all_epreuve'] = Epreuve.objects.all()

    return render(request, 'epreuves/epreuves_home.html', context)

def add_epreuve(request):

    context = {}
    context['card_color'] = 'bg-primary'
    context['form_card_title'] = 'Ajouter un epreuve'
    context['submit_text'] = 'Ajouter'
    context['form_title'] = 'epreuves | Ajouter un epreuve'
    form = EpreuveForm(request.POST or None)
    context['form'] = form
    if(request.method == 'POST'):
        if form.is_valid():

            matiere = form.cleaned_data['matiere']
            nb_exerce_form = form.cleaned_data['Nombre_exerce']
    
            nb_exercie = Exercice.objects.filter(matiere = matiere).count()

            if nb_exerce_form > nb_exercie:
                messages.warning(request, "Le nombre d'exercie que vous avez choisi est superieur au nombre d'exercie disponible pour cette matiere  veulleiz choisir un nombre d'epreuve <= {}".format(nb_exercie))
            else:
                exercice_list = []
                exercie_choices = Exercice.objects.filter(matiere = matiere)
                exercice_choices_ok = []
                for item in exercie_choices:
                    exercice_choices_ok.append(item.id)
                for i in range(0,nb_exerce_form):
                    index = randint(0,len(exercice_choices_ok))
                    exercice_list.append(exercice_choices_ok[index - 1])
                    exercice_choices_ok.remove(exercice_choices_ok[index - 1])
                    
                epreuve = form.save()
                for i in range(0, len(exercice_list)):
                    item = exercice_list [i]
                    
                    exo = Exercice.objects.get(pk = item)
                    print(exo.Titre)
                    epreuve.exercices.add(exo)
                epreuve.save()
                messages.success(request, ' les exercies on été bien ajouté et l\"epreuve a été crée' )
                return redirect('epreuves_homes')
            pass

    return render(request, 'form_page.html', context)


def update_epreuve(request, epreuve_id):

    context = {}
    context['card_color'] = 'bg-primary'
    context['form_card_title'] = 'Modifier l \'epreuve '
    context['submit_text'] = 'Modifier'
    context['form_title'] = 'epreuves | Modifier'

    return render(request, 'form_page.html', context)

def details_epreuve(request, epreuve_id):
    context = {}

    epreuve = Epreuve.objects.get(pk = epreuve_id)
    exercices = epreuve.exercices.all()

    context['epreuve'] = epreuve
    context['exercices'] = exercices

    return render(request,'epreuves/epreuve_details.html', context)

def delete_epreuve(request, epreuve_id):
    epreuve = Epreuve.objects.get(pk = epreuve_id)
    epreuve.delete()
    return redirect('epreuves_homes')



def douwnload_epreuve_pdf(request, epreuve_id):
    template = get_template('pdf2.html')

    context = {}

    epreuve = Epreuve.objects.get(pk = epreuve_id)
    exercices = epreuve.exercices.all()

    context['epreuve'] = epreuve
    context['exercices'] = exercices
    
    html = template.render(context)
    options = {
        'page-size': 'Letter',
        'encoding':  'UTF-8',
        
    }

    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')),result)

    
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type = 'application/pdf')
    return None

