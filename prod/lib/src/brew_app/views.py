from django.db import models
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, render_to_response, RequestContext
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from brew_app.models import Recipe, BrewLog, GrainIngredient, GrainList, HopList, GrainList, YeastList

from brew_app.serializers import BrewLogSerializer, RecipeSerializer, GrainListSerializer, HopListSerializer, YeastListSerializer
from rest_framework import viewsets


############################ Brewlog ############################

class BrewlogListView(ListView):
    model = BrewLog
    
class BrewlogDetailView(DetailView):
    model = BrewLog
 
class BrewlogCreateView(SuccessMessageMixin, CreateView):
    model = BrewLog
    success_message = "Brewlog was created."
    success_url = "../"


############################ Recipe ############################

class RecipeListView(ListView):
    model = Recipe
    
class RecipeDetailView(DetailView):
    model = Recipe
    
class RecipeCreateView(SuccessMessageMixin, CreateView):
    model = Recipe
    success_message = "Recipe was created."
    
    
class RecipeUpdateView(SuccessMessageMixin, UpdateView):
    model = Recipe
    success_message = "Recipe was updated."
    succes_url = "../../"
    


############################ View Sets ############################
class BrewLogViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BrewLog.objects.all()
    serializer_class = BrewLogSerializer

class RecipeViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class GrainListViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GrainList.objects.all()
    serializer_class = GrainListSerializer
    
class HopListViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = HopList.objects.all()
    serializer_class = HopListSerializer
    
class YeastListViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = YeastList.objects.all()
    serializer_class = YeastListSerializer




