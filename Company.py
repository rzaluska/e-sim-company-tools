import re
import NetSoup
from CompanyType import CompanyType
from Worker import Worker
from Regions import *

class Company(object):
    id = 0
    name = 0
    employer_id = 0
    employer = ""
    country_name = ""
    country_id = 0
    is_country_controls_capital = False
    region_name = ""
    region_id = 0
    region_type = 0
    quality = 0
    is_in_regions_highly_rich_in_resources = False
    is_country_controls_proper_high_raw_region = False
    raw_per_one_product = 0
    employees_who_worked_today = 0
    production_progress = 0.0
    total_employees = 0
    total_productivity = 0.0
    total_units_needed = 0.0
    total_units_producted = 0.0
    type = 0
    workers = []
    page = ""
    def __init__(self,company_id):
        self.workers = []
        addres = "http://secura.e-sim.org/company.html?id=" + str(company_id)
        soup = NetSoup.connect(addres).get()
        self.id = int( re.findall("=([0-9]+)", soup.find("div",{'id':"unitStatusHead"}).find("a").attrs[0][1])[0] )
        self.name = soup.find("div",{'id':"unitStatusHead"}).find("a").text
        self.employer_id = int( re.findall("=([0-9]+)",soup.find("div",{'id':"militaryLeader"}).find("a").attrs[0][1])[0] )
        self.employer = soup.find("div",{'id':"militaryLeader"}).find("a").text


        if len(soup.findAll("div",{'class':"product"})) == 1:
            self.quality = int(re.findall("q([1-5])",soup.findAll("div",{'class':"product"})[0].findAll('img')[1].attrs[0][1])[0])
            type = re.findall("s/(.+).png",soup.findAll("div",{'class':"product"})[0].findAll('img')[0].attrs[0][1])[0]
            if type == "Iron": self.type = CompanyType.IRON
            elif type == "Grain": self.type = CompanyType.GRAIN
            elif type == "Oil": self.type = CompanyType.OIL
            elif type == "Stone": self.type = CompanyType.STONE
            elif type == "Wood": self.type = CompanyType.WOOD
            elif type == "Diamonds": self.type = CompanyType.DIAMONDS

        elif len(soup.findAll("div",{'class':"product"})) == 2:
            self.quality = int(re.findall("q([1-5])",soup.findAll("div",{'class':"product"})[1].findAll('img')[1].attrs[0][1])[0])
            type = re.findall("s/(.+).png",soup.findAll("div",{'class':"product"})[1].findAll('img')[0].attrs[0][1])[0]
            if type == "Weapon": self.type = CompanyType.WEAPON
            elif type == "Food": self.type = CompanyType.FOOD
            elif type == "Gift": self.type = CompanyType.GIFT
            elif type == "Ticket": self.type = CompanyType.TICKET
            elif type == "House": self.type = CompanyType.HOUSE
            elif type == "Defense System": self.type = CompanyType.DEFENSE_SYSTEM
            elif type == "Hospital": self.type = CompanyType.HOSPITAL
            elif type == "Estate": self.type = CompanyType.ESTATE



        self.employees_who_worked_today = int(soup.findAll("div",{'class':"statsLabelRight smallStatsLabel blueLabel"})[1].text)
        self.total_employees = int(soup.findAll("div",{'class':"statsLabelRight smallStatsLabel blueLabel"})[2].text)
        if self.type > 5: self.raw_per_one_product = int(soup.findAll("div",{'class':"statsLabelRight smallStatsLabel blueLabel"})[-1].text)


        self.country_name = re.findall("/(\w+).png",soup.findAll("div",{'class':"statsLabelRight smallStatsLabel blueLabel countryLabel"})[0].find("img").attrs[2][1])[0]
        self.country_id = get_country_id(self.country_name)

        self.region_name = soup.findAll("div",{'class':"statsLabelRight smallStatsLabel blueLabel countryLabel"})[0].find("a").text
        self.region_id = int(re.findall("=([0-9]+)",soup.findAll("div",{'class':"statsLabelRight smallStatsLabel blueLabel countryLabel"})[0].find("a").attrs[0][1])[0])

        self.is_country_controls_capital = is_country_controls_capital(self.country_id)
        self.is_in_regions_highly_rich_in_resources = is_in_regions_highly_rich_in_resources(self.region_id)
        if self.type > 5: self.is_country_controls_proper_high_raw_region = is_country_controls_proper_high_raw_region(self.country_id,self.type)
        else :self.is_country_controls_proper_high_raw_region = False

        workers_rows = soup.find("div",{'style':"width:330px;text-align:center;font-size:11px;float:right;margin-right:30px;"}).findAll("tr",{"class":"tableRow"})
        e = 0
        self.total_units_producted = 0.0
        self.total_units_needed = 0.0
        self.total_productivity = 0.0
        for row in workers_rows:
            w = Worker()
            w.name = row.findAll('td')[0].text
            w.id = int(re.findall("=([0-9]+)",row.findAll('td')[0].find('a').attrs[0][1])[0])
            w.economy_skill = float(row.findAll('td')[1].text)
            w.salary = float(row.findAll('td')[2].find('b').text)
            w.calc_production(self.type, self.raw_per_one_product, is_country_controls_capital = self.is_country_controls_capital, is_in_rich_region = self.is_in_regions_highly_rich_in_resources or self.is_country_controls_proper_high_raw_region, employees_who_worked_today = e, company_quality = self.quality)
            self.workers.append(w)
            self.total_units_producted += w.total_units_producted
            if self.type >5: self.total_units_needed += w.productivity
            self.total_productivity += w.productivity
            e+=1

    def __repr__(self):
        return self.__class__.__name__  + " (" + self.name + ")"












