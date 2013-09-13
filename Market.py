#!/usr/bin/env python
# -*- coding: utf-8 -*-

import NetSoup
from CompanyType import *

def get_first_offer_price(resource=0,countryId=1,quality=1):
    addres = "http://secura.e-sim.org/productMarket.html?resource="+get_name_of_company_type(resource) +"&countryId="+ str(countryId)+"&quality=" + str(quality)
    soup = NetSoup.connect(addres).get()
    return float(soup.find("table",{"class":"dataTable"}).findAll('tr')[1].findAll('td')[3].find('b').text)

