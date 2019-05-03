#!/usr/bin/env python3

from bs4 import BeautifulSoup as bs4
import urllib
import re

class reverso:
    def __init__(self):
        self.link = 'https://context.reverso.net/traduzione/italiano-inglese/'

    def translate(self, data):
        data = data.replace(' ', '+')
        url = "%s%s" % (self.link, data)
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
