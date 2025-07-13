# my first dictionary

alien_0 = {'color': 'green', 'point': 5}

print(alien_0)
print(alien_0['color'])
print(alien_0['point'])

# adding value to a dictionary

alien_0['x-position'] = 0
alien_0['y-position'] = 25

print(alien_0)

# trying out various print statements with dictionary

print("The Details are:\n" \
    "color: " + alien_0['color'] +
    "\npoint: " + str(alien_0['point']) +
    "\nx-position: " + str(alien_0['x-position']) +
    "\ny-position: "+ str(alien_0['y-position']))

# usinf f-strings

print(f"""The details are:
color: {alien_0['color']}
point: {alien_0['point']}
x-postion: {alien_0['x-position']}
y-position: {alien_0['y-position']}""")