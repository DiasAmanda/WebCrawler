#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unicodedata


class UrlBuilder:

    def __init__(self):
        pass


def remove_accents(text):
    text.replace('-', '  ')
    text = unicodedata.normalize('NFD', unicode(text, 'utf8')).encode('ASCII', 'ignore')
    text.replace('  ', '-')
    return text


def url_builder(city, city_id, state):
    remove_accents(city)
    remove_accents(state)
    url = 'https://www.climatempo.com.br/climatologia/{0}/{1}-{2}'.format(city_id, city, state).lower()
    print(url)

