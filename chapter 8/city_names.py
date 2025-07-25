# Write a function called city_country() that takes in the name of a city and
# its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country pairs, and
# print the values that are returned.

def city_country(city, country):
    '''prints formatted city, country '''
    name = f"{city.title()}, {country.title()}"
    return name

print(city_country("santiago", "Chile"))
print(city_country("new delhi", "india"))
print(city_country("kathmandu", "nepal"))