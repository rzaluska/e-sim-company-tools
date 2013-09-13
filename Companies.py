from Company import Company
from CompanyType import CompanyType
from Market import *
class Companies:
    def __init__(self, companies_id_list):
        self.companies_list = []
        for id in companies_id_list:
            newc = Company(id)
            self.companies_list.append(newc)

    def get_total_production(self):
        t = []
        for c in self.companies_list:
            n = {}
            n["type"] = c.type
            n["total units producted"] =  c.total_units_producted
            n["quality"] = c.quality
            t.append(n)

        return t

    def get_total_consumpcion(self):
        w = []
        for c in self.companies_list:
            t = {}
            if c.type <= 5:
                if not c.type in t.keys():
                    t[c.type] = 0
            elif c.type == CompanyType.WEAPON:
                t["type"] = CompanyType.IRON
                t[CompanyType.IRON] = 0
                t[CompanyType.IRON] += c.total_productivity
                else: t[CompanyType.IRON] += c.total_productivity
            elif c.type == CompanyType.FOOD:
                if not CompanyType.GRAIN in t.keys():
                    t[CompanyType.GRAIN] = 0
                    t[CompanyType.GRAIN] += c.total_productivity
                else: t[CompanyType.GRAIN] += c.total_productivity
            elif c.type == CompanyType.GIFT:
                if not CompanyType.DIAMONDS in t.keys():
                    t[CompanyType.DIAMONDS] = 0
                    t[CompanyType.DIAMONDS] += c.total_productivity
                else: t[CompanyType.DIAMONDS] += c.total_productivity
            elif c.type == CompanyType.TICKET:
                if not CompanyType.OIL in t.keys():
                    t[CompanyType.OIL] = 0
                    t[CompanyType.OIL] += c.total_productivity
                else: t[CompanyType.OIL] += c.total_productivity
            elif c.type == CompanyType.HOUSE:
                if not CompanyType.WOOD in t.keys():
                    t[CompanyType.WOOD] = 0
                    t[CompanyType.WOOD] += c.total_productivity
                else: t[CompanyType.WOOD] += c.total_productivity
            elif c.type == CompanyType.DEFENSE_SYSTEM or c.type == CompanyType.HOSPITAL or e.type == CompanyType.ESTATE:
                if not CompanyType.STONE in t.keys():
                    t[CompanyType.STONE] = 0
                    t[CompanyType.STONE] += c.total_productivity
                else: t[CompanyType.STONE] += c.total_productivity

        return w

    def get_flow(self):
        t = {}
        p = self.get_total_production()
        c = self.get_total_consumpcion()

        for kp, vp in p.items():
            for kc, vc in c.items():
                if kc == kp:
                    t[kp] = vp - vc
                else:
                    t[kp] = vp
        return t

    def get_total_profit(self):
        total_profit = 0
        flow = self.get_flow()
        for c in self.companies_list:
            for fk,fv in flow.items():
                if c.type == fk:
                    price_for_one = get_first_offer_price(c.type,c.country_id,c.quality)
                    pr = price_for_one * c.total_units_producted
                    total_profit += pr

        return total_profit





c = Companies([9571,10895])
