class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []


    def add_pokemon(self, pokemon):
        found_pokemon = next((p for p in self.pokemons if p == pokemon), None)

        if not found_pokemon:
            self.pokemons.append(pokemon)

            return f'Caught {pokemon.name} with health {pokemon.health}'
        return 'This pokemon is already caught'


    def release_pokemon(self, pokemon_name):
        released_pokemon = next ((p for p in self.pokemons if p.name == pokemon_name), None)

        if released_pokemon:
            self.pokemons.remove(released_pokemon)
            return f'You have released {pokemon_name}'
        return 'Pokemon is not caught'


    def trainer_data(self):
        info = f'Pokemon Trainer {self.name}\n'
        info += f'Pokemon count {len(self.pokemons)}\n'
        for pokemon in self.pokemons:
            info += f'- {pokemon.pokemon_details()}\n'

        return info
