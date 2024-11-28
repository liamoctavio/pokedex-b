from django import template

register = template.Library()

@register.filter
def type_color(type_name):
    type_colors = {
        'fire': 'bg-fire',
        'water': 'bg-water',
        'grass': 'bg-grass',
        'electric': 'bg-electric',
        'ice': 'bg-ice',
        'fighting': 'bg-fighting',
        'poison': 'bg-poison',
        'ground': 'bg-ground',
        'flying': 'bg-flying',
        'psychic': 'bg-psychic',
        'bug': 'bg-bug',
        'rock': 'bg-rock',
        'ghost': 'bg-ghost',
        'dragon': 'bg-dragon',
        'dark': 'bg-dark',
        'steel': 'bg-steel',
        'fairy': 'bg-fairy'
    }
    return type_colors.get(type_name, 'bg-secondary')