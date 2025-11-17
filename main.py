from animal import animal
from hyena import hyena
from lion import lion

from datetime import date

#Create list of species
list_of_hyenas = []
list_of_lions = []
list_of_tigers = []
list_of_bears = []

#Birthday calculations
current_date = date.today()
current_year = current_date.year

def calc_birth_date(season, years):
    year_of_birth = int(current_year) - int(years)