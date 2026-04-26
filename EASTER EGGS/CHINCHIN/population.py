presentPopulation =312032486
birthRate = 7
deathRate =13
mmigrant = 45
secPerYear = 365 * 24 * 60 * 60
birthPerYear = secPerYear // birthRate
immigrantPerYear = secPerYear // immigrant
	
population = birthPerYear + immigrantPerYear - deathPerYear
years = int(input("Enter number of years: "))
years = years * population;
print("Population is " + years)

