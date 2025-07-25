# Write a function that stores information about a car in a dictionary. The
# function should always receive a manufacturer and a model name. It should
# then accept an arbitrary number of keyword arguments. Call the function
# with the required information and two other name-value pairs, such as a color
# or an optional feature. Your function should work for a call like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure all the information was
# stored correctly.

def build_cars(manufacturer ,model_name, **my_car):
    '''summarizing the manufacturing of a car.'''
    my_car['manufacturer'] = manufacturer
    my_car['model_name'] = model_name
    return my_car


car = build_cars('subaru', 'outback', color='blue', tow_package=True)
print(car)