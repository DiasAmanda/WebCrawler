from Main.Models.Regions import *
# from Main.Builders.UrlBuilder import *

regions = Regions()
states = regions.get_states()
cities = regions.get_cities()
