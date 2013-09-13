#!/usr/bin/env python
# -*- coding: utf-8 -*-

class CompanyType(object):
    IRON = 0
    GRAIN = 1
    OIL = 2
    STONE = 3
    WOOD = 4
    DIAMONDS = 5
    WEAPON = 6
    FOOD = 7
    GIFT = 8
    TICKET = 9
    HOUSE = 10
    DEFENSE_SYSTEM = 11
    HOSPITAL = 12
    ESTATE = 13



def get_name_of_company_type(company_type):
    if company_type == CompanyType.IRON:
        return "IRON"
    elif company_type == CompanyType.GRAIN:
        return "GRAIN"
    elif company_type == CompanyType.OIL:
        return "OIL"
    elif company_type == CompanyType.STONE:
        return "STONE"
    elif company_type == CompanyType.WOOD:
        return "WOOD"
    elif company_type == CompanyType.DIAMONDS:
        return "DIAMONDS"
    elif company_type == CompanyType.WEAPON:
        return "WEAPON"
    elif company_type == CompanyType.FOOD:
        return "FOOD"
    elif company_type == CompanyType.TICKET:
        return "TICKET"
    elif company_type == CompanyType.HOUSE:
        return "HOUSE"
    elif company_type == CompanyType.DEFENSE_SYSTEM:
        return "DEFENSE_SYSTEM"
    elif company_type == CompanyType.HOSPITAL:
        return "HOSPITAL"
    elif company_type == CompanyType.ESTATE:
        return "ESTATE"




