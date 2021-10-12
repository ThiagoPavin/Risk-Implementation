from country import Country
from troop import Troop

class Player:
    def __init__(self, id, n_new_troops):
        self.id = id
        self.countries_owned = []
        self.n_troops = 0
        self.n_new_troops = n_new_troops
    

    def attack(self, n_troops : int, attacker : Country, attacked : Country):
        pass

    def move_troops(self, n_troops : int, from_country : Country, to_country : Country):
        pass

    def set_new_troops(self, country : Country, n_troops : int):
        if(country.owner == self):
            if(n_troops <= self.n_new_troops):
                for _ in range(n_troops):
                    troop = Troop()
                    country.troops.append(troop)
                    self.n_new_troops -= 1
            else:
                print("Player esta tentando colocar tropas em pais que nao lhe pertence")
        else:
            print("Voce nao tem tropas suficientes")


    def pass_turn(self):
        pass