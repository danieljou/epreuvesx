from django import forms
from .models import * 


class ExerciceForm(forms.ModelForm):
    
    class Meta:
        model = Exercice
        exclude = ('Auteur',)

        widgets = {
            'matiere' : forms.Select(
                attrs = {
                    'class' : 'form-select'
                }
            ) 
        }

class MatiereForm(forms.ModelForm):
    
    class Meta:
        model = Matiere
        fields = '__all__'

class EpreuveForm(forms.ModelForm):
    
    class Meta:
        model = Epreuve
        exclude = ('exercices',)
        widgets = {
            'matiere' : forms.Select(
                attrs = {
                    'class' : 'form-select'
                }
            ) 
        }
