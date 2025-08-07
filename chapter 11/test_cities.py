# Create a file called test_cities.py that tests the function you just wrote.
# Write a function called test_city_country() to verify that calling your function
# with values such as 'santiago' and 'chile' results in the correct string. Run the
# test, and make sure test_city_country() passes.

from city_functions import city_country_population, city_country

def test_city_country():
    assert city_country("santiago", "chile") == "Santiago, Chile"
    assert city_country("mumbai", "india") == "Mumbai, India"
    assert city_country("KaTHmanDu", "NePAl") == "Kathmandu, Nepal"

def test_city_country_population():
    assert city_country_population("santiago", "chile") == "Santiago, Chile"
    assert city_country_population("mumbai", "india", 2500000) == "Mumbai, India - population 2500000"
    assert city_country_population("KaTHmanDu", "NePAl") == "Kathmandu, Nepal"