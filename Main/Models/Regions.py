from selenium import webdriver
import time

browser = webdriver.Chrome("C:\Users\Amandinha\PycharmProjects\WebCrawler\Drivers\chromedriver.exe")


class States:

    def __init__(self):
        pass


states = []
cities = dict


def get_states():
    browser.get("https://www.climatempo.com.br/climatologia/2/santos-sp")
    total_uf = browser.execute_script("return document.getElementById('sel-state-geo').length")
    for object in range(total_uf):
        states.append(
            browser.execute_script('return document.getElementById("sel-state-geo").options[%d].value;' % object))
    print(states)
    return states


def get_cities():
    browser.get("https://www.climatempo.com.br/climatologia/2/santos-sp")
    for object in states:
        print(object)
        browser.execute_script("$('#sel-state-geo').val('%s').change()" % object)
        time.sleep(4000)
        total_city = browser.execute_script("return document.getElementById('sel-city-geo').length")
        for object in range(total_city):
            print(total_city)
            city_id = browser.execute_script(
                'return document.getElementById("sel-city-geo").options[%d].value;' % object)
            city_name = browser.execute_script(
                'return document.getElementById("sel-city-geo").options[%d].text;' % object)
            print(city_name, city_id)
            cities.update(city_id, city_name)
    return cities
