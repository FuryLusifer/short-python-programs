# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country, such
# as Santiago, Chile. Store the function in a module called city_functions.py,
# and save this file in a new folder so pytest won’t try to run the
# tests we’ve already written.

# Modify your function so it requires a third parameter, population. It should
# now return a single string of the form City, Country – population xxx,
# such as Santiago, Chile – population 5000000. Run the test again, and make 
# sure test_city_country() fails this time.

def city_country(city, country):
    formatted_text = f"{city}, {country}"
    return formatted_text.title()

def city_country_population(city, country, population=None):
    if population:
        formatted_text = (
            f"{city.title()}, {country.title()} - population {population}"
        )
        return formatted_text
    
    else:
        formatted_text = f"{city}, {country}"
        return formatted_text.title()