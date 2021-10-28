from world import World
from player import Player

import json
import random
import os
import time

class Game:
    def __init__(self):

        self.world = World()
        self.player_1 = Player(1,40)
        self.player_2 = Player(2,40)

    def create_command_files(self):

        p1_data = {
            "id": 1
        }

        p1_json = json.dumps(p1_data, indent = 4)


        p2_data = {
            "id": 2
        }

        p2_json = json.dumps(p2_data, indent = 4)

        with open("Calls\player_1.json", "w") as outfile:
            outfile.write(p1_json)

        self.last_m_time_p1 = os.path.getmtime("Calls\player_1.json")

        with open("Calls\player_2.json", "w") as outfile:
            outfile.write(p2_json)
        
        self.last_m_time_p2 = os.path.getmtime("Calls\player_2.json")


    def random_draft(self):

        random.shuffle(self.world.country_list)

        self.player_1.countries_owned = self.world.country_list[0:21]
        self.player_2.countries_owned = self.world.country_list[21:42]

        for country in self.player_1.countries_owned:
            country.owner = self.player_1
            self.player_1.set_new_troops(1, country)

        for country in self.player_2.countries_owned:
            country.owner = self.player_2
            self.player_2.set_new_troops(1, country)


    def update_players_data(self):

        countries_data = {} 

        for country in self.world.country_list:
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

        path = "Calls\player_" + str(id) + ".json"

        if id == 1:
            current_time = os.path.getmtime(path)

            while self.last_m_time_p1 == current_time:
                current_time = os.path.getmtime(path)

            time.sleep(0.000000001)

            self.last_m_time_p1 = current_time

        elif id == 2:
            current_time = os.path.getmtime(path)

            while self.last_m_time_p2 == current_time:
                current_time = os.path.getmtime(path)

            #TODO needs fix
            time.sleep(0.000000001)

            self.last_m_time_p2 = current_time

    def execute_player_action(self, id):
        #path = "Calls\player_1.json"
        path = "Calls\player_" + str(id) + ".json"    

        if id == 1:
            player = self.player_1
            enemy = self.player_2
        elif id == 2:
            player = self.player_2
            enemy = self.player_1

        #TODO needs fix
        while True:  
            try:
                with open(path) as openfile:
                    json_object = json.load(openfile)
                    
                    print(json_object)

                    break
            except:
                print("Oh, deu erro aqui") 
                
        if json_object["command"]["name"] == "attack":
            attacker = None
            attacked = None

            for country_owned in player.countries_owned:
                if country_owned.name == json_object["command"]["args"][1]:
                    attacker = country_owned
                    break
            
            for country_owned in enemy.countries_owned:
                if country_owned.name == json_object["command"]["args"][2]:
                    attacked = country_owned
                    break
            
            if(attacker == None):
                print("Player", id, "does not own any country named", json_object["command"]["args"][1])
            elif(attacked == None):
                print("Player", enemy.id, "does not own any country named", json_object["command"]["args"][2])
            else:
                has_won = player.attack(json_object["command"]["args"][0], attacker, attacked)
                if has_won:
                    #Set state to mobilizing_attack
                    pass
        
        elif json_object["command"]["name"] == "move_troops":
            from_country = None
            to_country = None

            for country_owned in player.countries_owned:
                if country_owned.name == json_object["command"]["args"][1]:
                    from_country = country_owned
                    break
            
            for country_owned in player.countries_owned:
                if country_owned.name == json_object["command"]["args"][2]:
                    to_country = country_owned
                    break
            
            if(from_country == None):
                print("Player", id, "does not own any country named", json_object["command"]["args"][1])
            elif(to_country == None):
                print("Player", id, "does not own any country named", json_object["command"]["args"][2])
            else:
                player.move_troops(json_object["command"]["args"][0], from_country, to_country)

        elif json_object["command"]["name"] == "set_new_troops":
            country = None

            for country_owned in player.countries_owned:
                if country_owned.name == json_object["command"]["args"][1]:
                    country = country_owned
                    break
            
            if(country == None):
                print("Player", id, "does not own any country named", json_object["command"]["args"][1])
            else:
                player.set_new_troops(json_object["command"]["args"][0], country)
        
        elif json_object["command"]["name"] == "pass_turn":
            print("Turn passed")
        
        else:
            print("Player", id, "is trying to use a command that does not exist (", json_object["command"]["name"], ")")
                
if __name__ == '__main__':

    game = Game()

    game.create_command_files()
    print("Criou os command files")

    game.random_draft()
    print("Distribuiu os paises")

    game.update_players_data()
    print("atualizou os dados dos player")

    count = 0

    while True:
        print("Esperando acao do player 1...")
        game.wait_for_agent(1)

        #game.execute_player_action(1)

        print(count)

        # game.execute_player_action(1)
        # print("Acao executada")
        
        # game.update_players_data()
        # print("atualizou os dados dos player")

        count += 1