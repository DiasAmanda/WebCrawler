from Main.Models.Regions import *
from Main.Builders.UrlBuilder import *

get_states()
sample = get_cities()

for region in sample.items():
    url_builder(region.values(),region.keys(),region.values())



