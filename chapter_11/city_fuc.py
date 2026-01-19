def city_describe(city_name, country, population=''):
    if population:
        all_city = f'{city_name}, {country}, {population}'
    else:
        all_city = f'{city_name}, {country}'
    return all_city