class Worker(object):
    id = 0;
    name = ""
    economy_skill = 0.0
    salary = 0.0
    profit = 0.0
    worked_today = False
    total_units_producted = 0.0
    productivity = 0.0
    def calc_production(self, company_type,raw_per_one_product, is_country_controls_capital = True, is_in_rich_region = True, employees_who_worked_today = 0, company_quality = 1):
        productivity = 10
        productivity *= (4 + self.economy_skill)

        if employees_who_worked_today <= 10 : productivity *=    (1.0 + (10-employees_who_worked_today) * 0.05)
        elif employees_who_worked_today <= 20 : productivity *=  (1.0 - (employees_who_worked_today-10) * 0.03)
        elif employees_who_worked_today <= 30 : productivity *=  (0.7 - (employees_who_worked_today-20) * 0.02)
        else: productivity *= 0.5

        if not is_country_controls_capital: productivity *= 0.75

        if company_type > 5 and is_in_rich_region: productivity *= 1.25
        if company_type <= 5 and not is_in_rich_region: productivity *= 0.75

        if company_type <= 5:
            if company_quality == 2: productivity *= 1.2
            elif company_quality == 3: productivity *= 1.4
            elif company_quality == 4: productivity *= 1.6
            elif company_quality == 5: productivity *= 1.8

        self.productivity = productivity

        if company_type > 5:
            self.total_units_producted = productivity/(raw_per_one_product)
        elif company_type <= 5:
            self.total_units_producted = productivity

    def __repr__(self):
        return self.__class__.__name__  + " (" + self.name + ")"
