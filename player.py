from country import Country
import random

class Player:
    def __init__(self, id, n_new_troops):
        self.count = 0
        self.id = id
        self.countries_owned = []
        self.n_new_troops = n_new_troops
        self.state = None
    
    # Falta fazer se o atacante dominar o territorio
    def attack(self, n_dice : int, attacker : Country, attacked : Country):
        if attacker.owner == self:
            if attacked.owner != self:
                if attacked in attacker.neighbours:
                    attacked_dice = 0
                    if attacked.n_troops == 1:
                        attacked_dice = 1
                    else:
                        attacked_dice = 2

                    if attacker.n_troops > 1 and (attacker.n_troops - n_dice) >= 1:
                        attacker_dice_values = random.sample(range(1, 7), n_dice)
                        attacked_dice_values = random.sample(range(1, 7), attacked_dice)

                        attacked_dice_values.sort(reverse=True)
                        #print("attacked_dice_values = ", attacked_dice_values)

                        attacker_dice_values.sort(reverse=True)
                        #print("attacker_dice_values = ", attacker_dice_values)

                        for i in range(n_dice):
                            if attacked_dice_values[i] >= attacker_dice_values[i]:
                                attacker.n_troops -= 1
                                #print("attacked ganhou")
                            else:
                                attacked.n_troops -= 1
                                #print("attacker ganhou")

                            if i == len(attacked_dice_values) - 1:
                                break

                        if attacked.n_troops == 0:
                            attacked.owner = attacker.owner
                            attacked.n_troops += n_dice
                            attacker.n_troops -= n_dice

                            return True

                        return False

                    else:
                        print("Player", self.id, "doesn't have enough troops on", attacker.name, "to attack")
                else:
                    print("Player", self.id, "is trying to attack", attacked.name, "that is not neighbour of", attacker.name)
            else:
                print("Player", self.id, "is trying to attack his own country (", attacked.name,")")
        else:
            print("Player", self.id, "is trying to attack with enemy's country (", attacker.name,")")


    def move_troops(self, n_troops : int, from_country : Country, to_country : Country):
        if(from_country.owner == self):
            if(to_country.owner == self):
                if(n_troops < from_country.n_troops):
                    to_country.n_troops += n_troops
                    from_country.n_troops -= n_troops
                else:
                    print("Player", self.id, "is trying to move", n_troops, "troops, but has only", from_country.n_troops - 1, "available")
            else:
                print("Player", self.id, "is trying to move troops to enemy's country (", to_country.name, ")")
        else:
            print("Player", self.id, "is trying to move troops from enemy's country (", from_country.name, ")")

    def set_new_troops(self, n_troops : int, country : Country):
        if(country.owner == self):
            if(n_troops <= self.n_new_troops):
                country.n_troops += n_troops
                self.n_new_troops -= n_troops
            else:
                print("Player", self.id, "is trying to set", n_troops, "troops, but has only", self.n_new_troops)
        else:
            print("Player", self.id, "is trying to set troops in enemy's country (", country.name, ")")

    def pass_turn(self):
        pass