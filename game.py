from world import World
from player import Player
import json

import random

import os

class Game:
    def __init__(self):

        self.world = World()
        self.player_1 = Player(1,40)
        self.player_2 = Player(2,40)
        self.player_neutral = Player(3,40)

        self.countries = self.world.country_list

    def create_command_files(self):

        p1_data = {
            "id": 1
        }

        p1_json = json.dumps(p1_data, indent = 4)


        p2_data = {
            "id": 2
        }

        p2_json = json.dumps(p2_data, indent = 4)

        with open("Commands\commands_player_1.json", "w") as outfile:
            outfile.write(p1_json)

        self.last_m_time_p1 = os.path.getmtime("Commands\commands_player_1.json")

        with open("Commands\commands_player_2.json", "w") as outfile:
            outfile.write(p2_json)
        
        self.last_m_time_p2 = os.path.getmtime("Commands\commands_player_2.json")


    def random_draft(self):

        random.shuffle(self.countries)

        self.player_1.countries_owned = self.countries[0:21]
        self.player_2.countries_owned = self.countries[21:42]

        for country in self.player_1.countries_owned:
            country.owner = self.player_1
            self.player_1.set_new_troops(country,1)

        for country in self.player_2.countries_owned:
            country.owner = self.player_2
            self.player_2.set_new_troops(country,1)


    def update_players_data(self):

        countries_data = {} 

        for country in self.countries:
            countries_data[country.name] = {
                "neighbours": [neighbour.name for neighbour in country.neighbours],
                "owner": country.owner.id,
                "n_troops": country.n_troops
            }

        # P1
        p1_countries_owned_names = [country.name for country in self.player_1.countries_owned]

        p1_data = {
            "count": self.player_1.count,
            "id": self.player_1.id,
            "n_new_troops": self.player_1.n_new_troops,
            "state": "mobilizing",
            "countries_owned": p1_countries_owned_names,
            "countries_conections": "working in progress",
            "countries_data": countries_data
        }

        p1_json = json.dumps(p1_data, indent = 4)

        with open("Logs\player_1.json", "w") as outfile:
            outfile.write(p1_json)

        # P2
        p2_countries_owned_names = [country.name for country in self.player_2.countries_owned]

        p2_data = {
            "count": self.player_2.count,
            "id": self.player_2.id,
            "n_new_troops": self.player_2.n_new_troops,
            "state": "mobilizing",
            "countries_owned": p2_countries_owned_names,
            "countries_conections": "working in progress",
            "countries_data": countries_data
        }

        p2_json = json.dumps(p2_data, indent = 4)

        with open("Logs\player_2.json", "w") as outfile:
            outfile.write(p2_json)



    def wait_for_agent(self, id):

        path = "Commands\commands_player_" + str(id) + ".json"

        last_m_time = 0

        if id == 1:
            last_m_time = self.last_m_time_p1
        elif id == 2:
            last_m_time = self.last_m_time_p2

        time = os.path.getmtime(path)

        while last_m_time == time:
            time = os.path.getmtime(path)
            
        
        last_m_time = time

    def execute_player_action(self, id):
        path = "Commands\commands_player_" + str(id) + ".json"

        if id == 1:
            player = self.player_1
        elif id == 2:
            player = self.player_2


        #with open(path, "r") as openfile:
        #     json_object = json.load(openfile)

        #     print(json_object["id"])

        #     #if json_object["command"]["name"] == "set_new_troops":
        #         #player.set_new_troops(json_object["command"]["args"][0], json_object["command"]["args"][1])
                


if __name__ == '__main__':

    game = Game()

    print("Criou os command files")
    game.create_command_files()

    print("Distribuiu os paises")
    game.random_draft()

    print("atualizou os dados dos player")
    game.update_players_data()

    print("Esperando acao do player 1 ...")
    game.wait_for_agent(1)

    print("Executando acao")
    game.execute_player_action(1)

    print("Executada!")

    print("atualizou os dados dos player")
    game.update_players_data()

    print("Esperando acao do player 1 ...")
    game.wait_for_agent(1)
