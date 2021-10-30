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

        self.player_1.state = "mobilizing"
        self.player_2.state = "waiting"

        self.active_player = self.player_1

        self.winner = None


    def create_command_files(self):

        self.count_p1 = 0
        self.count_p2 = 0

        p1_data = {
            "id": 1,
            "count": self.count_p1
        }

        p1_json = json.dumps(p1_data, indent = 4)


        p2_data = {
            "id": 2,
            "count": self.count_p2
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
            "state": self.player_1.state,
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
            "state": self.player_2.state,
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

            last_count = self.count_p1

            while last_count == self.count_p1:
                while self.last_m_time_p1 == current_time:
                    current_time = os.path.getmtime(path)

                while True:
                    try:
                        with open(path) as openfile:
                            data = json.load(openfile)
                            if data["count"] == self.count_p1:
                                print("Atualizou sem precisar")
                            self.count_p1 = data["count"]
                            break
                    except:
                        print("Oh, deu erro aqui")


                current_time = os.path.getmtime(path)

                self.last_m_time_p1 = current_time

        elif id == 2:
            current_time = os.path.getmtime(path)

            last_count = self.count_p2

            while last_count == self.count_p2:
                while self.last_m_time_p2 == current_time:
                    current_time = os.path.getmtime(path)

                while True:
                    try:
                        with open(path) as openfile:
                            data = json.load(openfile)
                            if data["count"] == self.count_p2:
                                print("Atualizou sem precisar")
                            self.count_p2 = data["count"]
                            break
                    except:
                        print("Oh, deu erro aqui")


                current_time = os.path.getmtime(path)

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
                    enemy.countries_owned.remove(attacked)
                    player.countries_owned.append(attacked)
                    attacked.owner = attacker.owner
                    attacked.n_troops += json_object["command"]["args"][0]
                    attacker.n_troops -= json_object["command"]["args"][0]
                    player.state = "conquering"

                    if len(player.countries_owned) == 42:
                        self.winner = player
        
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

                if player.state == "conquering":
                    player.state = "attacking"

            

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

            if player.state == "mobilizing":
                player.state = "attacking"

            elif player.state == "attacking":
                player.state = "fortifying"

            elif player.state == "fortifying":
                player.state = "waiting"
                self.active_player = enemy
                enemy.state = "mobilizing"

            elif player.state == "conquering":
                print("Player", id, "cannot pass_turn during a conquering state")

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

    while True:
        print("Esperando acao do player 1...")
        game.wait_for_agent(game.active_player.id)

        game.execute_player_action(game.active_player.id)
        print("Acao executada")

        if game.winner != None:
            print(game.winner.id, "win!")
            
            if game.winner.id == 1:
                game.player_1.state = "winner"
                game.player_2.state = "loser"

            elif game.winner.id == 2:
                game.player_1.state = "loser"
                game.player_2.state = "winner"
                
        game.update_players_data()
        print("atualizou os dados dos player")