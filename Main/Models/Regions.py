#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from selenium import webdriver
import time


browser = webdriver.Chrome("C:\Users\Amandinha\PycharmProjects\WebCrawler\Drivers\chromedriver.exe")


class Regions:

    def __init__(self):
        pass


states = []
total_uf = 0
cities = {}
state_dict = {}



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
    for state in states:
        browser.execute_script("$('#sel-state-geo').val('%s').change()" % state)
        time.sleep(10)
        total_city = browser.execute_script("return document.getElementById('sel-city-geo').length")
        print("============================ESTADO: %s =============================" % state)
        print(total_city)
        print("\n \n \n")
        for city in range(total_city):
            city_id = browser.execute_script(
                'return document.getElementById("sel-city-geo").options[%d].value;' % city)
            city_name = browser.execute_script(
                'return document.getElementById("sel-city-geo").options[%d].text;' % city)
            cities[city_id] = city_name
            print(cities)
            state_dict = { state : cities }
            if len(cities) > 99:
                return
    return state_dict


def call_urlbuilder():
    i = 0
    # for item in state_dict:
    inner_dict = state_dict[cities][0]
    print(inner_dict['city_name'][i])
    print('\n')
    print(inner_dict['city_id'][i])
    print('\n')
    print(inner_dict.keys[i])
    print('\n')
    # url_builder(dic_item['city_name'][i],dic_item['city_id'][i],dic_item.keys()[i])
    i += 1


get_states()
get_cities()
call_urlbuilder()