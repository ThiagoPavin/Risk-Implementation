from continent import Continent
from country import Country

class World:
    def __init__(self):

        north_america = Continent("North America")
        south_america = Continent("South America")
        australia = Continent("Australia")
        europe = Continent("Europe")
        asia = Continent("Asia")
        africa = Continent("Africa")

        north_america.extra_armies = 5
        south_america.extra_armies = 2
        australia.extra_armies = 2
        europe.extra_armies = 5
        asia.extra_armies = 7
        africa.extra_armies = 3
        
        north_america_countries = ["Alaska", "Alberta", "Ontario", "Western America", "Eastern America", "Quebec", "Central America", "Greenland", "Northwest America"]
        south_america_countries = ["Brazil", "Venezuela", "Peru", "Argentina"]
        australia_countries = ["Western Australia", "Eastern Australia", "Indoneasia", "Papua New Guinea"]
        europe_countries = ["Ukraine", "Skandinavia", "Iceland", "Great Britain", "Northern Europe", "Western Europe", "Southern Europe"]
        asia_countries = ["Yakutsk", "Siberia", "Kamchatka", "Irkutsk", "Ural", "Japan", "Mongolia", "China", "Middle East", "India", "Siam", "Afganistan"]
        africa_countries = ["Congo", "East Africa", "Egypt", "Madagascar", "North Africa", "South Africa"]

        continents_countries = [north_america_countries, south_america_countries, australia_countries, europe_countries, asia_countries, africa_countries]

        self.continents = [north_america, south_america, australia, europe, asia, africa]

        self.country_dict = {}
        self.country_list = []

        i = 0

        for continent in continents_countries:
            
            for country in continent:
                self.country_dict[country] = Country(country)
                self.country_list.append(self.country_dict[country])
                self.continents[i].countries.append(self.country_dict[country])

            i += 1

        # North America
        self.country_dict["Alaska"].add_neighbours([self.country_dict["Northwest America"], self.country_dict["Alberta"], self.country_dict["Kamchatka"]])
        self.country_dict["Alberta"].add_neighbours([self.country_dict["Alaska"], self.country_dict["Ontario"], self.country_dict["Northwest America"], self.country_dict["Western America"]])
        self.country_dict["Ontario"].add_neighbours([self.country_dict["Alberta"], self.country_dict["Quebec"], self.country_dict["Northwest America"], self.country_dict["Eastern America"], self.country_dict["Greenland"], self.country_dict["Western America"]])
        self.country_dict["Northwest America"].add_neighbours([self.country_dict["Alberta"], self.country_dict["Alaska"], self.country_dict["Ontario"], self.country_dict["Greenland"]])
        self.country_dict["Western America"].add_neighbours([self.country_dict["Alberta"], self.country_dict["Ontario"], self.country_dict["Central America"], self.country_dict["Eastern America"]])
        self.country_dict["Eastern America"].add_neighbours([self.country_dict["Ontario"], self.country_dict["Quebec"], self.country_dict["Central America"], self.country_dict["Western America"]])
        self.country_dict["Quebec"].add_neighbours([self.country_dict["Greenland"], self.country_dict["Ontario"], self.country_dict["Eastern America"]])
        self.country_dict["Central America"].add_neighbours([self.country_dict["Eastern America"], self.country_dict["Western America"], self.country_dict["Venezuela"]])
        self.country_dict["Greenland"].add_neighbours([self.country_dict["Ontario"], self.country_dict["Quebec"], self.country_dict["Northwest America"], self.country_dict["Iceland"]])

        # South America
        self.country_dict["Brazil"].add_neighbours([self.country_dict["Venezuela"], self.country_dict["Peru"], self.country_dict["Argentina"], self.country_dict["North Africa"]])
        self.country_dict["Venezuela"].add_neighbours([self.country_dict["Brazil"], self.country_dict["Peru"], self.country_dict["Central America"]])
        self.country_dict["Peru"].add_neighbours([self.country_dict["Brazil"], self.country_dict["Venezuela"], self.country_dict["Argentina"]])
        self.country_dict["Argentina"].add_neighbours([self.country_dict["Peru"], self.country_dict["Brazil"]])

        # Australia
        self.country_dict["Western Australia"].add_neighbours([self.country_dict["Eastern Australia"], self.country_dict["Indoneasia"], self.country_dict["Papua New Guinea"]])
        self.country_dict["Eastern Australia"].add_neighbours([self.country_dict["Papua New Guinea"], self.country_dict["Western Australia"]])
        self.country_dict["Indoneasia"].add_neighbours([self.country_dict["Siam"], self.country_dict["Papua New Guinea"], self.country_dict["Western Australia"]])
        self.country_dict["Papua New Guinea"].add_neighbours([self.country_dict["Indoneasia"], self.country_dict["Eastern Australia"], self.country_dict["Western Australia"]])

        # Europe
        self.country_dict["Ukraine"].add_neighbours([self.country_dict["Skandinavia"], self.country_dict["Northern Europe"], self.country_dict["Southern Europe"], self.country_dict["Middle East"], self.country_dict["Ural"], self.country_dict["Afganistan"]])
        self.country_dict["Skandinavia"].add_neighbours([self.country_dict["Iceland"], self.country_dict["Great Britain"], self.country_dict["Northern Europe"], self.country_dict["Ukraine"]])
        self.country_dict["Iceland"].add_neighbours([self.country_dict["Skandinavia"], self.country_dict["Great Britain"], self.country_dict["Greenland"]])
        self.country_dict["Great Britain"].add_neighbours([self.country_dict["Iceland"], self.country_dict["Skandinavia"], self.country_dict["Northern Europe"], self.country_dict["Western Europe"]])
        self.country_dict["Northern Europe"].add_neighbours([self.country_dict["Great Britain"], self.country_dict["Skandinavia"], self.country_dict["Ukraine"], self.country_dict["Western Europe"], self.country_dict["Southern Europe"]])
        self.country_dict["Western Europe"].add_neighbours([self.country_dict["Great Britain"], self.country_dict["Northern Europe"], self.country_dict["Southern Europe"], self.country_dict["North Africa"]])
        self.country_dict["Southern Europe"].add_neighbours([self.country_dict["Ukraine"], self.country_dict["Middle East"], self.country_dict["Egypt"], self.country_dict["North Africa"], self.country_dict["Western Europe"], self.country_dict["Northern Europe"]])

        # Asia
        self.country_dict["Yakutsk"].add_neighbours([self.country_dict["Siberia"], self.country_dict["Irkutsk"], self.country_dict["Kamchatka"]])
        self.country_dict["Siberia"].add_neighbours([self.country_dict["Yakutsk"], self.country_dict["Irkutsk"], self.country_dict["Mongolia"], self.country_dict["China"], self.country_dict["Ural"]])
        self.country_dict["Kamchatka"].add_neighbours([self.country_dict["Yakutsk"], self.country_dict["Irkutsk"], self.country_dict["Japan"], self.country_dict["Mongolia"], self.country_dict["Alaska"]])
        self.country_dict["Irkutsk"].add_neighbours([self.country_dict["Siberia"], self.country_dict["Kamchatka"], self.country_dict["Yakutsk"], self.country_dict["Mongolia"]])
        self.country_dict["Ural"].add_neighbours([self.country_dict["Ukraine"], self.country_dict["Afganistan"], self.country_dict["China"], self.country_dict["Siberia"]])
        self.country_dict["Japan"].add_neighbours([self.country_dict["Kamchatka"], self.country_dict["Mongolia"]])
        self.country_dict["Mongolia"].add_neighbours([self.country_dict["China"], self.country_dict["Siberia"], self.country_dict["Irkutsk"], self.country_dict["Kamchatka"], self.country_dict["Japan"]])
        self.country_dict["China"].add_neighbours([self.country_dict["Afganistan"], self.country_dict["Ural"], self.country_dict["Siberia"], self.country_dict["Mongolia"], self.country_dict["Siam"], self.country_dict["India"]])
        self.country_dict["Middle East"].add_neighbours([self.country_dict["India"], self.country_dict["Afganistan"], self.country_dict["Egypt"], self.country_dict["East Africa"], self.country_dict["Southern Europe"], self.country_dict["Ukraine"]])
        self.country_dict["India"].add_neighbours([self.country_dict["Middle East"], self.country_dict["Afganistan"], self.country_dict["China"], self.country_dict["Siam"]])
        self.country_dict["Siam"].add_neighbours([self.country_dict["China"], self.country_dict["India"], self.country_dict["Indoneasia"]])
        self.country_dict["Afganistan"].add_neighbours([self.country_dict["Ukraine"], self.country_dict["Ural"], self.country_dict["China"], self.country_dict["India"], self.country_dict["Middle East"]])

        # Africa
        self.country_dict["Congo"].add_neighbours([self.country_dict["North Africa"], self.country_dict["East Africa"], self.country_dict["South Africa"]])
        self.country_dict["East Africa"].add_neighbours([self.country_dict["Egypt"], self.country_dict["North Africa"], self.country_dict["Congo"], self.country_dict["South Africa"], self.country_dict["Madagascar"], self.country_dict["Middle East"]])
        self.country_dict["Egypt"].add_neighbours([self.country_dict["North Africa"], self.country_dict["East Africa"], self.country_dict["Southern Europe"], self.country_dict["Middle East"]])
        self.country_dict["Madagascar"].add_neighbours([self.country_dict["South Africa"], self.country_dict["East Africa"]])
        self.country_dict["North Africa"].add_neighbours([self.country_dict["Egypt"], self.country_dict["East Africa"], self.country_dict["Congo"], self.country_dict["Brazil"], self.country_dict["Western Europe"], self.country_dict["Southern Europe"]])
        self.country_dict["South Africa"].add_neighbours([self.country_dict["Congo"], self.country_dict["East Africa"], self.country_dict["Madagascar"]])