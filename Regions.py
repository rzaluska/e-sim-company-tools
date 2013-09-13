#!/usr/bin/env python
# -*- coding: utf-8 -*-

import NetSoup
import json
from CompanyType import CompanyType

def get_countries():
    page = NetSoup.connect("http://secura.e-sim.org/apiCountries.html").get_plain()
    return json.loads(page)

def get_regions():
    page = NetSoup.connect("http://secura.e-sim.org/apiRegions.html").get_plain()
    return json.loads(page)

def get_map_api():
    page = NetSoup.connect("http://primera.e-sim.org/apiMap.html").get_plain()
    return json.loads(page)

countries = get_countries()
#regions = get_regions()
map_api = get_map_api()

def get_country_id(country_name):
    for country in countries:
        if country["name"] == country_name:
            return country["id"]

def is_country_controls_capital(country_id):
        for country in countries:
            if country["id"] == country_id:
                capitalRegionId = country['capitalRegionId']
                for region in map_api:
                    if region['regionId'] == capitalRegionId:
                        if region["occupantId"] == country_id:
                            return True
                        else: return False

def get_country_regions_ids(country_id):
    country_regions = []
    for region in map_api:
        if region['occupantId'] == country_id:
            country_regions.append(region['regionId'])
    return country_regions

def is_in_regions_highly_rich_in_resources(region_id):
    for region in map_api:
        if region['regionId'] == region_id:
            if region['rawRichness'] == "HIGH":
                return True
            elif region['rawRichness'] == "MEDIUM":
                return False
            else: return False

def is_country_controls_proper_high_raw_region(country_id, manufacted_object_type):
    if manufacted_object_type > 5:
        regions = get_country_regions_ids(country_id)
        for region in map_api:
            if region['regionId'] in regions:
                if region['rawRichness'] != "NONE":
                    if region['raw'] == "IRON":
                        if manufacted_object_type == CompanyType.WEAPON:
                            return True
                    elif region['raw'] == "OIL":
                        if manufacted_object_type == CompanyType.TICKET:
                            return True
                    elif region['raw'] == "GRAIN":
                        if manufacted_object_type == CompanyType.FOOD:
                            return True
                    elif region['raw'] == "DIAMONDS":
                        if manufacted_object_type == CompanyType.GIFT:
                            return True
                    elif region['raw'] == "STONE":
                        if manufacted_object_type == CompanyType.DEFENSE_SYSTEM or manufacted_object_type == CompanyType.HOSPITAL or manufacted_object_type == CompanyType.ESTATE:
                            return True
                    elif region['raw'] == "WOOD":
                        if manufacted_object_type == CompanyType.HOUSE:
                            return True
    else:
        raise AttributeError("Not manufacture company type passed in arguments")
    return False


class RegionRawRichness:
    MEDIUM = 0
    HIGH = 1
