import NetSoup
from Company import Company
from Worker import Worker
from Regions import *

soup = NetSoup.connect("http://secura.e-sim.org/productMarket.html?resource=IRON&countryId=1&quality=1").get()
#$wep = Company(10895)
#iron = Company(9571)

