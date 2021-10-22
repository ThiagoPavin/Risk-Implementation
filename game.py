from world import World
from player import Player
import json

import random

from onMyWatch import OnMyWatch

import os

import threading

class Game:
    def __init__(self):

        self.world = World()
        self.player_1 = Player(1,40)
        self.player_2 = Player(2,40)
        self.player_neutral = Player(3,40)

        self.countries = self.world.country_list

        random.shuffle(self.countries)

        self.player_1.countries_owned = self.countries[0:21]
        self.player_2.countries_owned = self.countries[21:42]

        for country in self.player_1.countries_owned:
            country.owner = self.player_1
            self.player_1.set_new_troops(country,1)

        for country in self.player_2.countries_owned:
            country.owner = self.player_2
            self.player_2.set_new_troops(country,1)


def game_function(name):
    print("Thread %s: starting", name)
    game = Game()

    countries_data = {}

    for country in game.countries:
        countries_data[country.name] = {
            "neighbours": [neighbour.name for neighbour in country.neighbours],
            "owner": country.owner.id,
            "n_troops": country.n_troops
        }

    p1_countries_owned_names = [country.name for country in game.player_1.countries_owned]

    p1_data = {
        "count": game.player_1.count,
        "id": game.player_1.id,
        "n_new_troops": game.player_1.n_new_troops,
        "state": "mobilizing",
        "countries_owned": p1_countries_owned_names,
        "countries_conections": "working in progress",
        "countries_data": countries_data
    }

    p1_json = json.dumps(p1_data, indent = 4)

    with open("Logs\player_1.json", "w") as outfile:
        outfile.write(p1_json)
    
    print("Thread %s: finishing", name)

def whatch_function(name):
    print("Thread %s: starting", name)
    watch = OnMyWatch()
    watch.run()
    print("Thread %s: finishing", name)


if __name__ == '__main__':
    
    x = threading.Thread(target=game_function, args=(1,))
    x.start()

    y = threading.Thread(target=whatch_function, args=(2,))
    y.start()

    # with open("player_1_calls.json", "r") as openfile:
    #     p1_calls = json.load(openfile)
    #     # while(game.player_1.count < p1_calls)
