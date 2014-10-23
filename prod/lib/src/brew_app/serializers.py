from rest_framework import serializers
from brew_app.models import BrewLog, Recipe, GrainIngredient, GrainList, HopIngredient, HopList, YeastIngredient, YeastList, BrewAction



############################ Brewlog Seralizer ############################

class BrewActionSeralizer(serializers.ModelSerializer):
    class Meta:
        model = BrewAction
        fields = ('brewaction_time','brewaction_step', 'brewaction_comment')

class BrewLogSerializer(serializers.ModelSerializer):
    
    brew_action = BrewActionSeralizer(many=True)
    brew_rating = serializers.ChoiceField(choices=(), blank_display_value=None)
    
    class Meta:
        model = BrewLog
        fields = ('brew_name', 'brew_rating', 'brew_status', 'brew_start_time', 'brew_end_time', 'brew_action')


############################ Recipe Seralizer ############################

class GrainIngredientSeralizer(serializers.ModelSerializer):
    
    selected_grain = serializers.CharField(max_length=60)
    
    class Meta:
        model = GrainIngredient
        fields = ('selected_grain','amountof_grain')

class HopIngredientSeralizer(serializers.ModelSerializer):
    
    selected_hops = serializers.CharField(max_length=60)
    
    class Meta:
        model = HopIngredient
        fields = ('selected_hops' ,'amountof_hops')

class YeastIngredientSeralizer(serializers.ModelSerializer):
    
    selected_yeast = serializers.CharField(max_length=60)
    
    class Meta:
        model = YeastIngredient
        fields = ('selected_yeast' ,'amountof_yeast')


class RecipeSerializer(serializers.ModelSerializer):
    
    recipe_grain = GrainIngredientSeralizer(many=True)
    recipe_hop = HopIngredientSeralizer(many=True)
    recipe_yeast = YeastIngredientSeralizer(many=True)
    
    class Meta:
        model = Recipe
        fields = ('recipe_name', 'recipe_type', 'recipe_grain', 'recipe_hop', 'recipe_yeast')
        depth = 1


############################ List Seralizers ############################

class GrainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrainList

class HopListSerializer(serializers.ModelSerializer):
    class Meta:
        model = HopList

class YeastListSerializer(serializers.ModelSerializer):
    class Meta:
        model = YeastList



