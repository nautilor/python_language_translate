#!/usr/bin/env python3

from urllib.request import urlopen
import json

class yandex:
    def __init__(self):
        """ GET YOUR API AT https://tech.yandex.com/translate/  """
        self.key = 'YANDEX_KEY'
        self.link = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    def build(self, text, lang):
        return "%s?key=%s&text=%s&lang=%s" % (self.link, self.key, text, lang)

    def translate(self, text, language):
        try:
            data = urlopen(self.build(text.replace(' ', '+'), language))
            return json.load(data)['text'][0]
        except Exception:
            return "GENERIC ERROR"

