"""
The spectrum range of visible light is approximately
between 400 and 700 nanometers.

Among them, the violet light
with a wavelength of 400 nanometers has the shortest wavelength,
while the red light with a wavelength of 700 nanometers
has the longest wavelength.

The human eye is sensitive to light within this range,
so we can see the colors within this spectrum range.
According to the above facts, please write a program
to check if a specified wavelength is visible light or not.
"""

WAVELENGTH_MAX = 700
WAVELENGTH_MIN = 400

wavelength = 600

# wavelength <= 700 and wavelength >= 400
if 400 <= wavelength <= 700 :
    print('Visible light')
else:
    print('Not visible light')



