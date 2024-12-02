from django.urls import path
from .views import index, PokemonList, search_pokemon, autocomplete, pokemon_detail

urlpatterns = [
    path('', index, name='index'),
    path('api/pokemon/', PokemonList.as_view(), name='pokemon_list'),
    path('search/', search_pokemon, name='search_pokemon'),
    path('autocomplete/', autocomplete, name='autocomplete'),
    path('pokemon/<str:pokemon_name>/', pokemon_detail, name='pokemon_detail'),



]