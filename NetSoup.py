#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from BeautifulSoup import BeautifulSoup

class Connection(object):
    addres = ""
    def __init__(self, addres):
        self.addres = addres
    def get(self):
        response = urllib2.urlopen(self.addres)
        return BeautifulSoup(response.read())
    def get_plain(self):
        response = urllib2.urlopen(self.addres)
        return response.read()

def connect(addres):
    return Connection(addres)
