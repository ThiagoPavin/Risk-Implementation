from world import World
from player import Player
from country import Country

import json
import random
import os

class Game:
    def __init__(self):

        self.world = World()
        self.player_1 = Player(1,40)
        self.player_2 = Player(2,40)

        self.turn = 0

        self.player_1.state = "mobilizing"
        self.player_2.state = "waiting"

        self.player_1.control.call_count = 0
        self.player_2.control.call_count = 0
        
        self.player_1.control.call_path = "Calls\player_1.json"
        self.player_2.control.call_path = "Calls\player_2.json"
        
        self.player_1.control.data_path = "Logs\player_1.json"
        self.player_2.control.data_path = "Logs\player_2.json"

        self.active_player = self.player_1

        self.winner = None

        self.map_changed = True

        self.unity_world_data_path = "Logs\\Unity_world_data.json"
        self.unity_commands_data_path = "Logs\\Unity_commands_data.json"

        self.unity_commands_dict = []

        self.unity_commands_data = []

    def _distribute_new_troops(self, player : Player):
        n_countries_owned = len(player.countries_owned)
        n_new_troops = int(n_countries_owned // 3)
        n_new_troops = max(n_new_troops, 3)

        bonus_troops = 0

        for continent in self.world.continents:
            if continent.owner == player:
                bonus_troops += continent.extra_armies
        
        print("Total bonus = ", bonus_troops)

        n_new_troops += bonus_troops
        player.n_new_troops += n_new_troops
        

    def _create_call_data(self, id: int, call_count: int) -> str:
        data = {
            'id': id,
            'count': call_count,
            'command': {
                'name': "",
                'args': []
            }  
        }

        json_data = json.dumps(data, indent = 4)
        
        return json_data

    def _update_json_file(self, path : str, json_data : str):
        with open(path, "w") as outfile:
            outfile.write(json_data)

    # TODO
    # Make a _update_countries_data where it updates only the changeable data
    def _create_countries_data(self) -> dict:
        countries_data = {} 

        for country in self.world.country_list:
            countries_data[country.name] = {
                "neighbours": [neighbour.name for neighbour in country.neighbours],
                "owner": country.owner.id,
                "n_troops": country.n_troops
            }

        return countries_data

    # TODO
    # Make a _update_continents_data where it updates only the changeable data
    def _create_continents_data(self) -> dict:
        continents_data = {}

        for continent in self.world.continents:
            continent_owner = None
            
            if continent.owner != None:
                continent_owner = continent.owner.id

            continents_data[continent.name] = {
                "owner": continent_owner,
                "extra_armies": continent.extra_armies,
                "countries": [country.name for country in continent.countries]
            }

        return continents_data

    def _is_connected(self, country_1 : Country, country_2 : Country, countries_visited : list) -> bool:
        for neighbour in country_1.neighbours:
            if neighbour in countries_visited:
                continue
            elif neighbour.owner == country_1.owner:
                if neighbour == country_2:
                    return True
                else:
                    countries_visited.append(neighbour)
                    if self._is_connected(neighbour, country_2, countries_visited):
                        return True
                    else:
                        return False
        return False

    def _create_connection_matrix(self, player : Player):
        player.connection_matrix = {} 

        for country in player.countries_owned:
            player.connection_matrix[country.name] = {}
        
        for country_1 in player.countries_owned:
            for country_2 in player.countries_owned:
                if country_1 == country_2:
                    continue
                elif (country_1, country_2) in player.connection_matrix.items():
                    continue
                else:
                    countries_visited = []
                    countries_visited.append(country_1)
                    if self._is_connected(country_1, country_2, countries_visited):
                        player.connection_matrix[country_1.name][country_2.name] = True
                        player.connection_matrix[country_2.name][country_1.name] = True
                    else:
                        player.connection_matrix[country_1.name][country_2.name] = False
                        player.connection_matrix[country_2.name][country_1.name] = False

    def _create_border_countries(self, player : Player):
        player.border_countries = {}

        for country in player.countries_owned:
                for neighbour in country.neighbours:
                    if self.world.country_dict[neighbour.name].owner != player:
                        if country.name not in player.border_countries:
                            player.border_countries[country.name] = []
                            player.border_countries[country.name].append(neighbour.name)
                        else:
                            player.border_countries[country.name].append(neighbour.name)

    def _create_player_data(self, continents_data: dict, countries_data : dict, player : Player) -> str:
        countries_owned_names = [country.name for country in player.countries_owned]

        player.data_count += 1

        if self.map_changed:
            self._create_border_countries(player)
            self._create_connection_matrix(player)

        if player.id == 1:
            enemy = self.player_2
        else:
            enemy = self.player_1

        data = {
            "count": player.data_count,
            "id": player.id,
            "n_new_troops": player.n_new_troops,
            "n_total_troops": player.n_total_troops,
            "enemy_n_total_troops": enemy.n_total_troops,
            "state": player.state,
            "countries_owned": countries_owned_names,
            "countries_data": countries_data,
            "border_countries": player.border_countries,
            "connection_matrix": player.connection_matrix,
            "continents_data": continents_data
        }

        json_data = json.dumps(data, indent = 4)

        return json_data

    def create_command_files(self):

        p1_json_data = self._create_call_data(1, self.player_1.control.call_count)
        p2_json_data = self._create_call_data(2, self.player_2.control.call_count)

        self._update_json_file(self.player_1.control.call_path, p1_json_data)
        self.last_m_time_p1 = os.path.getmtime(self.player_1.control.call_path)
        
        self._update_json_file(self.player_2.control.call_path, p2_json_data)
        self.last_m_time_p2 = os.path.getmtime(self.player_2.control.call_path)

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

        # Distribute troops randomly among countries owned
        while self.player_1.n_new_troops > 0:
            country = random.choice(self.player_1.countries_owned)
            self.player_1.set_new_troops(random.randint(0, self.player_1.n_new_troops), country)
        
        while self.player_2.n_new_troops > 0:
            country = random.choice(self.player_2.countries_owned)
            self.player_2.set_new_troops(random.randint(0, self.player_2.n_new_troops), country)

    def update_players_data(self):

        countries_data = self._create_countries_data()
        continents_data = self._create_continents_data()

        p1_json_data = self._create_player_data(continents_data, countries_data, self.player_1)
        p2_json_data = self._create_player_data(continents_data, countries_data, self.player_2)

        self._update_json_file(self.player_1.control.data_path, p1_json_data)
        self._update_json_file(self.player_2.control.data_path, p2_json_data)

    def wait_for_agent(self, player : Player):
        
        current_time = os.path.getmtime(player.control.call_path)

        last_count = player.control.call_count

        while last_count == player.control.call_count:
            while player.control.last_m_time == current_time:
                current_time = os.path.getmtime(player.control.call_path)

            while True:
                try:
                    with open(player.control.call_path) as openfile:
                        call_data = json.load(openfile)
                        if call_data["count"] == player.control.call_count:
                            #print("Atualizou sem precisar")
                            pass
                        else:
                            player.control.last_call_data = player.control.call_data
                            player.control.call_data = call_data
                        player.control.call_count = call_data["count"]
                        break
                except:
                    #print("Oh, deu erro aqui")
                    pass

            current_time = os.path.getmtime(player.control.call_path)

            player.control.last_m_time = current_time

    def _attack(self, player : Player, enemy : Player):
        attacker = None
        attacked = None

        for country_owned in player.countries_owned:
            if country_owned.name == player.control.call_data["command"]["args"][1]:
                attacker = country_owned
                break
        
        for country_owned in enemy.countries_owned:
            if country_owned.name == player.control.call_data["command"]["args"][2]:
                attacked = country_owned
                break        
            
        attacker_n_troops_before_attack = attacker.n_troops

        attacked_n_troops_before_attack = attacked.n_troops
        
        if(attacker == None):
            print("Player", id, "does not own any country named", player.control.call_data["command"]["args"][1])
        elif(attacked == None):
            print("Player", enemy.id, "does not own any country named", player.control.call_data["command"]["args"][2])
        else:
            has_won = player.attack(player.control.call_data["command"]["args"][0], attacker, attacked)

            attacker_troops_after = attacker_n_troops_before_attack - attacker.n_troops
            attacked_troops_after = attacked_n_troops_before_attack - attacked.n_troops

            attacker.owner.n_total_troops -= attacker_troops_after
            attacked.owner.n_total_troops -= attacked_troops_after

            if has_won:
                enemy.countries_owned.remove(attacked)
                player.countries_owned.append(attacked)
                attacked.owner = attacker.owner
                attacked.n_troops += player.control.call_data["command"]["args"][0]
                attacker.n_troops -= player.control.call_data["command"]["args"][0]
                player.state = "conquering"

                if len(player.countries_owned) == 42:
                    self.winner = player
            
            self.unity_commands_dict.append( {
                "id" : player.id,
                "tipo" : "attack",
                "dice_number" : player.control.call_data["command"]["args"][0],
                "name_out" : attacker.name,
                "out_number" : attacker_troops_after,
                "name_in" : attacked.name,
                "in_number" : attacked_troops_after,
                "conquered" : has_won
            } )
            self.map_changed = has_won

    def _move_troops(self, player : Player, enemy : Player):
        from_country = None
        to_country = None

        if player.state == 'conquering':
            if player.control.call_data['command']['args'][1] != player.control.last_call_data['command']['args'][1] or player.control.call_data['command']['args'][2] != player.control.last_call_data['command']['args'][2]:
                print("Player", player.id, "can only move between", player.control.last_call_data['command']['args'][1], "and", player.control.last_call_data['command']['args'][2], "during a conquering")
                return

        if player.state == 'fortifying':
            country_1 = player.control.call_data["command"]["args"][1]
            country_2 = player.control.call_data["command"]["args"][2]
            if not player.connection_matrix[country_1][country_2]:
                print("Player", player.id, "is trying to mobilize troops between countries not connected (", country_1, "-", country_2, ")")
                return
            

        for country_owned in player.countries_owned:
            if country_owned.name == player.control.call_data["command"]["args"][1]:
                from_country = country_owned
                break
        
        for country_owned in player.countries_owned:
            if country_owned.name == player.control.call_data["command"]["args"][2]:
                to_country = country_owned
                break
        
        if(from_country == None):
            print("Player", id, "does not own any country named", player.control.call_data["command"]["args"][1])
        elif(to_country == None):
            print("Player", id, "does not own any country named", player.control.call_data["command"]["args"][2])
        else:
            player.move_troops(player.control.call_data["command"]["args"][0], from_country, to_country)

            if player.state == "conquering":
                player.state = "attacking"
                self.unity_commands_dict.append( {
                    "id" : player.id,
                    "tipo" : "move_troops",
                    "dice_number" : 0,
                    "name_out" : player.control.call_data["command"]["args"][1],
                    "out_number" : player.control.call_data["command"]["args"][0],
                    "name_in" : player.control.call_data["command"]["args"][2],
                    "in_number" : player.control.call_data["command"]["args"][0],
                    "conquered" : False
                } ) 

            elif player.state == "fortifying":
                self.unity_commands_dict.append( {
                    "id" : player.id,
                    "tipo" : "move_troops",
                    "dice_number" : 0,
                    "name_out" : player.control.call_data["command"]["args"][1],
                    "out_number" : player.control.call_data["command"]["args"][0],
                    "name_in" : player.control.call_data["command"]["args"][2],
                    "in_number" : player.control.call_data["command"]["args"][0],
                    "conquered" : False
                } )
                self._pass_turn(player, enemy)

    def _set_new_troops(self, player : Player):
        country = None

        for country_owned in player.countries_owned:
            if country_owned.name == player.control.call_data["command"]["args"][1]:
                country = country_owned
                break
        
        if(country == None):
            print("Player", id, "does not own any country named", player.control.call_data["command"]["args"][1])
        else:
            player.set_new_troops(player.control.call_data["command"]["args"][0], country)

        self.unity_commands_dict.append( {
                "id" : player.id,
                "tipo" : "set_new_troops",
                "dice_number" : 0,
                "name_out" : "N",
                "out_number" : 0,
                "name_in" : player.control.call_data["command"]["args"][1],
                "in_number" : player.control.call_data["command"]["args"][0],
                "conquered" : False
        } ) 

    def _pass_turn(self, player : Player, enemy : Player):

        if player.state == "mobilizing":
            player.state = "attacking"

        elif player.state == "attacking":
            player.state = "fortifying"

        elif player.state == "fortifying":

            self.unity_commands_dict.append( {
                "id" : player.id,
                "tipo" : "pass_turn",
                "dice_number" : 0,
                "name_out" : "N",
                "out_number" : 0,
                "name_in" : "N",
                "in_number" : 0,
                "conquered" : False
            } ) 
            
            player.state = "waiting"
            self.turn = self.turn + 1
            self.active_player = enemy
            enemy.state = "mobilizing"
            self._distribute_new_troops(self.active_player)

            self.unity_commands_data.append( {
                "turn_number": self.turn,
                "calls": self.unity_commands_dict
            } )

            self.unity_commands_dict = []

        elif player.state == "conquering":
            print("Player", id, "cannot pass_turn during a conquering state")

        

    def execute_player_action(self, id : int):
        self.map_changed = False

        if id == 1:
            player = self.player_1
            enemy = self.player_2
        elif id == 2:
            player = self.player_2
            enemy = self.player_1

        call_data = player.control.call_data
        print(call_data)
                
        if call_data["command"]["name"] == "attack":
            self._attack(player, enemy)
        
        elif call_data["command"]["name"] == "move_troops":
            self._move_troops(player, enemy) 

        elif call_data["command"]["name"] == "set_new_troops":
            self._set_new_troops(player)
        
        elif call_data["command"]["name"] == "pass_turn":
            self._pass_turn(player, enemy)

        else:
            print("Player", id, "is trying to use a command that does not exist (", call_data["command"]["name"], ")")

        #print('Player:', id, 'count:', call_data['count'])


    def create_unity_world_data_log(self):

        countries_dict = []

        for country in self.world.country_list:
            countries_dict.append( {
                "name": country.name,
                "owner": country.owner.id,
                "n_troops": country.n_troops
            } )

        countries = {"countries" : countries_dict}

        json_data = json.dumps(countries, indent = 4)

        with open(self.unity_world_data_path, "w") as outfile:
            outfile.write(json_data)


    def create_unity_commands_log(self):

        data = {"turns" : self.unity_commands_data}

        json_data = json.dumps(data, indent = 4)

        with open(self.unity_commands_data_path, "w") as outfile:
            outfile.write(json_data)
                
if __name__ == '__main__':

    game = Game()

    game.create_command_files()
    #print("Criou os command files")

    game.random_draft()
    #print("Distribuiu os paises")

    game._distribute_new_troops(game.active_player)

    game.update_players_data()
    #print("Atualizou os dados dos player")

    game.create_unity_world_data_log()

    while game.turn < 150:
        game.wait_for_agent(game.active_player)

        game.execute_player_action(game.active_player.id)

        if game.winner != None:
            #print('Player', game.winner.id, "win!")
            
            if game.winner.id == 1:
                game.player_1.state = "winner"
                game.player_2.state = "loser"

            elif game.winner.id == 2:
                game.player_1.state = "loser"
                game.player_2.state = "winner"
            
            game.update_players_data()
            game.turn += 1
            break
                
        game.update_players_data()

    game.unity_commands_data.append( {
        "turn_number": game.turn,
        "calls": game.unity_commands_dict
    } )
    
    game.create_unity_commands_log()