from country import Country

class Player:
    def __init__(self, id, n_new_troops):
        self.id = id
        self.countries_owned = []
        self.n_troops = 0
        self.n_new_troops = n_new_troops
        self.state = None
    

    def attack(self, n_troops : int, attacker : Country, attacked : Country):
        pass

    def move_troops(self, n_troops : int, from_country : Country, to_country : Country):
        if(from_country.owner == self and to_country.owner == self):
            if(n_troops < from_country.n_troops):
                to_country.n_troops += n_troops
                from_country.n_troops -= n_troops
            else:
                print("Player esta tentando colocar tropas em pais que nao lhe pertence")
        else:
            print("Voce nao tem tropas suficientes")

    def set_new_troops(self, country : Country, n_troops : int):
        if(country.owner == self):
            if(n_troops <= self.n_new_troops):
                country.n_troops += n_troops
                self.n_new_troops -= n_troops
            else:
                print("Player esta tentando colocar tropas em pais que nao lhe pertence")
        else:
            print("Voce nao tem tropas suficientes")


    def pass_turn(self):
        pass