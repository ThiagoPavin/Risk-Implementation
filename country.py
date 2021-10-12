class Country:

    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.owner = None
        self.troops = []

    def add_neighbours(self, countries):
        for country in countries:
            self.neighbours.append(country)
        