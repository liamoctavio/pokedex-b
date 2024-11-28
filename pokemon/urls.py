from django.urls import path
from .views import index, PokemonList, search_pokemon, autocomplete

urlpatterns = [
    path('', index, name='index'),
    path('api/pokemon/', PokemonList.as_view(), name='pokemon_list'),
    path('search/', search_pokemon, name='search_pokemon'),
    path('autocomplete/', autocomplete, name='autocomplete'),


]