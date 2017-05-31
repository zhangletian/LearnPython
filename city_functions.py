def city_country(city,country,population=''):
	if population:
		formatted_message = city.title() + ',' + country.title() + ' - population ' + str(population)
	else:
		formatted_message = city.title() + ',' + country.title()
	return formatted_message
