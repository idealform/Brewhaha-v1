from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.contrib import admin
admin.autodiscover()

from rest_framework import routers, serializers, viewsets
from brew_app.views import BrewLogViewset, RecipeViewset, RecipeListView, RecipeCreateView, RecipeUpdateView, BrewlogListView, BrewlogDetailView, BrewlogCreateView, GrainListViewset, HopListViewset, YeastListViewset, RecipeDetailView


router = routers.DefaultRouter()
router.register(r'brewlogs', BrewLogViewset)
router.register(r'recipes', RecipeViewset)
router.register(r'grainlist', GrainListViewset)
router.register(r'hoplist', HopListViewset)
router.register(r'yeastlist', YeastListViewset)


urlpatterns = patterns('',
    #url(r'xadmin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'brew_app.views.home', name='home'),
    
    #API
    url(r'^api/', include(router.urls)),
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Recipe urls
    url(r'^recipes/$', RecipeListView.as_view(), name='recipe_list'),
    url(r'^recipes/(?P<pk>\d+)', RecipeDetailView.as_view(), name='recipe_detail'),
    url(r'^recipes/edit/(?P<pk>\d+)', RecipeUpdateView.as_view(), name='recipe_edit'),
    url(r'^recipes/add/$', RecipeCreateView.as_view(), name='recipe_form'),     
    
    # Brewlog urls
    url(r'^brewlogs/$', BrewlogListView.as_view(), name='brewlog_list'),
    url(r'^brewlogs/(?P<pk>\d+)', BrewlogDetailView.as_view(), name='brewlog_detail'),
    url(r'^brewlogs/add/$', BrewlogCreateView.as_view(), name='brewlog_form'), 
    )



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)