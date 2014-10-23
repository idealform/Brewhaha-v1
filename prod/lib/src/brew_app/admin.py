from django.contrib import admin
from brew_app.models import BrewLog, Recipe, GrainList, GrainIngredient, HopList, HopIngredient, YeastList, YeastIngredient, BrewAction


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_filter = ['recipe_name',]
    list_display = ['recipe_name', 'recipe_type',]

admin.site.register(BrewLog)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(GrainList)
admin.site.register(GrainIngredient)
admin.site.register(HopList)
admin.site.register(HopIngredient)
admin.site.register(YeastList)
admin.site.register(YeastIngredient)
admin.site.register(BrewAction)