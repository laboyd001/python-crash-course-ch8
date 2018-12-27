#write a function that takes in city name and its country.  The function should return a string that looks like this: Santiago, Chile

# def city_country(city, country):
#     """Return a city and country name, neatly formatted."""
#     full_city_country = city + ',' + ' ' + country
#     return full_city_country.title()

# while True:
#     print("\nPlease tell me a city and its country:")
#     print("(enter 'q' at any time to quit)")

#     city_name = input("City name: ")
#     if city_name == 'q':
#         break
#     country_name = input("Country name: ")
#     if country_name == 'q':
#         break
#     formatted_name = city_country(city_name, country_name)
#     print("\n" + formatted_name)

def get_formatted_name(city, country):
    """Return a full name, neatly formatted."""
    full_name = city + ',' + ' ' + country
    return full_name.title()

city_country = get_formatted_name('owensboro', 'united states')
print(city_country)
city_country = get_formatted_name(city = 'paris', country = 'france')
print(city_country)
city_country = get_formatted_name('dublin', 'ireland')
print(city_country)