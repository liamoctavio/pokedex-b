from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse    

def index(request):
    query = request.GET.get('query')
    pokemons = []
    if query:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{query.lower()}')
        if response.status_code == 200:
            pokemon_data = response.json()
            species_response = requests.get(pokemon_data['species']['url'])
            species_data = species_response.json()
            description = next((entry['flavor_text'] for entry in species_data['flavor_text_entries'] if entry['language']['name'] == 'en'), 'No description available.')
            pokemons.append({
                'name': pokemon_data['name'],
                'types': [t['type']['name'] for t in pokemon_data['types']],
                'height': pokemon_data['height'],
                'weight': pokemon_data['weight'],
                'number': pokemon_data['id'],
                'image': pokemon_data['sprites']['front_default'],
                'description': description,
            })
    else:
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=9')
        if response.status_code == 200:
            data = response.json()
            for item in data['results']:
                pokemon_data = requests.get(item['url']).json()
                species_response = requests.get(pokemon_data['species']['url'])
                species_data = species_response.json()
                description = next((entry['flavor_text'] for entry in species_data['flavor_text_entries'] if entry['language']['name'] == 'en'), 'No description available.')
                pokemons.append({
                    'name': pokemon_data['name'],
                    'types': [t['type']['name'] for t in pokemon_data['types']],
                    'height': pokemon_data['height'],
                    'weight': pokemon_data['weight'],
                    'number': pokemon_data['id'],
                    'image': pokemon_data['sprites']['front_default'],
                    'description': description,
                })
    return render(request, 'pokemon/index.html', {'pokemons': pokemons})

class PokemonList(APIView):
    def get(self, request):
        response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=12')
        if response.status_code == 200:
            data = response.json()
            pokemons = []
            for item in data['results']:
                pokemon_data = requests.get(item['url']).json()
                pokemons.append({
                    'name': pokemon_data['name'],
                    'type': pokemon_data['types'][0]['type']['name'],
                    'height': pokemon_data['height'],
                    'weight': pokemon_data['weight']
                })
            return Response(pokemons, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

def search_pokemon(request):
    query = request.GET.get('query')
    if query:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{query.lower()}')
        if response.status_code == 200:
            pokemon_data = response.json()
            pokemon = {
                'name': pokemon_data['name'],
                'type': pokemon_data['types'][0]['type']['name'],
                'height': pokemon_data['height'],
                'weight': pokemon_data['weight']
            }
            return render(request, 'pokemon/search_results.html', {'pokemon': pokemon})
    return render(request, 'pokemon/search_results.html', {'pokemon': None})

def autocomplete(request):
    query = request.GET.get('query', '').lower()
    if query:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon?limit=1000')
        if response.status_code == 200:
            data = response.json()
            suggestions = [pokemon['name'] for pokemon in data['results'] if pokemon['name'].startswith(query)]
            return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)