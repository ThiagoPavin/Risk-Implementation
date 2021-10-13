from world import World
from player import Player

import random

class Game:
    def __init__(self):

        self.world = World()
        self.player_1 = Player(1,40)
        self.player_2 = Player(2,40)
        self.player_neutral = Player(3,40)

        self.countries = self.world.country_list

        random.shuffle(self.countries)

        self.player_1.countries_owned = self.countries[0:14]
        self.player_2.countries_owned = self.countries[14:28]

        self.player_neutral.countries_owned = self.countries[28:42]

        for country in self.player_1.countries_owned:
            country.owner = self.player_1
            self.player_1.set_new_troops(country,1)

        for country in self.player_2.countries_owned:
            country.owner = self.player_2
            self.player_2.set_new_troops(country,1)

        for country in self.player_neutral.countries_owned:
            country.owner = self.player_neutral
            self.player_neutral.set_new_troops(country,1)
        
        for country in self.countries:
            print(country.name)

            if(country.owner != None):
                print("player =", country.owner.id)
            else:
                print("Neutral")
            
            print(len(country.troops))

if __name__ == '__main__':
    Game()  