class Continent:
    def __init__(self, name):
        self.name = name
        self.countries = []
        self.owner = None
        self.extra_armies = 0

    def update_continent_owner(self):

        owner = None
        has_owner = True

        for country in self.countries:
            if owner == None:
                owner = country.owner
            elif owner != country.owner:
                has_owner = False
                break
        
        if has_owner:
            self.owner = owner
        else:
            self.owner = None
        

