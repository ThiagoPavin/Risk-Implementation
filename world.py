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

        self.country_list = []

        for continent in continents:
            for country in continent:

                countries[country] = Country(country)
                self.country_list.append(countries[country])
        

        # North America
        countries["Alaska"].add_neighbours([countries["Northwest America"], countries["Alberta"], countries["Kamchatka"]])
        countries["Alberta"].add_neighbours([countries["Alaska"], countries["Ontario"], countries["Northwest America"], countries["Western America"]])
        countries["Ontario"].add_neighbours([countries["Alberta"], countries["Quebec"], countries["Northwest America"], countries["Eastern America"], countries["Greenland"], countries["Western America"]])
        countries["Northwest America"].add_neighbours([countries["Alberta"], countries["Alaska"], countries["Ontario"], countries["Greenland"]])
        countries["Western America"].add_neighbours([countries["Alberta"], countries["Ontario"], countries["Central America"], countries["Eastern America"]])
        countries["Eastern America"].add_neighbours([countries["Ontario"], countries["Quebec"], countries["Central America"], countries["Western America"]])
        countries["Quebec"].add_neighbours([countries["Greenland"], countries["Ontario"], countries["Eastern America"]])
        countries["Central America"].add_neighbours([countries["Eastern America"], countries["Eastern America"], countries["Venezuela"]])
        countries["Greenland"].add_neighbours([countries["Ontario"], countries["Quebec"], countries["Northwest America"], countries["Iceland"]])

        # South America
        countries["Brazil"].add_neighbours([countries["Venezuela"], countries["Peru"], countries["Argentina"], countries["North Africa"]])
        countries["Venezuela"].add_neighbours([countries["Brazil"], countries["Peru"], countries["Central America"]])
        countries["Peru"].add_neighbours([countries["Brazil"], countries["Venezuela"], countries["Argentina"]])
        countries["Argentina"].add_neighbours([countries["Peru"], countries["Brazil"]])

        # Australia
        countries["Western Australia"].add_neighbours([countries["Eastern Australia"], countries["Indoneasia"], countries["Papua New Guinea"]])
        countries["Eastern Australia"].add_neighbours([countries["Papua New Guinea"], countries["Western Australia"]])
        countries["Indoneasia"].add_neighbours([countries["Siam"], countries["Papua New Guinea"], countries["Western Australia"]])
        countries["Papua New Guinea"].add_neighbours([countries["Indoneasia"], countries["Eastern Australia"], countries["Western Australia"]])

        # Europe
        countries["Ukraine"].add_neighbours([countries["Skandinavia"], countries["Northern Europe"], countries["Southern Europe"], countries["Middle East"], countries["Ural"], countries["Afganistan"]])
        countries["Skandinavia"].add_neighbours([countries["Iceland"], countries["Great Britain"], countries["Northern Europe"], countries["Ukraine"]])
        countries["Iceland"].add_neighbours([countries["Skandinavia"], countries["Great Britain"], countries["Greenland"]])
        countries["Great Britain"].add_neighbours([countries["Iceland"], countries["Skandinavia"], countries["Northern Europe"], countries["Western Europe"]])
        countries["Northern Europe"].add_neighbours([countries["Great Britain"], countries["Skandinavia"], countries["Ukraine"], countries["Western Europe"], countries["Southern Europe"]])
        countries["Western Europe"].add_neighbours([countries["Great Britain"], countries["Northern Europe"], countries["Southern Europe"]])
        countries["Southern Europe"].add_neighbours([countries["Ukraine"], countries["Middle East"], countries["Egypt"], countries["North Africa"], countries["Western Europe"], countries["Northern Europe"]])

        # Asia
        countries["Yakutsk"].add_neighbours([countries["Siberia"], countries["Irkutsk"], countries["Kamchatka"]])
        countries["Siberia"].add_neighbours([countries["Yakutsk"], countries["Irkutsk"], countries["Mongolia"], countries["China"], countries["Ural"]])
        countries["Kamchatka"].add_neighbours([countries["Yakutsk"], countries["Irkutsk"], countries["Japan"], countries["Mongolia"]])
        countries["Irkutsk"].add_neighbours([countries["Siberia"], countries["Kamchatka"], countries["Yakutsk"], countries["Mongolia"]])
        countries["Ural"].add_neighbours([countries["Ukraine"], countries["Afganistan"], countries["China"], countries["Siberia"]])
        countries["Japan"].add_neighbours([countries["Kamchatka"], countries["Mongolia"]])
        countries["Mongolia"].add_neighbours([countries["China"], countries["Siberia"], countries["Irkutsk"], countries["Kamchatka"], countries["Japan"]])
        countries["China"].add_neighbours([countries["Afganistan"], countries["Ural"], countries["Siberia"], countries["Mongolia"], countries["Siam"], countries["India"]])
        countries["Middle East"].add_neighbours([countries["India"], countries["Afganistan"], countries["Egypt"], countries["East Africa"], countries["Southern Europe"], countries["Ukraine"]])
        countries["India"].add_neighbours([countries["Middle East"], countries["Afganistan"], countries["China"], countries["Siam"]])
        countries["Siam"].add_neighbours([countries["China"], countries["India"], countries["Indoneasia"]])
        countries["Afganistan"].add_neighbours([countries["Ukraine"], countries["Ural"], countries["China"], countries["India"], countries["Middle East"]])

        # Africa
        countries["Congo"].add_neighbours([countries["North Africa"], countries["East Africa"], countries["South Africa"]])
        countries["East Africa"].add_neighbours([countries["Egypt"], countries["North Africa"], countries["Congo"], countries["South Africa"], countries["Madagascar"], countries["Middle East"]])
        countries["Egypt"].add_neighbours([countries["North Africa"], countries["East Africa"], countries["Southern Europe"], countries["Middle East"]])
        countries["Madagascar"].add_neighbours([countries["South Africa"], countries["East Africa"]])
        countries["North Africa"].add_neighbours([countries["Egypt"], countries["East Africa"], countries["Congo"], countries["Brazil"], countries["Western Europe"]])
        countries["South Africa"].add_neighbours([countries["Congo"], countries["East Africa"], countries["Madagascar"]])