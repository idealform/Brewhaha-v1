from django.db import models
from django.utils.encoding import smart_unicode
from django.core.urlresolvers import reverse


    
# Hops Country
US = 'US'
UK = 'UK'
GERMANY = 'Germany'
CANADA = 'Canada'
POLAND = 'Poland'
NEWZEALAND = 'New Zealand'
AUSTRALIA = 'Australia'
CZECREP = 'Czech Republic'
FRANCE = 'France'
SLOVENIA = 'Slovenia'

#Brew Rating
LOW = 'Low'
MEDIUM = 'Medium'
HIGH = 'High'


# Brew Action Steps
NOTSTARTED = "Not Started"
MASHSTART = 'Mash Started'
MASHEND = 'Mash Ended'
SPARGESTART = 'Sparge Started'
SPARGEEND = 'Sparge Ended'
BOILSTART = 'Boil Started'
BOILEND = 'Boil Ended'
FERMENTSTART = 'Fermentation Started'
FERMENTEND = 'Fermentation Ended'
BOTTLESTART = 'Bottled'
BOTTLEEND = 'Completed'

# Recipe Type
ALLGRAIN = 'All Grain'
EXTRACT = 'Extract'
    
    
# Recipe Type
AROMA = 'Aroma'
BITTERING = 'Bittering'

# Yeast Type
ALE = 'Ale'
CHAMPAGNE = 'Champagne'
LAGER = 'Lager'
WHEAT = 'Wheat'
WINE = 'Wine'

# Yeast Form
DRY = 'Dry'
LIQUID = 'Liquid'


############################ Brewlog Models ############################ 

class BrewLog(models.Model):
    brew_name = models.CharField(max_length=80, null=True, blank=False)
    brew_start_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    brew_end_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    # Brew Rating
    brew_rating = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    
    brew_rating = models.CharField(max_length=6,
                                      choices=brew_rating,
                                      default=LOW)
    
    brew_status = (
        (NOTSTARTED, 'Not Started'),
        (MASHSTART, 'Mash Started'),
        (MASHEND, 'Mash Ended'),
        (SPARGESTART, 'Sparge Started'),
        (SPARGEEND, 'Sparge Ended'),
        (BOILSTART, 'Boil Started'),
        (BOILEND, 'Boil Ended'),
        (FERMENTSTART, 'Fermentation Started'),
        (FERMENTEND, 'Fermentation Ended'),
        (BOTTLESTART, 'Bottled'),
        (BOTTLEEND, 'Completed'),
    )
    
    brew_status = models.CharField(max_length=20,
                                      choices=brew_status,
                                      default=NOTSTARTED)
    
    brew_action = models.ManyToManyField('BrewAction', null=True)
    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})
    
    def __unicode__(self):
        return smart_unicode(self.brew_name)


class BrewAction(models.Model):
    brewaction_time = models.DateTimeField(auto_now_add=True, auto_now=False)
    
    
    brew_steps = (
        (NOTSTARTED, 'Not Started'),
        (MASHSTART, 'Mash Started'),
        (MASHEND, 'Mash Ended'),
        (SPARGESTART, 'Sparge Started'),
        (SPARGEEND, 'Sparge Ended'),
        (BOILSTART, 'Boil Started'),
        (BOILEND, 'Boil Ended'),
        (FERMENTSTART, 'Fermentation Started'),
        (FERMENTEND, 'Fermentation Ended'),
        (BOTTLESTART, 'Bottled'),
        (BOTTLEEND, 'Completed'),
    )
    
    brewaction_step = models.CharField(max_length=20,
                                      choices=brew_steps,
                                      default=NOTSTARTED)
    
    brewaction_comment = models.CharField(max_length=80, null=True, blank=False, unique=False)
    
    def __unicode__(self):
        return smart_unicode(self.brewaction_step)
    

