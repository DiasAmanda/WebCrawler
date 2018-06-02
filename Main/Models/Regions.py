from selenium import webdriver
import time

browser = webdriver.Chrome("C:\Users\Amandinha\PycharmProjects\WebCrawler\Drivers\chromedriver.exe")


class States:

    def __init__(self):
        pass


states = []
total_uf = 0
cities = {}

def get_states():
    browser.get("https://www.climatempo.com.br/climatologia/2/santos-sp")
    total_uf = browser.execute_script("return document.getElementById('sel-state-geo').length")
    print(total_uf)
    for object in range(total_uf):
        states.append(
            browser.execute_script('return document.getElementById("sel-state-geo").options[%d].value;' % object))
    print(states)
    return states


def get_cities():
    browser.get("https://www.climatempo.com.br/climatologia/2/santos-sp")
    for object in states:
        browser.execute_script("$('#sel-state-geo').val('%s').change()" % object)
        time.sleep(10)
        total_city = browser.execute_script("return document.getElementById('sel-city-geo').length")
        print("============================ESTADO: %s =============================" % object)
        print(total_city)
        print("\n \n \n")
        for city in range(total_city):
            city_id = browser.execute_script(
                'return document.getElementById("sel-city-geo").options[%d].value;' % city)
            city_name = browser.execute_script(
                'return document.getElementById("sel-city-geo").options[%d].text;' % city)
            cities[city_id] = city_name
    print(cities.values())
    return cities
