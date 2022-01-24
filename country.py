class Country:

    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.owner = None
        self.n_troops = 0

    def add_neighbours(self, countries : list):
        for country in countries:
            self.neighbours.append(country)
        