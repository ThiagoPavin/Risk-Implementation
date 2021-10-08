from country import Country


from country import Country

class World:
    def __init__(self):
        
        north_america = ["Alaska", "Alberta", "Ontario", "Western America", "Eastern America", "Quebec", "Central America", "Greenland", "Northwest America"]
        south_america = ["Brazil", "Venezuela", "Peru", "Argentina"]
        australia = ["Western Australia", "Eastern Australia", "Indoneasia", "Papua New Guinea"]
        europe = ["Ukraine", "Skandinavia", "Iceland", "Great Britain", "Northern Europe", "Western Europe", "Southern Europe"]
        asia = ["Yakutsk", "Siberia", "Kamchatka", "Irkutsk", "Ural", "Japan", "Mongolia", "China", "Middle East", "India", "Siam", "Afganistan"]
        africa = ["Congo", "East Africa", "Egypt", "Madagascar", "North Africa", "South Africa"]

        continents = [north_america, south_america, australia, europe, asia, africa]

        countries = {}

        for continent in continents :
            for country in continent :

                countries[country] = Country(country)
        


        countries["Alaska"].add_neighbours([countries["Northwest America"], countries["Alberta"], countries["Kamchatka"]])

        for country in countries["Alaska"].neighbours:
            print(country.name)



world = World()