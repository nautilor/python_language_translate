#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs4
import urllib
import re

class reverso:
    def __init__(self):
        self.link = 'https://context.reverso.net/translation/'
        self.langs = {'it': 'italian', 'en': 'english', 'fr': 'french',
                      'de': 'german', 'jp': 'japanese', 'es': 'spanish'}

    def translate(self, main_language, foreign_language, data):
        data = data.replace(' ', '+')
        main_language = self.langs[main_language]
        foreign_language = self.langs[foreign_language]
        url = "%s%s-%s/%s" % (self.link, main_language, foreign_language, data)
        data = self.get_data(url)
        return self.words(data)

    def get_data(self, url):
        req = urllib.request.Request( url, data=None, headers={'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
        req = urllib.request.urlopen(req)
        return bs4(req.read(), 'lxml')

    def words(self, data):
        words = data.findAll('a', {'class': 'translation'})
        return [' '.join(self.de_html(word).split(' ')[1:]).lstrip() for word in words]


    def de_html(self, data):
        return re.sub('<[^>]*>', '', str(data))