############################ Recipe Models ############################ 

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=80, null=True, blank=False, unique=True)

    recipe_type = (
        (ALLGRAIN, 'All Grain'),
        (EXTRACT, 'Extract'),
    )
    
    recipe_type = models.CharField(max_length=9,
                                      choices=recipe_type,
                                      default=ALLGRAIN)
    
    recipe_grain = models.ManyToManyField('GrainIngredient', null=True)
    recipe_hop = models.ManyToManyField('HopIngredient', null=True)
    recipe_yeast = models.ManyToManyField('YeastIngredient', null=True)

    
    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return smart_unicode(self.recipe_name)
    


############################ Ingredients Models ############################

class GrainIngredient(models.Model):
    selected_grain = models.ForeignKey('GrainList', null=True)
    amountof_grain = models.IntegerField(null=True)
    
    def __unicode__(self):
        return smart_unicode(self.selected_grain)
    
class HopIngredient(models.Model):
    selected_hops = models.ForeignKey('HopList', null=True)
    amountof_hops = models.IntegerField(null=True)
    
    def __unicode__(self):
        return smart_unicode(self.selected_hops)
    
class YeastIngredient(models.Model):
    selected_yeast = models.ForeignKey('YeastList', null=True)
    amountof_yeast = models.IntegerField(null=True)
    
    def __unicode__(self):
        return smart_unicode(self.selected_yeast)




############################ Ingredient List Models ############################

############################ Grains #############
class GrainList (models.Model):
    grain_name = models.CharField(max_length=60, null=True, blank=False, unique=True)
    grain_gravity = models.IntegerField(null=True, )
    grain_description = models.CharField(max_length=80, null=True, blank=False)
    
    grainlist_type = (
        (ALLGRAIN, 'All Grain'),
        (EXTRACT, 'Extract'),
    )
    
    grainlist_type = models.CharField(max_length=9,
                                      choices=grainlist_type,
                                      default=ALLGRAIN)
    
    def __unicode__(self):
        return smart_unicode(self.grain_name)

############################ Hops #############
class HopList (models.Model):
    hop_name = models.CharField(max_length=60, null=True, blank=False, unique=True)
    hop_alpha = models.IntegerField(null=True, )

    
    hoplist_origin = (
        (US, 'US'),
        (UK, 'UK'),
        (GERMANY, 'Germany'),
        (CANADA, 'Canada'),
        (POLAND, 'Poland'),
        (NEWZEALAND, 'New Zealand'),
        (AUSTRALIA, 'Australia'),
        (CZECREP, 'Czech Rep'),
        (FRANCE, 'France'),
        (SLOVENIA, 'Slovenia'),
    )
    
    hoplist_origin = models.CharField(max_length=15,
                                      choices=hoplist_origin,
                                      default=US)
    
    hoplist_type = (
        (AROMA, 'Aroma'),
        (BITTERING, 'Bittering'),
    )
    
    hoplist_type = models.CharField(max_length=10,
                                      choices=hoplist_type,
                                      default=AROMA)

    def __unicode__(self):
        return smart_unicode(self.hop_name)

############################ Yeast #############
class YeastList (models.Model):
    yeast_name = models.CharField(max_length=60, null=True, blank=False, unique=True)
    
    
    hoplist_origin = (
        (ALE, 'Ale'),
        (CHAMPAGNE, 'Champagne'),
        (LAGER, 'Lager'),
        (WHEAT, 'Wheat'),
        (WINE, 'Wine'),
    )
    
    hoplist_origin = models.CharField(max_length=10,
                                      choices=hoplist_origin,
                                      default=ALE)
    
    
    yeastlist_floc = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    
    yeastlist_floc = models.CharField(max_length=6,
                                      choices=yeastlist_floc,
                                      default=LOW)
    
    
    yeastlist_type = (
        (DRY, 'Dry'),
        (LIQUID, 'Liquid'),
    )
    
    yeastlist_type = models.CharField(max_length=6,
                                      choices=yeastlist_type,
                                      default=DRY)


    def __unicode__(self):
        return smart_unicode(self.yeast_name)






















