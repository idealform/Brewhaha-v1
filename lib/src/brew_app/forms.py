from django import forms
from django.forms.formsets import formset_factory
from brew_app.models import Recipe, BrewLog

############################ Forms ############################

############################ Brewlog #############
class BrewlogForm(forms.ModelForm):
    class Meta:
        model = BrewLog

############################ Recipe #############
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
