import math

PI = math.pi

r = input('Enter a random radius for a sphere: ')

r = float(r)

surfaceArea = 4 * (r**2) * PI

print('The surface area of a sphere with a radius of {} is {}'.format(r,surfaceArea))